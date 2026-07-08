# This is a dictionary in Python. It contains key-value pairs where each key is unique and maps to a specific value. 
d = {} # This is an empty dictionary. You can add key-value pairs to it later.
marks = {
    "Shivanshu": 100,
    "Rohan": 56,
    0: "Mohan"
}
print(marks) # This will output the entire dictionary, showing the keys and their corresponding values.
# --------------//-------------------
# Methods of dictionary
# 1. keys() - This method returns a view object that displays a list of all the keys in the dictionary.
print(marks.keys()) # This will output the keys of the dictionary: dict_keys(['Shivanshu', 'Rohan', 0])
# 2. values() - This method returns a view object that displays a list of all the values in the dictionary.
print(marks.values()) # This will output the values of the dictionary: dict_values([100, 56, 'Mohan'])
# 3. items() - This method returns a view object that displays a list of the dictionary's key-value tuple pairs.
print(marks.items()) # This will output the items of the dictionary: dict_items([('Shivanshu', 100), ('Rohan', 56), (0, 'Mohan')])
# 4. get() - This method returns the value for the specified key if the key is in the dictionary. If the key is not found, it returns None (or a specified default value).
print(marks.get("Shivanshu")) # This will output the value associated with the key "Shivanshu": 100
print(marks.get("Alice")) # This will output None since the key "Alice" is not in the dictionary
print(marks.get("Alice", "Key not found")) # This will output "Key not found" since the key "Alice" is not in the dictionary.
marks.update({"Shivanshu": 99, "Ritika": 88}) # This will update the value for "Shivanshu" to 99 and add a new key-value pair for "Ritika": 88
print(marks) # This will output the updated dictionary: {'Shivanshu': 99, 'Rohan': 56, 0: 'Mohan', 'Ritika': 88}
# # 5. pop() - This method removes the specified key and returns the corresponding value. If the key is not found, it raises a KeyError.
removed_value = marks.pop("Rohan") # This will remove the key "Rohan" and return its value
print(removed_value) # This will output the value that was removed: 56
print(marks) # This will output the dictionary after removing the key "Rohan": {'Shivanshu': 99, 0: 'Mohan', 'Ritika': 88}
# 6. popitem() - This method removes and returns the last inserted key-value pair as a tuple. If the dictionary is empty, it raises a KeyError.
last_item = marks.popitem() # This will remove and return the last inserted key-value pair
print(last_item) # This will output the last inserted key-value pair that was removed: ('Ritika', 88)
print(marks) # This will output the dictionary after removing the last inserted key-value pair: {'Shivanshu': 99, 0: 'Mohan'}
# 7. clear() - This method removes all items from the dictionary, leaving it empty.
marks.clear() # This will clear all items from the dictionary
print(marks) # This will output the empty dictionary: {}
# 8. copy() - This method returns a shallow copy of the dictionary.
marks_copy = marks.copy() # This will create a shallow copy of the dictionary
print(marks_copy) # This will output the copy of the dictionary: {}
# 9. fromkeys() - This method creates a new dictionary with keys from the specified iterable and values set to the specified value (default is None).
new_dict = dict.fromkeys(["a", "b", "c"], 0) # This will create a new dictionary with keys "a", "b", and "c", all set to the value 0
print(new_dict) # This will output the new dictionary: {'a': 0, 'b': 0, 'c': 0}
# 10. setdefault() - This method returns the value of the specified key. If the key does not exist, it inserts the key with the specified value (default is None).
value = marks.setdefault("Shivanshu", 100) # This will return the value for the key "Shivanshu" if it exists, otherwise it will insert "Shivanshu" with the value 100
print(value) # This will output the value associated with the key "Shivanshu": 100
print(marks) # This will output the dictionary after setting the default value for the key "Shivanshu": {'Shivanshu': 100}
# 11. del - This statement removes the specified key from the dictionary. If the key is not found, it raises a KeyError.
del marks["Shivanshu"] # This will remove the key "Shivanshu" from the dictionary
print(marks) # This will output the dictionary after deleting the key "Shivanshu": {}
# 12. len() - This function returns the number of items (key-value pairs) in the dictionary.
print(len(marks)) # This will output the number of items in the dictionary: 0
# 13. in - This operator checks if a specified key exists in the dictionary and returns True or False.
print("Shivanshu" in marks) # This will output False since the key "Shivanshu" has been deleted from the dictionary
# 14. not in - This operator checks if a specified key does not exist in the dictionary and returns True or False.
print("Shivanshu" not in marks) # This will output True since the key "Shivanshu" has been deleted from the dictionary
# 15. clear() - This method removes all items from the dictionary, leaving it empty.
marks.clear() # This will clear all items from the dictionary
print(marks) # This will output the empty dictionary: {}
# --------------//-------------------
# This is a set in Python. It is an unordered collection of unique elements.
e = set() # This is an empty set. You can add elements to it later.
print(type(e)) # This will output the type of the variable 'e', which is <class 'set'>
s = {1,2,5,3,5,23, "shivanshu"} # This is a set with some duplicate elements. The duplicates will be removed automatically.
print(s) # This will output the set: {1, 2, 3, 23, 5, "shivanshu"}
s.add(56) # This will add the element 56 to the set
print(s) # This will output the set after adding 56: {1, 2, 3, 23, 5, "shivanshu", 56}
# --------------//-------------------
# Operations and methods on sets.
# 1. len() - This function returns the number of elements in the set.
print(len(s)) # This will output the number of elements in the set: 7
# 2. in - This operator checks if a specified element exists in the set and returns True or False.
print(56 in s) # This will output True since the element 56 is in the set
# 3. not in - This operator checks if a specified element does not exist in the set and returns True or False.
print(100 not in s) # This will output True since the element 100 is not in the set
# 4. remove() - This method removes the specified element from the set. If the element is not found, it raises a KeyError.
s.remove(56) # This will remove the element 56 from the set
print(s) # This will output the set after removing 56: {1, 2, 3, 23, 5, "shivanshu"}
# 5. discard() - This method removes the specified element from the set if it exists. If the element is not found, it does nothing (no error is raised).
s.discard(100) # This will attempt to remove the element 100 from the set
print(s) # This will output the set after discarding 100: {1, 2, 3, 23, 5, "shivanshu"}
# 6. pop() - This method removes and returns an arbitrary element from the set. If the set is empty, it raises a KeyError.
popped_element = s.pop() # This will remove and return an arbitrary element from the set
print(popped_element) # This will output the popped element
print(s) # This will output the set after popping an element: {1, 2, 3, 23, 5, "shivanshu"}
# 7. clear() - This method removes all elements from the set, leaving it empty.
s.clear() # This will clear all elements from the set
print(s) # This will output the empty set: set()
# 8. union() - This method returns a new set that contains all unique elements from both sets.
s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = s1.union(s2) # This will create a new set with all unique elements from both sets
print(s3) # This will output the union of the two sets: {1, 2, 3, 4, 5}
# 9. intersection() - This method returns a new set that contains only the elements that are common to both sets.
s4 = s1.intersection(s2) # This will create a new set with elements that are common to both sets
print(s4) # This will output the intersection of the two sets: {3}
# 10. difference() - This method returns a new set that contains the elements that are in the first set but not in the second set.
s5 = s1.difference(s2) # This will create a new set with elements that are in s1 but not in s2
print(s5) # This will output the difference of the two sets: {1, 2}
# 11. symmetric_difference() - This method returns a new set that contains the elements that are in either of the sets but not in both.
s6 = s1.symmetric_difference(s2) # This will create a new set with elements that are in either s1 or s2 but not in both
print(s6) # This will output the symmetric difference of the two sets: {1, 2, 4, 5}
# 12. issubset() - This method checks if all elements of the first set are present in the second set and returns True or False.
print(s1.issubset(s2)) # This will output False since not all elements of s1 are present in s2
# 13. issuperset() - This method checks if all elements of the second set are present in the first set and returns True or False.
print(s1.issuperset(s2)) # This will output False since not all elements of s2 are present in s1
# 14. isdisjoint() - This method checks if the two sets have no elements in common and returns True or False.
print(s1.isdisjoint(s2)) # This will output False since the two sets have the element 3 in common
# 15. copy() - This method returns a shallow copy of the set.
s7 = s1.copy() # This will create a shallow copy of the set s1
print(s7) # This will output the copied set: {1, 2, 3}
# 16. frozenset() - This function returns an immutable version of the set, which means that the elements of the frozenset cannot be changed after it is created.
fs = frozenset(s1) # This will create a frozenset from the set s1
print(fs) # This will output the frozenset: frozenset({1, 2, 3})
# 17. update() - This method adds all elements from another set (or any iterable) to the current set.
s1.update(s2) # This will add all elements from s2 to s1
print(s1) # This will output the updated set: {1, 2, 3, 4, 5}\
# 18. intersection_update() - This method updates the current set to keep only the elements that are present in both sets.
s1.intersection_update(s2) # This will update s1 to keep only the elements that are present in both s1 and s2
print(s1) # This will output the updated set: {3, 4, 5}
# 19. difference_update() - This method updates the current set to remove the elements that are present in another set.
s1.difference_update(s2) # This will update s1 to remove the elements that are present in s2