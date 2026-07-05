# This is a simple Python program that takes user input for their name and then prints a greeting message. The input function prompts the user to enter their name, and the print function displays a personalized greeting using an f-string for formatting.
name = input("Enter your name: ")
print(f"Hello {name}, Good Afternoon!")
# -------------------//----------------------
# This program demonstrates the use of string replacement in Python. It defines a multi-line string template for a letter, which includes placeholders for the recipient's name and the date. The program then replaces these placeholders with actual values and prints the final letter.
letter  = '''Dear <|Name|>,
You are selected!
<|Date|>
Thank you,
HR Team'''
print(letter.replace("<|Name|>", "Shivanshu").replace("<|Date|>", "05 July 2026"))
# -------------------//----------------------
# This program demonstrates the use of string methods in Python. It defines a string variable 'fact' and uses the find() method to locate the index of a specific substring, and the replace() method to replace occurrences of that substring with another string. The program also illustrates that strings are immutable in Python, as the original string remains unchanged after the replace operation.
fact = "In  python, everything is  an object."
print(fact.find("  ")) # This will print the index of the first occurrence of the substring "  " in the string fact. If the substring is not found, it will return -1.
print(fact.replace("  ", " ")) # This will replace all occurrences of the substring "  " with a single space " " in the string fact and print the modified string.
print(fact.find("  ")) # This will again print the index of the first occurrence of the substring "  " in the modified string fact. This shows, Strings are immutable in Python, and the original string fact remains unchanged after the replace operation.
# -------------------//----------------------
# This program demonstrates the use of escape characters in Python strings. It defines a string variable 'letter' that includes newline (\n) and tab (\t) escape characters to format the output. The print function then displays the letter with the specified formatting, showing how escape characters can be used to control the layout of printed text.
letter = "Dear Shivanshu, \n\tIt was nice talking to you. \nThanks & Regards."
print(letter) # This will print the letter with proper formatting, including a newline and a tab character.
