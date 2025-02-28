import os

fname = "hello.txt"

# create a file
# myFile = open(fname, "w")
# myFile.write("Hello, World!!")
# myFile.close()

# with open(fname, "w") as myFile:
#     myFile.write("Hello, World!!")

# read a file
# with open(fname, "r") as file:
#     print(file.read())


# read file from another folder
# email_text = "templates/email.txt"
email_text = os.path.join("templates", "email.txt")

content = ""
with open(email_text, "r") as file:
    content = file.read()

print(content.format(name = "Mahfuz"))
