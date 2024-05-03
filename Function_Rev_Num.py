# Q) WAP to reverse the given number by functions?

def reverse(n):
    rev = 0
    rem = 0

    while n >= 1:
        rem = n % 10
        rev = (rev * 10) +rem
        n = n // 10

    return rev


n = int(input("Enter No: "))
rev = reverse(n)
print("\n REVERSE NO: ",rev)