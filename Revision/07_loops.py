# Loops in Python are used to execute a block of code repeatedly as long as a certain condition is met. There are two main types of loops in Python: `for` loops and `while` loops.
# 1. while loop: A while loop continues to execute a block of code as long as a specified condition is true.
# Example:
l = [1, "shivanshu", 2, "shubham", 3, "nikhil", 4, "adeeb", 5, "utkarsh", 6, "aditya", 7, "tushar", 8, "abhay", 9, "nishant"]
i =0
while(i<len(l)):
    print(l[i])
    i+=1

# 2. for loop: A for loop is used to iterate over a sequence (like a list, tuple, or string) and execute a block of code for each item in the sequence. Example:
word = "shivanshu"
for i in word:
    print(i)

# 3. for loop with else: In Python, a for loop can also have an optional else clause. The else block will be executed after the for loop completes its iteration over the sequence, unless the loop is terminated by a break statement. Example:
l = [1, "shivanshu", 2, "shubham", 3, "nikhil", 4, "adeeb", 5, "utkarsh", 6, "aditya", 7, "tushar", 8, "abhay", 9, "nishant"]
for ele in l:
    print(ele)
else:
    print("Loop has completed its iteration over the list.")
# ---------------------------------------//----------------------------------------

# break and continue statements: The break statement is used to exit a loop prematurely, while the continue statement is used to skip the current iteration and move on to the next one. Example:
# break statement:
for i in range(20):
    if(i == 11):
        break
    print(i)
# continue statement:
for i in range(20):
    if(i == 10):
        continue
    print(i)
# ----------------------------------------//----------------------------------------

# Pass statement: The pass statement is a null operation; it does nothing when executed. It is often used as a placeholder in loops, functions, or classes where code will be added later. Example:
for i in range(10):
    pass  # This loop does nothing and serves as a placeholder for future code.
i = 10
while i>0:
    print(i)
    i-=1