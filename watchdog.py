import psutil
from configparser import *
import argparse
from threading import *
import subprocess
import time
import logging as logger
from datetime import datetime, timedelta

class WatchDog:
    def __init__(self):
        self.config=ConfigParser()
        self.config.read('myapp.cfg')
        logger.basicConfig(
                filename="service.log",
                filemode="a",
                level=logger.DEBUG,
                format="%(levelname)s - %(message)s - %(asctime)s",
                datefmt="%H:%M:%S - %A ,%d-%B-%Y "
        )

    def check_restart_time(self,name):
        now = datetime.now()
        count=0
        window_time = self.config.get('DEFAULT','window_time')
        threshold = self.config.get('DEFAULT','threshold')
        with open("service.log", "r") as f:
            for line in f:
                if "Restarted" in line:
                    try:
                        parts = line.strip().split(" - ")
                        log_time_str = " - ".join(parts[-2:])
                        log_time=datetime.strptime(log_time_str,"%H:%M:%S - %A ,%d-%B-%Y")
                        if log_time > now - timedelta(minutes = int(window_time)):
                            count+=1
                    except Exception as e:
                        print(f"Error checking restart time: {e}")
                        continue
        return count >= threshold

    def is_process_running(self,name):
        return any(proc.info["name"] == name for proc in psutil.process_iter(attrs=["name"]))

    def listprocess(self):
        self.service_name = self.config.get('DEFAULT','service_name')
        while True:
            try:
                if (self.is_process_running(self.service_name)):
                    print(f"{self.service_name} is running.")
                else:
                    print(f" {self.service_name} is NOT running. Restarting ... ")
                    try:
                        result = subprocess.run(['service',self.service_name,'start'],capture_output=True,text=True,check=True)
                        if (result.returncode==0):
                             print(f"{self.service_name} is running.")
                             logger.error(f"{self.service_name} | Restarted")
                             if (self.check_restart_time(self.service_name)):
                                 print("Sent Mail!")

                    except subprocess.CalledProcessError as e:
                        print(f"Failed to restart {self.service_name} : {e}")
                        logger.error(f"{self.service_name} | Failed to Restart")
            except:
                print("Error while running the script")
            finally:
                time.sleep(5)


if __name__=="__main__":
    wD=WatchDog()
    t=Thread(target=wD.listprocess , daemon=True)
    t.start()
    t.join()
