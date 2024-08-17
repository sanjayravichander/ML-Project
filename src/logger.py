import logging # Contains basic info of all excecution in files so that we can track some errors. Even custom exceptions errors, we can log into that file.
import os
from datetime import datetime
import __main__

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" # Log file name
log_path=os.path.join(os.getcwd(),"logs",LOG_FILE) # Log file path
os.makedirs(log_path, exist_ok=True) # Overlapping and appending the log file
LOG_FILE_PATH=os.path.join(log_path, LOG_FILE) # Log file path

logging.basicConfig(
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    handlers=[
        logging.FileHandler(LOG_FILE_PATH),
        logging.StreamHandler()
    ]
)
