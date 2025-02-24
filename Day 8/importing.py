from math_operations import add, subtract
import requests

# Importing - Internal & External in Python

# Internal Imports
# Internal imports refer to importing modules or functions from within the same project or package.

# Example of Internal Import
# Assuming we have a file named math_operations.py in the same directory with the following content:
# def add(a, b):
#     return a + b
# def subtract(a, b):
#     return a - b

# We can import and use these functions in another file like this:

result_add = add(5, 3)
result_subtract = subtract(5, 3)

print(f"Addition: {result_add}")
print(f"Subtraction: {result_subtract}")

# External Imports
# External imports refer to importing modules or packages that are not part of the standard library and need to be installed separately.

# Example of External Import
# Let's use the request library, which is not part of the standard library and needs to be installed using pip:
# pip install requests


response = requests.get('https://api.github.com')
print(f"Status Code: {response.status_code}")
print(f"Response Content: {response.content}")

# Note: Make sure to install the requests library before running the above code.