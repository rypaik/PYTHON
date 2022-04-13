""" 
    4 Fibonacci Sequence scripts
    find_fib_num(num) - finds the nth term in fibonacci
    fibo_loop(num) - prints the fibonacci series up to num
    fibo_recursive(num) - 

"""

# Fibonacci Series
# [Source](https://www.educba.com/fibonacci-series-in-python/)

# Finding nth Fib Number
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


# print(find_fib_num(100))

# GENERATORS Method
# def fibo_generator(num):
#     a, b = 0, 1
#     for i in range(0, num):
#         yield "{} :: {}".format(i+1, a)
#         a, b= b, a+b
#
# for item in fibo_generator(10):
#     print(item)


# LOOPS METHOD - Print Each Added result - add return code
def fibo_loop(num):
    u, v = 0, 1
    for i in range(0, num):
        print(u)
        u, v = v, u + v


# fibo_loop(15)

# RECURSIVE METHOD
def fibo_recursive(m):
    if m <= 1:
        return m
    else:
        return fibo_recursive(m - 1) + fibo_recursive(m - 2)


# m = int(input("Enter number of terms:"))
# print("Fibonacci sequence:")
# for i in range(m):
#     print(fibo_recursive(i),)
#     # print(f"{fibo_recursive(i)},")
