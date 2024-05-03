# Q) WAP to check whether the given string is palindrome or not?

st = input("Enter String: ")
rev = st[::-1]

if st.__eq__(rev):
    print("String is Palindrome")
else:
    print("String is not Palindrome")

