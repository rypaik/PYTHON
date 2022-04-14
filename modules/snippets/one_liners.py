
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

# one-liner version
starttime=time.time()
n,m=9999,9999
arr=[[0 for i in range(m)] for j in range(n)]
# print(arr)
print("Time taken is :",time.time()-starttime)

# one-liner with timeit_plus decorator
from ptimeit import timethis, Timer

@timethis(name="This function has taken: :")
def fibo_oneliner():
    n,m=9999,9999
    arr=[[0 for i in range(m)] for j in range(n)]
    # print(arr)
    # print("Time taken is :",time.time()-starttime)

Timer.run()
