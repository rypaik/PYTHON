from dotenv import load_dotenv
import os
from rich.console import Console

from common.tools.lg import Logger

load_dotenv(verbose=True)

# Poner aquí cualquier otra variable que haya que cargar del archivo .env
# List any other variables that need to be loaded from the .env file
ENV_VAR = os.getenv('ENV_VAR', 'TEST')
STORAGE_LOGS = os.getenv('STORAGE_LOGS')

console = Console()
log = Logger(log_dir=STORAGE_LOGS).logger
