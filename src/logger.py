# logging → used to record messages (like errors, warnings, info) in your program.
# os → helps create folders and handle file paths.
# datetime → used to get the current date and time.
import logging
import os
from datetime import datetime

LOGS_DIR = "logs"
os.makedirs(LOGS_DIR,exist_ok=True) #creates that folder if it doesn’t already exist (so your program won’t crash if it’s already there).

# So, every day, a new log file is created automatically with the date in its name.
LOG_FILE = os.path.join(LOGS_DIR, f"log_{datetime.now().strftime('%Y-%m-%d')}.log")


logging.basicConfig(
    filename=LOG_FILE,
    format='%(asctime)s - %(levelname)s - %(message)s',
    level = logging.INFO
)
#level=logging.INFO → tells Python to record messages that are INFO level or higher (INFO, WARNING, ERROR, etc.).


#logger with given name
def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    return logger
