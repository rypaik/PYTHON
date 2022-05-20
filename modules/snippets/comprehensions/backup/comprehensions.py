
# Create a list to be used in comprehensions
numbers = [1, 2, 3, -3, -2, -1]

# Create a new list of these numbers’ squares
mylist = [x*x for x in numbers]
[1, 4, 9, 9, 4, 1]

# Create a new dictionary of these numbers’ exponentiation
mydict = {x: pow(10, x) for x in numbers}
# output {1: 10, 2: 100, 3: 1000, -3: 0.001, -2: 0.01, -1: 0.1}

# Create a set of these numbers’ absolutes

myset = {abs(x) for x in numbers}
# output {1, 2, 3}
print(type(myset))




# TODO: search generators from comprehensions
#() comprehension creates a generator - not a tuple
my_tuple = (abs(x) for x in numbers)
print(type(my_tuple))

for value in my_tuple:
    print(value)
