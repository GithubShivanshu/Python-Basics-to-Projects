# This demonstrates the use of conditional statements in Python. If elif else ladder is uded to check multiple conditions.
# The program checks if the user is eligible to vote based on their age. If the age is 18 or above, it prints that the user is eligible to vote. If the age is less than or equal to 0, it prints that the age is invalid. Otherwise, it prints that the user is not eligible to vote.7
age = int(input("Enter your age: "))
if(age >=18):
    print("You are eligible to vote.")
elif(age <=0):
    print("Invalid age.")
else:
    print("You are not eligible to vote.")

print("Program ended")
