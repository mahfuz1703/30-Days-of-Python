# Iteration and Loops in Python

# In Python, iteration refers to the process of looping through the elements of a collection (like a list or a tuple) or repeating a block of code a certain number of times. Python provides several constructs for iteration, including for loops and while loops.

# 1. For Loop
# The for loop in Python is used to iterate over a sequence (such as a list, tuple, dictionary, set, or string).

# Example:
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Output:
# apple
# banana
# cherry

# 2. While Loop
# The while loop in Python is used to repeatedly execute a block of code as long as a condition is true.

# Example:
count = 0
while count < 5:
    print(count)
    count += 1

# Output:
# 0
# 1
# 2
# 3
# 4

# 3. Nested Loops
# You can use one or more loops inside another loop. This is called nesting.

# Example:
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")

# Output:
# i: 0, j: 0
# i: 0, j: 1
# i: 1, j: 0
# i: 1, j: 1
# i: 2, j: 0
# i: 2, j: 1

# 4. Loop Control Statements
# Python provides several control statements to control the flow of loops:
# -> break: Terminates the loop statement and transfers execution to the statement immediately following the loop.

# -> continue: Causes the loop to skip the remainder of its body and immediately retest its condition prior to reiterating.
# -> pass: Does nothing; it is used when a statement is required syntactically but you do not want any command or code to execute.

# Example of break:
for num in range(10):
    if num == 5:
        break
    print(num)

# Output:
# 0
# 1
# 2
# 3
# 4

# Example of continue:
for num in range(10):
    if num % 2 == 0:
        continue
    print(num)

# Output:
# 1
# 3
# 5
# 7
# 9

# Example of pass:
for num in range(5):
    if num == 3:
        pass
    print(num)

# Output:
# 0
# 1
# 2
# 3
# 4

# 5. Iterating through a Dictionary
# You can iterate through the keys, values, or key-value pairs of a dictionary.

# Example:
person = {"name": "Alice", "age": 25, "city": "New York"}
for key, value in person.items():
    print(f"{key}: {value}")

# Output:
# name: Alice
# age: 25
# city: New York

# These are the basic concepts of iteration and loops in Python. They are powerful tools that allow you to perform repetitive tasks efficiently.