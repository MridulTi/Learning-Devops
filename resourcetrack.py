import psutil as ps
import time
import logging
import threading
import smtplib
import rich
from rich.live import Live
from rich.table import Table

class SystemStats:
    def __init__(self):
        self.cpu_count=ps.cpu_count()
        self.cpu_freq=ps.cpu_percent(percpu=True)
        self.v_mem=ps.virtual_memory()
        self.disk_part=ps.disk_partitions(all=True)

    def MonitorThread(self,table):
        while True:
            MEng=MonitorEngine(table).logging()
            time.sleep(5)

class MonitorEngine(SystemStats):
    def __init__(self,table):
        super().__init__()
        self.table=table
        
    def logging(self):
        for cpu in self.cpu_freq:
            if (cpu>1):
                msg="CPU Usage increased threashold"
                self.table.add_row(msg)        
            else:
                self.table.add_row(f"CPU Usage: {cpu}")
        
        if (self.v_mem.free<2000):
            msg="Memory Free below threshold of 2000"
            self.table.add_row(msg)
        else:
            self.table.add_row(f"Memory usage: {self.v_mem.free}")

        for part in self.disk_part:
            if (ps.disk_usage(part.mountpoint).percent>13):
                msg="Disk Usage Incresed beyond threshold of 13"
                self.table.add_row(msg)
            else:
                self.table.add_row(f"Disk Usage: {ps.disk_usage(part.mountpoint).percent}")

if __name__=="__main__":
    SysStat=SystemStats()
    table=Table()
    with Live(table,transient=True,screen=True, refresh_per_second=1) as live:
        for _ in range(40):
            live.update(SysStat.MonitorThread(table))
            
