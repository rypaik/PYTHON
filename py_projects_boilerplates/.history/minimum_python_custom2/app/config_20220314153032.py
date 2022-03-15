from dotenv import load_dotenv
import os
from rich.console import Console

# from common.tools.log import Logger
# from loguru import logger
load_dotenv(verbose=True)

# Set here any other var available at the .env file

ENV_VAR = os.getenv('ENV_VAR')
STORAGE_LOGS = os.getenv('STORAGE_LOGS')
PROJECT_BASE = os.getenv('./')

console = Console()
log = logger(log_dir=STORAGE_LOGS).logger