import argparse

import config
# from common.tools.lg import Logger
from config import console
from modules.hello_world.tools.tools import say_hello


def run(**kwargs):
    message = kwargs.get('message')

    say_hello(message)

    print(f"I am reading a config var and it's value is: {config.ENV_VAR}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='')

    parser.add_argument(
        '--message', type=str,
        help='The message to use',
        required=True
    )

    args = parser.parse_args()

    console.print("=== Received args: ")
    console.print(args.__dict__)

    run(**args.__dict__)
