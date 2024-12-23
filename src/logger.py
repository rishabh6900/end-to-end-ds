import logging  # Import the logging module for creating logs.
import os  # Import os module for interacting with the file system.
from datetime import datetime  # Import datetime to handle date and time.

# Generate a unique log file name based on the current timestamp.
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Define the directory path where logs will be stored.
# Combines the current working directory (cwd) with a "logs" folder and the log file name.
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)

# Create the directory structure for the logs if it does not already exist.
os.makedirs(logs_path, exist_ok=True)

# Full path to the log file.
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Configure the logging settings.
logging.basicConfig(
    filename=LOG_FILE_PATH,  # Specify the log file to write logs to.
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",  # Format for log messages.
    level=logging.INFO,  # Set the logging level to INFO (captures INFO and above: WARNING, ERROR, CRITICAL).
)

# if __name__=="__main__":
#     logging.info("Logging has started")