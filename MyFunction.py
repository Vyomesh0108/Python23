def show():
    print("Welcome to the world of Functions")
    print("We are in Functions")


def fact(no):
    i = 1
    f = 1

    while i <= no:
        f = f * i
        i = i + 1

    return f


def power(x, n):
    i = 1
    p = 1

    while i <= n:
        p = p * x
        i = i + 1

    return p


a = int(input("Enter X: "))
b = int(input("Enter N: "))
p = power(a, b)
print("\n POWER: ",p)

show()

no = int(input("Enter No: "))
f = fact(no)
print("\n FACTORIAL: ",f)