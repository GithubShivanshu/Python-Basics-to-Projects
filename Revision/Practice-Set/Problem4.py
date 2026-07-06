# This program allows the user to input a list of fruits and then displays the list.
fruits = []
items = int(input("Enter the number of fruits you want to add: "))
for i in range(items):
    fruit = input("Enter the fruit name: ")
    fruits.append(fruit)
print("The list of fruits you entered is: ", fruits)
# ----------------//-----------------------
# This program allows the user to input a list of student marks and then displays the sorted list.
marks = []
items = int(input("Enter the number of students: "))
for i in range(items):
    mark = int(input("Enter the marks of each student: "))
    marks.append(mark)
marks.sort()
print("The list of marks you entered is: ", marks)
# ----------------//-----------------------
# This program demonstrates the use of list methods and functions to perform operations on a list of numbers.
List = [2,5,6,3,3]
print(sum(List)) # This program calculates the sum of the elements in the list `List`. The `sum()` function takes an iterable (in this case, the list) and returns the total of its elements.
print(max(List)) # This program finds the maximum value in the list `List`. The `max()` function returns the largest item in an iterable or the largest of two or more arguments.
print(List.count(3)) # This program counts the occurrences of the number 3 in the list `List`. The `count()` method returns the number of times a specified value appears in the list.
