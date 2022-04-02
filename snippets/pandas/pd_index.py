
# USING For Loop to get index

# Method-1
 
# Import pandas
import pandas as pd
 
# Create a Python dictionary
data = {"Name": ['Sanjay', 'Shreya', 'Raju', 'Gopal', 'Ravi'],
        "Roll": [101, 102, 103, 104, 105]}
 
# Create a DataFrame object from above dictionary
df = pd.DataFrame(data, index = [1, 2, 3, 4, 5])
print("This is DataFrame:\n")
print(df)
 
# Get the index/rows of the above DataFrame 
# Using for loop iteration
print("\nThis is index of DataFrame:\n")
for idx in df.index:
    print(idx, end = ' ')


# This is DataFrame:
#  
#      Name  Roll
# 1  Sanjay   101
# 2  Shreya   102
# 3    Raju   103
# 4   Gopal   104
# 5    Ravi   105
#  
# This is index of DataFrame:
#  
# 1 2 3 4 5
