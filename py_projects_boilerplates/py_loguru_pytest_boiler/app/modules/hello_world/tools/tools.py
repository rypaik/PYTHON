#from config import console, log
from config import console
from loguru import logger
import sys
#TODO: factory function to create logger

# setting up Logger
logger.add(sys.stderr, format="{time} {level} {message}", level="INFO")
logger.add("./common/loguru_log/Tools_{time}.log", rotation="500 MB")

# @logger.catch 
# @logger.catch
def say_hello(message):
    # print(message)
    console.print(message, style="bold blue")
    return message
    logger.bind(special=True).info("This message, though, is logged to the file!")