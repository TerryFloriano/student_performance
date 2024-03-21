import logging
import os
from datetime import datetime

FILE_LOG = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

logs_path = os.path.join(os.getcwd(), "logs", FILE_LOG)
os.makedirs(logs_path, exist_ok= True)

FILE_LOG_PATH = os.path.join(logs_path, FILE_LOG)

logging.basicConfig(
    filename = FILE_LOG_PATH,
    format = "[%(asctime)s]  %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level = logging.INFO,
)
