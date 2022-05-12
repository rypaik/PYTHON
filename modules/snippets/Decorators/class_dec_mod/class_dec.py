class test_class:
    def __init__(self):
        print("Init complete")

    def printInit():
        # print(dir(self)) # need to pass self to make it work
        print("Finished printInit()")


class test_decorator_class:
    def __init__(self, func):
        self.func = func


def decorator_func(func):
    print("Inside Decorator")

    def inner(*args, **kwargs):
        print("Inside inner function")
        print("Decorated the function")
        func()

    return inner
