# This code demonstrates the use of lists in Python, including indexing, slicing, and mutability.
List = ["apple", "banana", 3, 5.78, True] # A list is a collection of items that can be of different data types. In this case, the list contains strings, an integer, a float, and a boolean value.
print(List[0]) # prints "apple" because it accesses the first element of the list using index 0. It demonstrates Lists indexing.
print(List[1:4]) # prints ['banana', 3, 5.78] because it slices the list from index 1 to 3 (4 is excluded). It demonstrates Lists slicing.
List[0] = "mango" # This line modifies the first element of the list from "apple" to "mango". It demonstrates that lists are mutable, meaning their elements can be changed.
print(List) # prints ['mango', 'banana', 3, 5.78, True] because the first element of the list has been changed to "mango". It demonstrates Lists mutability.
# ---------------------//----------------------
# This code demonstrates the use of Lists methods in Python, including append(), sort(), reverse(), insert(), pop(), and remove().
List = [1,2,4,7,3,6]
List.append(5)
print(List) # prints [1, 2, 4, 7, 3, 6, 5] because the append() method adds the element 5 to the end of the list. It demonstrates how to add an element to a list in Python.
List.sort()
print(List) # prints [1, 2, 3, 4, 5, 6, 7] because the sort() method sorts the elements of the list in ascending order. It demonstrates how to sort a list in Python.
List.reverse()
print(List) # prints [7, 6, 5, 4, 3, 2, 1] because the reverse() method reverses the order of the elements in the list. It demonstrates how to reverse a list in Python.
List.insert(2, 8)
print(List) # prints [7, 6, 8, 5, 4, 3, 2, 1] because the insert() method adds the element 8 at index 2 of the list. It demonstrates how to insert an element at a specific position in a list in Python.
print(List.pop(2)) # prints 8 because the pop() method removes and returns the element at index 2 of the list. It demonstrates how to remove an element from a list in Python.
print(List) # prints [7, 6, 5, 4, 3, 2, 1] because the element at index 2 (which was 8) has been removed from the list. It demonstrates how to remove an element from a list in Python.
List.remove(5)
print(List) # prints [7, 6, 4, 3, 2, 1] because the remove() method removes the first occurrence of the element 5 from the list. It demonstrates how to remove a specific element from a list in Python.
# ---------------------//----------------------
# This code demonstrates the use of tuples in Python, including indexing, slicing, and immutability.
Tuple = (1,) # A tuple is a collection of items that can be of different data types. In this case, the tuple contains a single integer value. The comma after the integer is necessary to indicate that it is a tuple with one element.
print(Tuple) # prints (1,) because it displays the tuple containing the single integer value. It demonstrates how to create and print a tuple with one element in Python.
Tuple = ("apple", "banana", 3, 5.78, True) # A tuple is a collection of items that can be of different data types. In this case, the tuple contains strings, an integer, a float, and a boolean value.
print(Tuple)
print(type(Tuple[4])) # prints <class 'bool'> because it checks the data type of the element at index 4 of the tuple, which is a boolean value (True). It demonstrates how to check the data type of an element in a tuple in Python.
print(Tuple[0]) # prints "apple" because it accesses the first element of the tuple using index 0. It demonstrates tuples indexing.
print(Tuple[1:4]) # prints ('banana', 3, 5.78) because it slices the tuple from index 1 to 3 (4 is excluded). It demonstrates tuples slicing.
Tuple[0] = "mango" # This line will raise a TypeError because tuples are immutable, meaning their elements cannot be changed after they are created. It demonstrates tuples immutability.
# ----------------------//----------------------
# This code demonstrates the use of tuples methods in Python, including count() and index().
Tuple = (1, 2, 3, 4, 5, 2, 3, 2) # A tuple is a collection of items that can be of different data types. In this case, the tuple contains integers.
print(Tuple.count(3)) # prints 2 because the count() method returns the number of occurrences of the specified element (3) in the tuple. It demonstrates how to count occurrences of an element in a tuple in Python.
print(Tuple.index(4)) # prints 3 because the index() method returns the index of the first occurrence of the specified element (4) in the tuple. It demonstrates how to find the index of an element in a tuple in Python.
# ----------------------//----------------------
# This code demonstrates the use of Operators in Python, including arithmetic, comparison, logical, membership, concatenation, Repetition, length, unpacking operators.
Tuple = (1,2,3,4,5)
print(Tuple + (6,7,8)) # prints (1, 2, 3, 4, 5, 6, 7, 8) because the + operator concatenates two tuples together. It demonstrates how to concatenate tuples in Python.
print(Tuple * 2) # prints (1, 2, 3, 4, 5, 1, 2, 3, 4, 5) because the * operator repeats the tuple a specified number of times. It demonstrates how to repeat a tuple in Python.
print(len(Tuple)) # prints 5 because the len() function returns the number of elements in the tuple. It demonstrates how to get the length of a tuple in Python.
print(3 in Tuple) # prints True because the in operator checks if the specified element (3) is present in the tuple. It demonstrates how to check for membership in a tuple in Python.
print(10 not in Tuple) # prints True because the not in operator checks if the specified element (10) is not present in the tuple. It demonstrates how to check for non-membership in a tuple in Python.
print(Tuple[1] > Tuple[0]) # prints True because the > operator compares the elements at index 1 and index 0 of the tuple. It demonstrates how to use comparison operators with tuples in Python.
print(Tuple[1] == Tuple[2]) # prints False because the == operator checks if the elements at index 1 and index 2 of the tuple are equal. It demonstrates how to use comparison operators with tuples in Python.
print(Tuple[0] and Tuple[1]) # prints 2 because the and operator returns the second operand if both operands are true. It demonstrates how to use logical operators with tuples in Python.
print(Tuple[0] or Tuple[1]) # prints 1 because the or operator returns the first operand if it is true. It demonstrates how to use logical operators with tuples in Python.
print(not Tuple[0]) # prints False because the not operator negates the truth value of the operand. It demonstrates how to use logical operators with tuples in Python.
print(Tuple[0] + Tuple[1]) # prints 3 because the + operator adds the elements at index 0 and index 1 of the tuple. It demonstrates how to use arithmetic operators with tuples in Python.
print(Tuple[0] - Tuple[1]) # prints -1 because the - operator subtracts the element at index 1 from the element at index 0 of the tuple. It demonstrates how to use arithmetic operators with tuples in Python.
print(Tuple[0] * Tuple[1]) # prints 2 because the * operator multiplies the elements at index 0 and index 1 of the tuple. It demonstrates how to use arithmetic operators with tuples in Python.
print(Tuple[0] / Tuple[1]) # prints 0.5 because the / operator divides the element at index 0 by the element at index 1 of the tuple. It demonstrates how to use arithmetic operators with tuples in Python.
a,b, c, d, e = Tuple # This line demonstrates tuple unpacking, where the elements of the tuple are assigned to individual variables a, b, c, d, and e. It allows for easy access to the elements of the tuple.
print(a, b, c, d, e) # prints 1 2 3 4 5 because the variables a, b, c, d, and e hold the values of the elements in the tuple. It demonstrates how to access the unpacked values from a tuple in Python.