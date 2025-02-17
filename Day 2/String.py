# Python Strings

# A string is a sequence of characters enclosed in single quotes, double quotes, or triple quotes.
single_quote_string = 'Hello, World!'
double_quote_string = "Hello, World!"
triple_quote_string = '''Hello,
World!'''

# Type of a string
print(type(single_quote_string))  # Output: <class 'str'>

# String Concatenation
# Concatenation is the process of joining two or more strings together.
string1 = "Hello"
string2 = "World"
concatenated_string = string1 + " " + string2
print(concatenated_string)  # Output: Hello World

# Type Conversion
# Converting other data types to string using the str() function.
integer_value = 100
float_value = 10.5
boolean_value = True

string_from_integer = str(integer_value)
string_from_float = str(float_value)
string_from_boolean = str(boolean_value)

print(string_from_integer)  # Output: '100'
print(string_from_float)    # Output: '10.5'
print(string_from_boolean)  # Output: 'True'

# String Methods
# Some useful string methods for day-to-day life.

# Changing case
upper_case_string = concatenated_string.upper()
lower_case_string = concatenated_string.lower()
print(upper_case_string)  # Output: HELLO WORLD
print(lower_case_string)  # Output: hello world

# Removing whitespace
whitespace_string = "   Hello, World!   "
stripped_string = whitespace_string.strip()
print(stripped_string)  # Output: Hello, World!

# Finding a substring
substring_index = concatenated_string.find("World")
print(substring_index)  # Output: 6

# Replacing a substring
replaced_string = concatenated_string.replace("World", "Python")
print(replaced_string)  # Output: Hello Python

# Splitting a string
split_string = concatenated_string.split(" ")
print(split_string)  # Output: ['Hello', 'World']

# Joining a list of strings
joined_string = " ".join(split_string)
print(joined_string)  # Output: Hello World

# String Formatting
# Using f-strings for formatting strings.
name = "Mahfuz"
age = 25
formatted_string = f"My name is {name} and I am {age} years old."
print(formatted_string)  # Output: My name is Mahfuz and I am 25 years old.