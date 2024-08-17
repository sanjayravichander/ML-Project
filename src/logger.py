import logging #The logging module is used for tracking events that happen when some software runs. You can use it to log messages that you want to appear in your log files or the console.
import os
from datetime import datetime
import __main__

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" # This variable stores the name of the log file, which is a string formatted with the current date and time, followed by .log. This ensures each log file has a unique name based on when it's created.
log_path=os.path.join(os.getcwd(),"logs",LOG_FILE) 
os.makedirs(log_path, exist_ok=True) #  This joins the current working directory path with the logs directory and the log file name. The os.path.join function ensures the paths are combined correctly regardless of the operating system.
LOG_FILE_PATH=os.path.join(log_path, LOG_FILE)  # This variable now holds the full path to where the log file will be stored, such as /path/to/current/directory/logs/08_17_2024_14_35_22.log.

logging.basicConfig(
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    handlers=[
        logging.FileHandler(LOG_FILE_PATH),
        logging.StreamHandler()
    ]
)

"""
Summary
The code sets up a logging system that logs messages both to a file and to the console.
The log file is stored in a logs directory, with a filename based on the current date and time.
The log format includes the timestamp, line number, logger name, log level, and message.
The logging level is set to INFO, so it will capture informational messages and above.
This setup is useful for tracking and debugging applications, as it allows you to review logs from both the console and a file.
"""