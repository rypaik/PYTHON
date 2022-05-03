
# ARRAY ONE LINERS -FOR LOOP FUNCTIONS PRODUCE A LIST
# 1. CREATE A LIST OF ZEROES
# 2. SELECTING EVEN NUMBERS IN RANGE
# 3. IF-ELSE WITH A FUNCTION

#TODO: MAKE ONE LINERS FOR DICTS


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
# from ptimeit import timethis, Timer

# @timethis(1, name="This function has taken: :")
# def fibo_oneliner():
#     n,m=9999,9999
#     arr=[[0 for i in range(m)] for j in range(n)]
#     # print(arr)
#     # print("Time taken is :",time.time()-starttime)

# Timer.run()

# one-liner with timeit_plus decorator
# from timeit_plus import tplus

#@tplus()
#def fibo_oneliner():
#    n,m=9999,9999
#    arr=[[0 for i in range(m)] for j in range(n)]
#    # print(arr)
#    # print("Time taken is :",time.time()-starttime)



###### SELECTING EVEN NUMBERS IN RANGE

# non-oneliner
import time
starttime=time.time()
arr=[]
for i in range(999999999):
    if(i%2==0):
        arr.append(i)      
print("Time taken is:", time.time()-starttime)



# one-liner version
import time
starttime=time.time()
arr=[i for i in range(m) if i%2==0]
print("Time taken is: ", time.time()-starttime)




###### ONE LINER IF ELSE WITH FUNCTION

# non-one liner
def divisibleby3(x):
    sum=0
    while(x!=0):
        sum+=x%10
        x//=10
    if(sum%3==0):
        return True
    return False
n,m=9999,9999
x,y=0,0
for i in range(99999999):
    if(divisibleby3(i)):
        x+=1

# one-liner
def divisibleby3_oneline(x):
    return True if sum(list(map(int,str(x))))%3==0 else False

arr = sum([1 for i in range (99999999) if(divisibleby3_oneline(i))])



###### MANIPULATING AN ARRAY
# non one-liner
arr_man=[]
for i in range(9999999):
    arr_man.append(i)
for i in range (len(arr_man)):
    arr_man[i]=arr_man[i]**2



# one-liner version
arr=[i for i in range(9999999)]
arr=[i**2 for i in arr]





###### PALINDROME CHECK
# non-oneliner
n=9*9999999
temp=n
rev=0
while(n>0):
    dig=n%10
    rev=rev%10+dig
    n=n//10

# oneliner
x=99999
def palindrome(x):
    return x==x[::-1]
palindrome(str(x))




###### ONE LINE IF ELSE
# <conditional-true> if conditional else <conditional-false>
x = 10 
y = 5
print("x is greater than y") if x > y else print("y is greater than x")

# multiple if elif
x = 200
print("x is less than 20") if x < 20 else print("x is equal to 200") if x == 200 else print("x is above 20")



# Assign Multiple Variables
name, age, single = ‘jc’, 35, False


# variable swap
tmp = var1
var1 = var2
var2 = tmp

var1, var2 = var2, var1

# switching elements
colors = ['red', 'green', 'blue']
colors[0], colors[1] = colors[1], colors[0]
print(colors)

####### LIST COMPREHENSIONS

# non comprehension
scores = []
for x in range (20):
    if x % 2 == 1:
       scores.append(x)
print(scores)

# List Comp
scores = [x for x in range(5)]
print(scores)


# Conditional List Comp
scores = [x for x in range(20) if x % 2 == 1]
print(scores)

# nested loops list comprehension
my_list = [(x, y) for x in [3, 4, 6] for y in [3, 4, 7] if x != y]
print(my_list)
# [(3, 4), (3, 7), (4, 3), (4, 7), (6, 3), (6, 4), (6, 7)]


# dictionary comprehension
square_dict = {num: num * num for num in range(1, 11)}
print(square_dict)


# flatten list
my_list = [[1,2], [4, 6], [8, 10]]
flattened = [i for j in my_list for i in j]
print(flattened)
# [1, 2, 4, 6, 8, 10]


# list deconstruction
x, y, *z = [1, 2, 3, 4, 5]
print(x, y, z)


# load file into list
my_list = [line.strip() for line in open('countries.txt', 'r')]
print(my_list)
