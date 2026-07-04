# Program to list the contents of a specified directory using os module in Python.
import os

# Specify the directory path you want to list the contents of.
directory_path = '/'

# List the contents of the specified directory using os.listdir() method.
contents = os.listdir(directory_path)

# Print the contents of the specified directory.
for item in contents:
    print(item)