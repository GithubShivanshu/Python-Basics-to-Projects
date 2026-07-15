# Write a Python program to find the greatest of four numbers entered by the user.
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
num4 = int(input("Enter the fourth number: "))
if(num1>num2 and num1>num3 and num1>num4):
    print(f"{num1} is the greatest number.")
elif(num2>num1 and num2>num3 and num2>num4):
    print(f"{num2} is the greatest number.")
elif(num3>num1 and num3>num2 and num3>num4):
    print(f"{num3} is the greatest number.")
else:
    print(f"{num4} is the greatest number.")
# --------------------------//---------------------------
# This program checks if a student has passed or failed based on their marks in three subjects. The passing criteria are that the student must have at least 33 marks in each subject and an overall percentage of at least 40%.
a = int(input("Enter your marks in subject 1: "))
b = int(input("Enter your marks in subject 2: "))
c = int(input("Enter your marks in subject 3: "))
percent = (a+b+c)/3
if(a>=33 and b>=33 and c>=33 and percent>=40):
    print(f"Passed with {percent}%")
else:
    print("Failed.")
# --------------------------//---------------------------
# This program checks if a given message is spam or not. It uses a set of spam keywords and checks if any of those keywords are present in the user's message. If any keyword is found, it prints that the message is spam; otherwise, it prints that the message is not spam.
spam = {"Make a lot of money", "buy now", "subscribe this", "click this"}
message = input("Enter your message: ").lower()
if any(word in message for word in spam):
    print("This message is a spam.")
else:
    print("This message is not a spam.")
# --------------------------//---------------------------
# This program checks the length of the user's name. If the name contains less than 10 characters, it prints a message indicating that. Otherwise, it greets the user with their name.
name = input("Enter your name: ")
if(len(name)<10):
    print("The name contains less than 10 characters.")
else:
    print(f"Hello {name}")
# ---------------------------//---------------------------
# This program checks if the user's name is in a predefined list of friends. If the name is found, it prints a message indicating that the user is a friend of Shivanshu. Otherwise, it simply greets the user.
friends = ["nishant", "shubham", "tushar", "utkarsh", "nikhil", "aditya", "adeeb", "abhay"]
name = input("Enter your name: ").lower()
if name in friends:
    print(f"Hello {name} you are a friend of Shivanshu.")
else:
    print(f"Hello {name}.")