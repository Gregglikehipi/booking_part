import logging
import os
from datetime import datetime

# Create a directory for log files
log_directory = "logs"
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

# Configure the logging
log_file = os.path.join(log_directory, "app.log")
logging.basicConfig(level=logging.DEBUG,
                    format='[%(asctime)s] %(message)s',
                    datefmt='%d.%m.%y %H:%M:%S',
                    handlers=[logging.FileHandler(log_file, 'a', 'utf-8')])

def log_message(message):
    """
    Logs a message to the log file with the current date and time.

    Parameters:
    message (str): The message to be logged.
    """
    try:
        logging.info(message)
    except Exception as e:
        logging.error(f"Failed to log message: {e}")

