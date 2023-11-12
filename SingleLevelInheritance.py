# Single Level Inheritance

# Defining the superclass (or parent class)
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")


# Defining the subclass (or child class)
# The subclass inherits from the superclass using the '()' notation
class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking.")


# Creating an object of the subclass
my_dog = Dog("Buddy", 3)

# Accessing the properties and methods of the subclass
print(my_dog.name) # Output: Buddy
print(my_dog.age)   # Output: 3
my_dog.eat()        # Output: Buddy is eating.
my_dog.sleep()      # Output: Buddy is sleeping.
my_dog.bark()       # Output: Buddy is barking.
