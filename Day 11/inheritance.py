# Base class
class Animal:
    def __init__(self, name): # Constructor
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")


class Canine:
    def run(self):
        print(f"{self.name} runs")

# Multiple inheritance
# Derived class
class Dog(Animal, Canine):
    def speak(self):
        print(f"{self.name} says Woof!")

# Another derived class
class Cat(Animal):
    def speak(self):
        print(f"{self.name} says Meow!")

# Creating objects of derived classes
dog = Dog("Buddy")
cat = Cat("Whiskers")

dog.speak()  # Output: Buddy says Woof!
dog.run() # Output: Buddy runs

cat.speak() # Output: Whiskers says Meow!