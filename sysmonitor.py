import psutil as ps
import time
import logging
import threading
import smtplib



class SystemStats:
    def __init__(self):
        self.cpu_count=ps.cpu_count()
        self.cpu_freq=ps.cpu_percent(percpu=True)
        self.v_mem=ps.virtual_memory()
        self.disk_part=ps.disk_partitions(all=True)

    def MonitorThread(self):
        while True:
            MEng=MonitorEngine().logging()
            time.sleep(5)

class MonitorEngine(SystemStats):
    def __init__(self):
        super().__init__()
        self.port = 25
        self.smtp_server = "smtp.freesmtpservers.com"
        self.sender_email="mridultiwari2002@gmail.com"
        self.receiver_email="mridultiwari2002@gmail.com"
        self.message=[]

    def logging(self):
        logging.basicConfig(
                filename="sys.log",
                filemode="a",
                level=logging.INFO,
                format="%(levelname)s - %(asctime)s - %(message)s",
                datefmt="%Y-%m-%d %H:%M"
        )

        for cpu in self.cpu_freq:
            if (cpu>1):
                msg="CPU Usage increased threashold"
                logging.error(msg)        
                self.message.append(msg)
            else:
                logging.info("CPU Usage: %.f",(cpu))
        
        if (self.v_mem.free<2000):
            msg="Memory Free below threshold of 2000"
            logging.error(msg)
            self.message.append(msg)
        else:
            logging.info("Memory usage: %.f",(self.v_mem.free))

        for part in self.disk_part:
            if (ps.disk_usage(part.mountpoint).percent>13):
                msg="Disk Usage Incresed beyond threshold of 13"
                logging.error(msg)
                self.message.append(msg)
            else:
                logging.info("Disk Usage: %.2f",(ps.disk_usage(part.mountpoint).percent))
        try:
            with smtplib.SMTP(self.smtp_server,self.port) as server:
                server.starttls()
                server.sendmail(self.sender_email,self.receiver_email,str(self.message))
            print("Email Sent!")
        except:
            raise Exception("SMTP Server fconnection failed!")

if __name__=="__main__":
    sys=SystemStats()
    t=threading.Thread(target=sys.MonitorThread, daemon=True)
    t.start()

    t.join()
