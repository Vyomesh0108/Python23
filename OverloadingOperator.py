# Addition

class A:
    def __init__(self, a):
        self.a = a

    # Addintg two objects
    def __add__(self, o):
        return self.a + o.a


ob1 = A(1)
ob2 = A(2)
ob3 = A("Geeks")
ob4 = A("For")

print(ob1 + ob2)
print(ob3 + ob4)

print(A.__add__(ob1, ob2))
print(A.__add__(ob3,ob4))

print(ob1.__add__(ob2))
print(ob3.__add__(ob4))

# Complex numbers
class complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return self.a + other.a, self.b + other.b


Ob1 = complex(1, 2)
Ob2 = complex(2, 3)
Ob3 = Ob1 + Ob2
print(Ob3)

# Comparison Operator
class B:
    def __init__(self, a):
        self.a = a

    def __gt__(self, other):
        if self.a>other.a:
            return True
        else:
            return False

OB1 = B(2)
OB2 = B(3)

if OB1 > OB2:
    print("OB1 is greater than OB2")
else:
    print("Ob2 is greater than OB1")


# Equality and Less Than Operator

class C:
    def __init__(self, a):
        self.a = a

    def __lt__(self, other):
        if (self.a < other.a):
            return "ob1 is lessthan ob2"
        else:
            return "ob2 is less than ob1"

    def __eq__(self, other):
        if (self.a == other.a):
            return "Both are equal"
        else:
            return "Not equal"


oB1 = C(2)
oB2 = C(3)
print(oB1 < oB2)

oB3 = A(4)
oB4 = A(4)
print(oB1 == oB2)


# ~ Operator
class D:
    def __init__(self, a):
        self.a = a

    def __invert__(self):
        return "This is the ~ operator, overloaded as binary operator"


op1 = D(2)
print(~op1)

# Boolean Operator
class MyClass:
    def __init__(self, value):
        self.value = value

    def __and__(self, other):
        return MyClass(self.value and other.value)


a = MyClass(True)
b = MyClass(False)
c = a & b  # c.value is False

