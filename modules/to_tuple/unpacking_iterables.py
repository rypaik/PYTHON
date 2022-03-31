# define list
my_list = [1, 2, 3]


# unpacked_list_to_tuple = (*my_list)
# throws error because unpacking only works as parameter

print(*my_list)
# print(f"The Unpacked list:{print(*my_list)}")


# Throws TypeError
# print(type(*my_list))

print(my_list)


# *********************************************** #
# upacking list for parameters to function call
# parameters count equal the list being passed in
def my_sum(a, b, c):
    print(a+b+c)


sum_list = [5, 6, 7]
my_sum(*sum_list)


# *args to make it even more flexible
def my_sum(*args):
    result = 0
    for x in args:
        result += x
    return result


list1 = [1, 2, 3]
list2 = [4, 5]
list3 = [6, 7, 8, 9]

print(my_sum(*list1, *list2, *list3))


# ****************************************** #
# EXTRACTING LIST USING *
# @FIXME:
y_list = [1, 2, 3, 4, 5, 6]

a, *b, c = my_list

print(a)
print(b) # [2,3,4,5]
print(c)


# ****************************************** #
# MERGING LISTS USING *
my_first_list = [1, 2, 3]
my_second_list = [4, 5, 6]
my_merged_list = [*my_first_list, *my_second_list]

print(my_merged_list)


# ****************************************** #
# MERGING DICTS USING *
my_first_dict = {"A": 1, "B": 2}
my_second_dict = {"C": 3, "D": 4}
my_merged_dict = {**my_first_dict, **my_second_dict}

print(my_merged_dict)

# ***************************************** #
# STRINGS TO LIST USING *
a = [*"StringsToList"]
print(a)

*a, = "Uncommon Syntax"
print(a)
