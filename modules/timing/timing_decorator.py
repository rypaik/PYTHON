from functools import wraps
from time import time

# def timing(f):
#     @wraps(f)
#     def wrap(*args, **kw):
#         ts = time()
#         result = f(*args, **kw)
#         te = time()
#         print(f"func:{f.__name__} args:{args},{kw} took{te-ts:2.4f} secs")
#  
#         # print 'func:%r args:[%r, %r] took: %2.4f sec' % \
#             # (f.__name__, args, kw, te-ts)
#         return result
#     return wrap


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
    
# @timing
# def f(a):
#     for i in range(a):
#         i = 0
#     return -1
# 
# 

# pretty_timeit decorator
from ptimeit import timethis, Timer

@timethis([10])
def find_fib_num(m):
     u = 0
     v = 1
     if m < 0:
         print("Incorrect input entered")
     elif m == 0:
         return u
     elif m == 1:
         return v
     else:
         for i in range(2, m):
             c = u + v
             u = v
             v = c
         return v

Timer.run()
