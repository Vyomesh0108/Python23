def is_prime(number):
    if(number <= 1):
        print("Invalid number entered")
        return False
    else:
        for i in range (2, number):
            if(number%i) == 0:
                return False
        return True

# Execution starting from here
number = int(input("Please enter integer number :"))
if is_prime(number):
    print(str(number)+" is Prime")
else:
    print(str(number)+" is not Prime")
