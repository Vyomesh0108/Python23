# Q) WAP to enter 2 numbers & any arithmetc operator and print appropriate by using switch?

def arith(op):
    switch = {
        "+": a + b,
        "-": a - b,
        "*": a * b,
        "/": a / b,
        "%": a % b
    }
    return switch.get(op, "Invalid Operator")


a = int(input("Enter No1: "))
b = int(input("Enter No2: "))
c = input("Enter Operator: ")

print("\n\n Output = ", arith(c))
