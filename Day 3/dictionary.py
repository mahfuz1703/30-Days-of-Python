# Python Dictionary

# A dictionary in Python is an unordered collection of items. 
# Each item is a key-value pair. Dictionaries are optimized to retrieve values when the key is known.

# Creating a dictionary
my_dict = {
    'name': 'John',
    'age': 25,
    'city': 'New York'
}

# Accessing values
print(my_dict['name'])  # Output: John

# Adding a new key-value pair
my_dict['email'] = 'john@example.com'

# Updating an existing key-value pair
my_dict['age'] = 26

# Removing a key-value pair
del my_dict['city']

# Iterating through a dictionary
for key, value in my_dict.items():
    print(f'{key}: {value}')

# Checking if a key exists in the dictionary
if 'name' in my_dict:
    print('Name is present in the dictionary')

# Dictionary methods
keys = my_dict.keys()  # Returns a view object of all keys
values = my_dict.values()  # Returns a view object of all values
items = my_dict.items()  # Returns a view object of all key-value pairs

# Example of nested dictionary
nested_dict = {
    'person1': {'name': 'Alice', 'age': 30},
    'person2': {'name': 'Bob', 'age': 25}
}

# Accessing values in a nested dictionary
print(nested_dict['person1']['name'])  # Output: Alice

# Dictionary comprehension
squares = {x: x*x for x in range(6)}
print(squares)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}