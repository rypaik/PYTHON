#from config import console, log
from config import console

def say_hello(message):
    print(message)

    console.print(message, style="bold blue")

    # log.info(message)

    return message
