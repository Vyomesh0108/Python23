# Q) WAP to check whether the given number is odd or even by switch?

def OddEven(no):
    switch = {
        1: "Odd",
        2: "Even"
    }
    return switch.get(no, "Invalid Operation")


no = int(input("Enter No: "))

if no % 2 == 0:
    no = 2
else:
    no = 1

print("\n Number is : ",OddEven(no))