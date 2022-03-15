from loguru import logger
import sys

# Basic Starting


from loguru import logger

logger.debug("Simple Logging")

# logging with colors
logger.add(sys.stdout, colorize=True, format="<green>{time}</green> <level><red>{message}</red></level>")

# no handler, no formatter, no filter - one function
logger.add(sys.stderr, colorize= True, format="{time} <red>{level}</red> {message}", filter="my_module",  level="INFO")


# sending log  to a file
logger.add(log_dir=STORAGE_LOGS,"file_{time}.log", rotation="1 week")


#string formatting using braces
logger.info("If you're using Python {}, prefer {feature} of course!", 3.6, feature="f-strings")


