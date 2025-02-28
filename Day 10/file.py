fname = "hello.txt"

# create a file
# myFile = open(fname, "w")
# myFile.write("Hello, World!!")
# myFile.close()

# with open(fname, "w") as myFile:
#     myFile.write("Hello, World!!")

# read a file
with open(fname, "r") as file:
    print(file.read())
