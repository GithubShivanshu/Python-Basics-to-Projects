# name = "shivanshu"
# shortname = name[4:9] # Slicing is used to extract a portion of a string in python. The syntax for slicing is string[start:end], where start is the index of the first character to include, and end is the index of the first character to exclude. In this case, we are extracting characters from index 4 to 8 (9 is excluded) from the string "shivanshu", which gives us "anshu".
# print(shortname) # prints "anshu"

# name = "shivanshu"
# print(name[-4:-1]) # prints "nsh" because negative indexing starts from the end of the string, where -1 is the last character, -2 is the second last character, and so on. In this case, we are extracting characters from index -4 to -2 (excluding -1) from the string "shivanshu", which gives us "nsh".

# name = "shivanshu"
# print(name[0:]) # prints "shivanshu" because we are slicing the string from index 0 to the end of the string. In this case, we are extracting all characters from index 0 to the end of the string "shivanshu", which gives us "shivanshu".
# print(name[0:9]) # prints "shivanshu" because we are slicing the string from index 0 to 8 (9 is excluded). In this case, we are extracting all characters from index 0 to 8 from the string "shivanshu", which gives us "shivanshu".

# word = 'amazing'
# print(word[1:6:2]) # prints "mzn" because we are slicing the string from index 1 to 5 (6 is excluded) with a step of 2. In this case, we are extracting characters from index 1 to 5 with a step of 2 from the string "amazing", which gives us "mzn".

# ----------- String functions in Python are built-in methods that allow you to manipulate and perform operations on strings. Some common string functions include:
# len(): Returns the length of a string.
# lower(): Converts all characters in a string to lowercase.
# upper(): Converts all characters in a string to uppercase.
# strip(): Removes leading and trailing whitespace from a string.
# replace(): Replaces a specified substring with another substring in a string.
# endswith(): Checks if a string ends with a specified suffix.
# startswith(): Checks if a string starts with a specified prefix.
# capitalize(): Capitalizes the first character of a string.
# title(): Capitalizes the first character of each word in a string.
# split(): Splits a string into a list of substrings based on a specified delimiter.
# join(): Joins a list of strings into a single string using a specified delimiter.
# find(): Returns the index of the first occurrence of a specified substring in a string.
# index(): Returns the index of the first occurrence of a specified substring in a string (raises an error if the substring is not found).
# isdigit(): Checks if all characters in a string are digits.
# isalpha(): Checks if all characters in a string are alphabetic.
# isalnum(): Checks if all characters in a string are alphanumeric (letters and numbers).
# isspace(): Checks if all characters in a string are whitespace.
# count(): Returns the number of occurrences of a specified substring in a string.
# format(): Formats a string by replacing placeholders with specified values.

# name = "shivanshu pandey"
# print(len(name)) # prints 16 because the length of the string "shivanshu pandey" is 15 characters.
# print(name.endswith("dey")) # prints True because the string "shivanshu pandey" ends with the substring "dey".
# print(name.startswith("shiv")) # prints True because the string "shivanshu pandey" starts with the substring "shiv".
# print(name.capitalize()) # prints "Shivanshu pandey" because the capitalize() function capitalizes the first character of the string and converts the rest of the characters to lowercase.
# print(name.upper()) # prints "SHIVANSHU PANDEY" because the upper() function converts all characters in the string to uppercase.
# print(name.title()) # prints "Shivanshu Pandey" because the title() function capitalizes the first character of each word in the string.
# print(name.strip()) # prints "shivanshu pandey" because the strip() function removes leading and trailing whitespace from the string. In this case, there is no leading or trailing whitespace, so the original string is returned.
# print(name.removeprefix("shiv")) # prints "anshu pandey" because the removeprefix() function removes the specified prefix "shiv" from the string. If the string does not start with the specified prefix, the original string is returned.
# print(name.find("an")) # prints 4 because the find() function returns the index of the first occurrence of the specified substring "an" in the string. In this case, the first occurrence of "an" occurs at index 4.
# print(name.index("hn")) # gives an error because the index() function returns the index of the first occurrence of the specified substring "hn" in the string. In this case, the substring "hn" does not exist in the string "shivanshu pandey", so it raises a ValueError.
# print(name.replace("shivanshu", "shivansh")) # prints "shivansh pandey" because the replace() function replaces all occurrences of the specified substring "shivanshu" with the new substring "shivansh" in the string. In this case, the substring "shivanshu" is replaced with "shivansh", resulting in the new string "shivansh pandey".

# -------- Escape sequences characters in Python are special characters that are used to represent certain characters or actions within a string. They are preceded by a backslash (\) and have specific meanings. Some common escape sequences include:
# \n: Represents a new line.
# \t: Represents a tab.
# \\: Represents a backslash.
# \': Represents a single quote.
# \": Represents a double quote.

a = "Shivanshu is a good boy.\nHe is a \"hardworking\" \tstudent."
print(a) # prints "Shivanshu is a good boy.
# He is a "hardworking" 	student." because the escape sequence \n creates a new line, the escape sequence \" allows the double quotes to be included in the string, and the escape sequence \t creates a tab space before the word "student".
