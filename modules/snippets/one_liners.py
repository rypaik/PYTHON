
# ARRAY ONE LINERS- FUNCTION IN A LIST TO PRODUCE A LIST
# 1. CREATE A LIST OF ZEROES



# Array of Zeroes - timed
import time
starttime=time.time()
n,m=9999,9999
arr=[]
for i in range(n):
    arr1=[]
    for j in range(m):
        arr1.append(0)
    arr.append(arr1)
print("Time taken is :",time.time()-starttime)
print(type(arr))
# one-liner List of zeroes
# for loop within a for loop
starttime=time.time()
n,m=9999,9999
arr=[[0 for i in range(m)] for j in range(n)]
# print(arr)
print("Time taken is :",time.time()-starttime)


# Pretty Time-It Decorator - Fibonacci
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
         print(v)
Timer.run()



# one-liner with timeit_plus decorator
from ptimeit import timethis, Timer

# @timethis(1, name="This function has taken: :")
# def fibo_oneliner():
#     n,m=9999,9999
#     arr=[[0 for i in range(m)] for j in range(n)]
#     # print(arr)
#     # print("Time taken is :",time.time()-starttime)

# Timer.run()

# one-liner with timeit_plus decorator
from timeit_plus import tplus

@tplus()
def fibo_oneliner():
    n,m=9999,9999
    arr=[[0 for i in range(m)] for j in range(n)]
    # print(arr)
    # print("Time taken is :",time.time()-starttime)

# SELECTING EVEN NUMBERS IN RANGE

# timed non-one liner

