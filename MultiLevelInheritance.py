# Multi Level Inheritance

# Grand Parent Class
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")


# Parent Class
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def bark(self):
        print(f"{self.name} is barking.")


# Child Class
class Labrador(Dog):
    def __init__(self, name, breed, color):
        super().__init__(name, breed)
        self.color = color

    def play_fetch(self):
        print(f"{self.name} is playing fetch.")


my_dog = Labrador("Buddy", "Labrador", "Yellow")

my_dog.eat() # Output: Buddy is eating.
my_dog.sleep() # Output: Buddy is sleeping.
my_dog.bark() # Output: Buddy is barking.
my_dog.play_fetch() # Output: Buddy is playing fetch.
