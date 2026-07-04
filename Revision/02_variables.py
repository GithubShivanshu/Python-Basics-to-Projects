# a = '31.2'
# print(type(a))
# b = float(a) # type casting string to float
# print(type(b))

# taking user input using input() function
# a = input("Enter number 1: ") # 2
# b = input("Enter number 2: ") # 4
# print("The sum of numbers is: ", a+b) # this will concatenate the two strings instead of adding them as numbers. Prints 24

# a = int(input("Enter number 1: ")) # 2
# b = int(input("Enter number 2: ")) # 4
# print("The sum of numbers is: ", a+b) # prints 6

# Integer caching in Python, a mechanism that optimizes memory usage and performance by reusing immutable integer objects for small integer values. In Python, integers are immutable, meaning their value cannot be changed after they are created. To improve efficiency, Python caches small integer objects (typically in the range of -5 to 256) so that when you create an integer within this range, it reuses the existing object instead of creating a new one.

# printing square of a number
# a = int(input("Enter a number: "))
# print("The square of the number is: ", a**2)