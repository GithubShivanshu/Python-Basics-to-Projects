import pyjokes
# This program asks for the user's name and then tells them a joke using the pyjokes library.
# run command: pip install pyjokes in your terminal to install the pyjokes library before running this program.

name = input("What is your name? ")
print(f"Hello, {name}! Here is a joke for you:")
joke = pyjokes.get_joke()
print(joke)