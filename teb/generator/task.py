import logging
import logging.handlers as handlers
import time
from datetime import datetime
import random, os

logger = logging.getLogger('teb_task')
logger.setLevel(logging.INFO)

# Here we define our formatter
formatter = logging.Formatter('%(asctime)s %(message)s')

os.makedirs("city_logs", exist_ok=True)

logHandler = handlers.RotatingFileHandler('city_logs/app.log', maxBytes=2097152, backupCount=2)
logHandler.setLevel(logging.INFO)
logger.addHandler(logHandler)

def main():
    while True:
        time.sleep(1)
        cities = ["Istanbul","Tokyo", "Moskow","Beijing","London"]
        log_levels = ["INFO","WARN","FATAL","DEBUG","ERROR"]
        log_date = str(datetime.now())
        city = random.choice(cities)
        log_level = random.choice(log_levels)
        logger.info(log_date + " " + log_level + " " + city + " " + "Hello_from_" + city)

if __name__ == "__main__":
    main()