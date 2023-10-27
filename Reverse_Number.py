# Q) WAP to reverse the given number?

no = int(input("Enter No: "))

rev = 0
r = 0

while no >= 1:
    r = no % 10
    rev = (rev * 10) + r
    no = no // 10

print("Reverse No: "+str(rev))