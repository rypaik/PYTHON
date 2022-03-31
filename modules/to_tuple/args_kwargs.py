# without args
def my_sum(my_integers):
    result = 0
    for x in my_integers:
        result += x
    return result

list_of_integers = [1, 2, 3]
print(my_sum(list_of_integers))


# sum with args - Don't need to define the list as a variable to pass in
def args_sum(*args):
    result = 0
    # Iterating over the Python args tuple
    for x in args:
        result += x
    return result

print(args_sum(1, 2, 3))


# sum args as new name
def named_arg_sum(*integers):
    result = 0
    for x in integers:
        result += x
    return result
            
print(named_arg_sum(1, 2, 3))


# ********************************************* #
# CHANGING LIST TO TUPLE
# without args - no typecasting to tuple
my_list = [1, 2, 3]
my_list[0] = 9
print(my_list)


# my_tuple = (1, 2, 3)
# throws error - cannot assign to tuple
# my_tuple[0] = 9
# print(my_tuple)



def change_to_tuple(*args):
    print(dir(*args))
    new_tuple = tuple(*args)
#    for x in args:
 #       new_tuple += x
    return new_tuple


list_tuple = [1, 2, 3, 4]

print(change_to_tuple(list_of_integers))

tupled = change_to_tuple(list_tuple)



#  ************************************************ #
# KWARGS
# kwargs to conatenate dictionaires
def concat_dicts(**kwargs) -> dict:
    result=""
    for arg in kwargs.values():
        result += arg
    return result

print(concat_dicts(a="Key", b="Values", c="Can", d="Be", e="Great"))
