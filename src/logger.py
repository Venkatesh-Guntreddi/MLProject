import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# 1. This should ONLY be the directory path
logs_dir_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs")

# 2. Create the directory (not a directory named after the file)
os.makedirs(logs_dir_path, exist_ok=True)

# 3. Join the directory path with the file name
LOG_FILE_PATH = os.path.join(logs_dir_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,  # <--- CRITICAL: Use the full PATH here, not just the name
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s -%(message)s",
    level=logging.INFO,
)

