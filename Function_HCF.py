# Q) WAP to find HCF by function?

def hcf(x, y):
    if x < y:
        smaller = x
    else:
        smaller = y

    for i in range(1, smaller+1):
        if (x % i == 0) and (y % i == 0):
            hcf = i

    return hcf


no1 = int(input("Enter No1: "))
no2 = int(input("Enter No2: "))

print("\n HCF : ",hcf(no1, no2))