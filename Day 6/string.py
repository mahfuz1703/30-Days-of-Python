# Python String Formatting and F-Strings

# 1. Using the % operator
name = "Alice"
age = 25
formatted_string = "Hello, %s. You are %d years old." % (name, age)
print(formatted_string)  # Output: Hello, Alice. You are 25 years old.

# 2. Using the str.format() method
formatted_string = "Hello, {}. You are {} years old.".format(name, age)
print(formatted_string)  # Output: Hello, Alice. You are 25 years old.

# 3. Using f-strings (formatted string literals)
formatted_string = f"Hello, {name}. You are {age} years old."
print(formatted_string)  # Output: Hello, Alice. You are 25 years old.

# F-strings can also include expressions
a = 5
b = 10
formatted_string = f"The sum of {a} and {b} is {a + b}."
print(formatted_string)  # Output: The sum of 5 and 10 is 15.

# F-strings support formatting options
pi = 3.141592653589793
formatted_string = f"Pi to three decimal places is {pi:.3f}."
print(formatted_string)  # Output: Pi to three decimal places is 3.142.

# F-strings can also call functions
def greet(name):
    return f"Hello, {name}!"

formatted_string = f"{greet('Alice')}"
print(formatted_string)  # Output: Hello, Alice!