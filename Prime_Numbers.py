# Q) WAP to find Prime Numbers?

no = int(input("Enter NO: "))

i = 2
f = 0

while i < no:
    if no % i == 0:
        f = 1
        break

    i += 1

if f == 1:
    print("It is not a Prime Number")
else:
    print("It is a Prime Number")