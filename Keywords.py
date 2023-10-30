import keyword

print("The list of keywords is : ")
print(keyword.kwlist)

# True, False, None
print("")
print("True, False, None Keyword")
print(False == 0)
print(True == 1)

print(True + True + True)
print(True + False + False)

print(None == 0)
print(None == [])

# And, Or, Not, In, Is
print("")
print("And, Or, Not, In, Is Keyword")
print(True or False)
print(False and True)

if 's' in 'geeksforgeeks':
    print("s in part of geeksforgeeks")
else:
    print("s is not part of geeksforgeeks")

for i in 'geeksforgeeks':
    print(i, end="")

print("\r")

# print(" " is " ")
# print({} is {})

# And, Or, Not, In, Is
print("")
print("for, while, break, continue Keyword")

for i in range(10):
    print(i, end=" ")

    if i == 6:
        break

print()

i = 0
while i < 10:
    if i == 6:
        i += 1
        continue
    else:
        print(i, end=" ")

    i += 1


# If, Else, Elif
print("")
print("")
print("If, Else, Elif Keyword")
i = 20

if(i == 10):
    print("i is 10")
elif(i == 20):
    print("i is 20")
else:
    print("i is not present")

# def
print("")
print("def Keyword")
def fun():
    print("Inside Function")

fun()

# Return, Yield
print("")
print("Return and Yield Keyword")
def fun():
    s = 0

    for i in range(10):
        s += i
    return s

print(fun())


def fun():
    S = 0

    for i in range(10):
        S += i
        yield S

for i in fun():
    print(i)


# class
print("")
print("Class Keyword")

class Dog:
    attr1 = "mammal"
    attr2 = "dog"

    def fun(self):
        print("I'm a", self.attr1)
        print("Iim a", self.attr2)

Rodger = Dog()

print(Rodger.attr1)
Rodger.fun()


# with
print("")
print("With Keyword")
with open('file_path', 'w') as file:
    file.write('hello world!')


# as
print("")
print("as Keyword")
import math as gfg

print(gfg.factorial(5))

# pass
print("")
print("pass Keyword")
n = 10
for i in range(n):
    pass

# lambda
print("")
print("Lambda Keyword")
g = lambda x: x*x*x

print(g(7))

# import
print("")
print("Import Keyword")
from math import factorial
import math
print(math.factorial(10))

print(factorial(10))

# Exception Handling Keywords - try, except, raise, finally, and assert
print("")
print("try, except, raise, finally, and assert Keyword")

a = 4
b = 0

try:
    k = a//b
    print(k)

except ZeroDivisionError:
    print("Can't divide by zero")

finally:
    print("This is always executed")

# print("The value of a / b is : ")
# assert b != 0, "Divide by 0 error"
# print(a / b)
#
# temp = "geeks for geeks"
# if temp != "geeks":
#     raise TypeError("Both the strings are different.")

# del
print("")
print("del Keyword")

my_var1 = 20
my_var2 = "GeeksForGeeks"

print(my_var1)
print(my_var2)

del my_var1
del my_var2

# print(my_var1)
# print(my_var2)

# global, nonlocal
print("")
print("Global, Nonlocal Keyword")
a = 15
b = 10

def add():
    c = a + b
    print(c)

add()

def fun():
    var1 = 10

    def gun():
        nonlocal var1

        var1 = var1 + 10
        print(var1)

    gun()
fun()
