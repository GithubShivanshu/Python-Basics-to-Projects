# 1. This problem is about creating a simple dictionary in Python that stores the meanings of some words. The user can input a word, and the program will return its meaning if it exists in the dictionary. 
words = {
    "rogue": "a dishonest",
    "facade": "an outward appearance that is maintained to conceal a less pleasant or creditable reality",
    "obscure": "not discovered or known about; uncertain",
    "coerce": "persuade (an unwilling person) to do something by using force or threats"
}
word = input("Enter the word you want to know the meaning of: ").lower()
if word in words:
    print(f"The meaning of '{word}' is: '{words[word]}'")
else:
    print(f"Sorry, the word '{word}' is not in the dictionary.")
# -------------------------//---------------------------
# 2. This problem is about creating a set in Python. A set is an unordered collection of unique elements. The user can input a number of elements, and the program will add them to the set. If the user tries to add a duplicate element, it will not be added again.
s = set()
count = int(input("Enter the count of numbers you want to add to a set: "))
for i in range(count):
    element = int(input(f"Enter the element {i+1}: "))
    s.add(element) # This will add the element to the set. If the element already exists, it will not be added again.
print(f"This is the set of numbers you have created: {s}")
# -------------------------//---------------------------
# 3. This problem is about creating a set in Python and demonstrating how duplicate elements are handled. The user can add elements to the set, and the program will show that duplicate elements are not added.
s = set() # This is an empty set. You can add elements to it later.
s.add(10)
s.add(10.0) # This will not add a new element because 10 and 10.0 are considered equal in Python.
s.add("10") # This will add a new element because "10" is a string
print(s, len(s)) # This will output the set and its length. The length will be 2 because 10 and 10.0 are considered equal, so only one of them is stored in the set.
# ---------------------------//---------------------------
# 4. This problem is about creating a dictionary in Python that stores the names of 4 students and their favourite subjects. The user can input the names and subjects, and the program will store them in a dictionary. If a name already exists in the dictionary, it will update the subject for that name.
d = {} # This is an empty dictionary. You can add key-value pairs to it later.
for i in range(4):
    name = input("Enter your name: ")
    subject = input(f"Hi {name}, Enter your favourite subject: ")
    d.update({name: subject}) # This will add the name and subject as a key-value pair to the dictionary. If the name already exists in the dictionary, it will update the subject for that name.
print(d) # This will output the dictionary with the names and their favourite subjects.