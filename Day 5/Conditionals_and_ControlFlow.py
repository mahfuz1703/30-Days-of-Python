# Python Conditionals and Control Flow

# Conditionals and control flow are used to execute different blocks of code based on certain conditions.

# 1. if statement
# The if statement is used to test a condition. If the condition is true, the block of code inside the if statement is executed.

x = 10
if x > 5:
    print("x is greater than 5")

# 2. if-else statement
# The if-else statement is used to execute one block of code if the condition is true, and another block of code if the condition is false.

y = 3
if y > 5:
    print("y is greater than 5")
else:
    print("y is not greater than 5")

# 3. if-elif-else statement
# The if-elif-else statement is used to test multiple conditions. The first condition that is true will have its block of code executed.

z = 7
if z > 10:
    print("z is greater than 10")
elif z > 5:
    print("z is greater than 5 but less than or equal to 10")
else:
    print("z is 5 or less")

# 4. Nested if statements
# You can use nested if statements to test multiple conditions within another if statement.

a = 15
if a > 10:
    if a < 20:
        print("a is between 10 and 20")

# 5. Logical operators
# You can use logical operators (and, or, not) to combine multiple conditions.

b = 8
if b > 5 and b < 10:
    print("b is between 5 and 10")

c = 12
if c < 5 or c > 10:
    print("c is either less than 5 or greater than 10")

d = False
if not d:
    print("d is False")

# 6. Ternary operator
# The ternary operator is a shorthand way of writing an if-else statement.

e = 20
result = "e is even" if e % 2 == 0 else "e is odd"
print(result)