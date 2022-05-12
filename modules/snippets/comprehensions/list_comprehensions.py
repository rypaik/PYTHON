# https://medium.com/cluj-school-of-ai/python-primer-list-comprehensions-f0abd2ca528a


initial_list = [2, 7, 27, 28, 44, 49, 63, 64, 84, 100]


# flat list comprehension
new_list = [nr for n in intial_list]
print(new_list)

square_list = [nr**2 fro nr in initial_list]
print(square_list)



# list comprehension with if clause
if_list = [nr**2 for nr in initial_list if nr *2 == 0]



# list comprehensions using mutliple variables
coord_list = [(x,y) for x in range(4) for y in range(4)]
print(coord_list)
# [(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2), (2, 3), (3, 0), (3, 1), (3, 2), (3, 3)]
