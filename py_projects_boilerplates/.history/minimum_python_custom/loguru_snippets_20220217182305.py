from loguru import logger


# Basic Starting


from loguru import logger

logger.debug("Simple Logging")


# no handler, no formatter, no filter - one function
logger.add(sys.stderr, format="{time} {level} {message}", filter="my_module" level="INFO")


# sending log  to a file
logger.add("file_{time}.log", rotation="1 week")


#string formatting using braces
logger.info("If you're using Python {}, prefer {feature} of course!", 3.6, feature="f-strings")



# logging with colors
logger.add(sys.stdout, colorize=True, format="<green>{time}</green> <level>{message}</level>")