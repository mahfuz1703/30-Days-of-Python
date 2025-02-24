from hello import greeting
import hello as hi
import math

# Python Functions and Modules

# Functions
# A function is a block of code which only runs when it is called. 
# You can pass data, known as parameters, into a function. 
# A function can return data as a result.

# Defining a function
def my_function():
    print("Hello from a function")

# Calling a function
my_function()

# Function with parameters
def greet(name):
    print(f"Hello, {name}")

greet("Alice")

# Function with return value
def add(a, b):
    return a + b

result = add(3, 4)
print(result)

# Modules
# A module is a file containing Python definitions and statements. 
# The file name is the module name with the suffix .py added. 
# Modules can define functions, classes, and variables.

# Using a module
# To use a module, we use the import statement.

hi.greeting("Alice")

# You can also import specific functions from a module

greeting("Bob")

# You can give a module an alias

hi.greeting("Charlie")

# Built-in Modules
# Python has a number of built-in modules, such as math, datetime, etc.

print(math.sqrt(16))