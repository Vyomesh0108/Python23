# Q) WAP to find power of a given number?

no1 = int(input("Enter No1: "))
no2 = int(input("Enter No2: "))

power = 1
i = 1

while i <= no2:
    power = power * no1
    i += 1  # or i = i+1

print("POWER : "+str(power))