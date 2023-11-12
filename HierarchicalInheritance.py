# Hierarchical Inheritance

# Define the Person class, the top parent class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(f"Hello, my name is {self.name}")

    def display_age(self):
        print(f"I am {self.age} years old")


# Define the Employee class, a subclass of Person
class Employee(Person):
    def __init__(self, name, age, job_title, salary):
        super().__init__(name, age)
        self.job_title = job_title
        self.salary = salary

    def work(self):
        print(f"{self.name} is working as a {self.job_title}")

    def receive_salary(self):
        print(f"{self.name} received a salary of {self.salary}")


# Define the Student class, another subclass of Person
class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

    def study(self):
        print(f"{self.name} is studying {self.course}")


# Create instances of the Employee and Student classes
employee1 = Employee("Alice", 30, "Software Engineer", 70000)
student1 = Student("Bob", 20, "Computer Science")

# Call methods on the instances to demonstrate inheritance
employee1.speak()
employee1.work()
employee1.receive_salary()

student1.speak()
student1.study()
student1.display_age()