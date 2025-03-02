# A class in Python is a blueprint for creating objects. It defines a set of attributes and methods that the created objects will have.

# Example of a simple class with state:

class Dog:
    # Class attribute
    species = "Canis familiaris"

    def __init__(self, name, age):
        # Instance attributes
        self.name = name
        self.age = age

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"

# Creating instances of the Dog class
dog1 = Dog("Buddy", 3)
dog2 = Dog("Lucy", 5)

# Accessing class attributes
print(f"Buddy is a {dog1.species}")
print(f"Lucy is a {dog2.species}")

# Accessing instance attributes
print(dog1.description())
print(dog2.description())

# Calling instance methods
print(dog1.speak("Woof Woof"))
print(dog2.speak("Bark Bark"))