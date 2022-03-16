import functools
from logu_wrap_module import logger_wraps
from loguru import logger
import sys

logger.remove(0)
logger.add(sys.stdout)
logger.add("./logs/file_{time:MMM-DD: HH:mm}.log", level="TRACE", rotation="100 MB")
@logger_wraps()
def foo(a, b, c):
    logger.info("Inside the function")
    return a * b * c

def bar():
    foo(2, 4, c=8)

bar()

