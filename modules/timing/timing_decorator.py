from functools import wraps
from time import time

def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        print(f"func:{f.__name__} args:{args},{kw} took{te-ts:2.4f} secs")

        # print 'func:%r args:[%r, %r] took: %2.4f sec' % \
            # (f.__name__, args, kw, te-ts)
        return result
    return wrap


# call by using decorator
# @timing
# def f(a):
#    i = 0
#    for i in range(a):
#        i = i + 1 
#        time.sleep(2)
#    return(i)
# func_output =f(10000)
# print(func_output)
    
@timing
def f(a):
    for i in range(a):
        i = 0
    return -1
