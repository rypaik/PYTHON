from class_dec import test_class, decorator_func

if __name__ == "__main__":
    print("started main")
    classInstance = test_class
    print(dir(classInstance))
    classInstance.printInit()

    # callin decorator from module

    @decorator_func
    def func_to():
        print("TADAAAHH")

    func_to()
