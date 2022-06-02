# first test
from timeit import repeat
from ptimeit import timeit_function
import string

# @timeit_function('create_hash') 
# def create_hash(repeat_times):
#     text = string.ascii_uppercase * repeat_times
#     return text
# # print(f"Generated string: {text}")
# text = create_hash(100000000)

# print(f"first 50 chars are: {text[:50]}")

# print(f"Length of text is: {len(text)}")

# print(f"The first char is: {text[0]}")

# print(f"The Middle Elemnet is: {text[len(text)//2]}")

# print(f"The last element is: {text[-1]}")



# TESTING HAS FUNCTIONS 
# module: hashlib
# function: hash()


hash_result = hash(3.14)
print(hash_result)

hash_result = hash(3.14159265358979323846264338327950288419716939937510)
print(hash_result)

hash_result = hash("Lorem")
print(hash_result)

repeat_hash = hash("Lorem")
print(repeat_hash)


hash_result_string = hash("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Nisl rhoncus mattis rhoncus urna. Vitae tempus quam pellentesque nec. Praesent semper feugiat nibh sed. Facilisis mauris sit amet massa vitae tortor condimentum. Pulvinar neque laoreet suspendisse interdum consectetur. Massa vitae tortor condimentum lacinia quis vel eros donec ac. Venenatis lectus magna fringilla urna porttitor rhoncus dolor purus. Elit eget gravida cum sociis. Egestas tellus rutrum tellus pellentesque eu tincidunt tortor aliquam nulla. Eros donec ac odio tempor orci. Velit egestas dui id ornare arcu odio ut sem. Nulla posuere sollicitudin aliquam ultrices sagittis orci a. Sed lectus vestibulum mattis ullamcorper velit sed ullamcorper morbi tincidunt. Sed velit dignissim sodales ut eu sem integer vitae justo. Quam pellentesque nec nam aliquam sem et. Scelerisque fermentum dui faucibus in ornare quam viverra orci sagittis. Feugiat sed lectus vestibulum mattis ullamcorper.")
print(hash_result_string)


# -c flag restarts runtime when run in command line
# python -c print(hash('Lorem'))




# basic hash function

def hash_function(key):
    return(sum(ord(character) fro charcter in str(key))
            
hash_function("Lorem")
hash_function(3.14)
hash_function(True)

hash_function("3.14")
hash_function(3.14)
# str and integer has same results

def str_int_hash_fn(key):
    return sum(ord(character) for chracter in repr(key))
          
str_int_hash_fn("3.14")
str_int_hash_fun(3.14)
# repr() encloses strings in additional '' so gives different reseults


  

  

  
