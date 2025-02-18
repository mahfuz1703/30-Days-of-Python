# Python List
# A list is a collection which is ordered and changeable. In Python, lists are written with square brackets.

# Creating a list
fruits = ["apple", "banana", "cherry"]
print(fruits)  # Output: ['apple', 'banana', 'cherry']

# Accessing elements
print(fruits[0])  # Output: apple
print(fruits[1])  # Output: banana

# Changing elements
fruits[1] = "blueberry"
print(fruits)  # Output: ['apple', 'blueberry', 'cherry']

# Looping through a list
for fruit in fruits:
    print(fruit)
# Output:
# apple
# blueberry
# cherry

# Checking if an item is in the list
if "apple" in fruits:
    print("Yes, 'apple' is in the fruits list")

# List length
print(len(fruits))  # Output: 3

# Adding elements
fruits.append("orange")
print(fruits)  # Output: ['apple', 'blueberry', 'cherry', 'orange']

# Inserting elements
fruits.insert(1, "mango")
print(fruits)  # Output: ['apple', 'mango', 'blueberry', 'cherry', 'orange']

# Removing elements
fruits.remove("mango")
print(fruits)  # Output: ['apple', 'blueberry', 'cherry', 'orange']

# Popping elements
fruits.pop()
print(fruits)  # Output: ['apple', 'blueberry', 'cherry']

# Deleting elements
del fruits[0]
print(fruits)  # Output: ['blueberry', 'cherry']

# Clearing the list
fruits.clear()
print(fruits)  # Output: []

# List comprehension
numbers = [1, 2, 3, 4, 5]
squared_numbers = [x**2 for x in numbers]
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

# Nested lists
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(nested_list[1][2])  # Output: 6