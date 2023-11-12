# Multiple Inheritance

# Parent Class
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, my name is {self.name}")


# Child Class
class Student(Person):
    def __init__(self, name, school):
        super().__init__(name)
        self.school = school

    def study(self):
        print(f"{self.name} is studying at {self.school}")


# Child Class
class Employee(Person):
    def __init__(self, name, company):
        super().__init__(name)
        self.company = company

    def work(self):
        print(f"{self.name} is working at {self.company}")


# StudentEmployee class inherits from both the Student and Employee classes.
# This is an example of multiple inheritance.
class StudentEmployee(Student, Employee):
    def __init__(self, name, school, company):
        Student.__init__(self, name, school)
        Employee.__init__(self, name, company)

    def do_both(self):
        print(f"{self.name} is studying at {self.school} and working at {self.company}")


person = Person("John Doe")
person.greet()

student = Student("Jane Doe", "XYZ University")
student.greet()
student.study()

employee = Employee("Mark Doe", "ABC Corporation")
employee.greet()
employee.work()

student_employee = StudentEmployee("Smith Doe", "ABC University", "DEF Corporation")
student_employee.greet()
student_employee.study()
student_employee.work()
student_employee.do_both()