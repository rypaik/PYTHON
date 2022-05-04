from loguru import logger
# from _pytest.logging import caplog as _caplog
import logging

logger.remove(0)

def func():
    logger.info("This is a log message.")
    # print(type(caplog))

    
# if __name__ == "__main__":
#     func()


