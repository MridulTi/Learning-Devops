import logging

class DailyLogging:
    def __init__(self):
        logger=logging.basicConfig(
                filename="logger.log",
                filemode="a",
                level=logging.DEBUG,
                format="%(levelname)s - %(message)s - %(asctime)s",
                datefmt="%H:%M:%s -%A ,%d-%B-%Y "
        )

        logging.info("Daily Check In at")

if __name__=="__main__":
    log=DailyLogging()
