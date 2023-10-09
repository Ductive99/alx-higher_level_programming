# 0x0A. Python - Inheritance

Inheritance is a fundamental concept in object-oriented programming (OOP), and Python supports OOP through its class and inheritance mechanisms. Inheritance allows you to create a new class that is a modified version of an existing class. The existing class is often referred to as the "base class" or "parent class," and the new class is called the "derived class" or "subclass." The derived class inherits attributes and behaviors (i.e., attributes and methods) from the base class, allowing you to reuse and extend code.

```Python
# Base class (or parent class)
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

# Derived class (or subclass)
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# Creating instances of the derived classes
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Calling the speak method on instances
print(dog.speak())  # Output: "Buddy says Woof!"
print(cat.speak())  # Output: "Whiskers says Meow!"
```
