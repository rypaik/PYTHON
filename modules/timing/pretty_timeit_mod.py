from ptimeit import timethis, Timer

# although this is a decorator, your original function will not be modified.
@timethis() 
def function_to_be_timed():
    lst = [i for i in range(10)]

Timer.run() # Call this at the end of the file.
