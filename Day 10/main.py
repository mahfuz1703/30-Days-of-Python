"""
The open() function is used to open a file. It takes two arguments: the file name and the mode in which the file should be opened. The mode can be:

-> 'r': Read (default mode)
-> 'w': Write (creates a new file or truncates an existing file)
-> 'a': Append (adds content to the end of the file)
-> 'b': Binary mode
-> 't': Text mode (default mode)
-> 'x': Create (creates a new file and fails if the file already exists)

"""

# Creating and writing to a file
with open('example.txt', 'w') as file:
    file.write('Hello, World!\n')
    file.write('This is a new file.\n')


# Reading from a file
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)


# Appending to a file
with open('example.txt', 'a') as file:
    file.write('Appending a new line.\n')



# Reading a file line by line
with open('example.txt', 'r') as file:
    for line in file:
        print(line, end='')



# Writing to a binary file
with open('example.bin', 'wb') as file:
    file.write(b'\x00\x01\x02\x03')

# Reading from a binary file
with open('example.bin', 'rb') as file:
    content = file.read()
    print(content)



file = open('example.txt', 'r')
content = file.read()
file.close()