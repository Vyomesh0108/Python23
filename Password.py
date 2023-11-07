# Question -1
# In this exercise you will write a function that determines whether or not a password is good.
# We will define a good password to be a one that is at least 8 characters long and contains at least
# one uppercase letter, at least one lowercase letter, and at least one number.
# Your function should return true if the password passed to it as its only parameter is good.
# Otherwise, it should return false.
# Include a main program that reads a password from the user and reports whether or not it is good.


def password(passwd):
    if len(passwd) >= 8:

        password_has_lowercase = False
        password_has_uppercase = False
        password_has_digit = False

        for char in passwd:
            if char.islower():
                password_has_lowercase = True
            elif char.isupper():
                password_has_uppercase = True
            elif char.isdigit():
                password_has_digit = True
        return password_has_digit and password_has_uppercase and password_has_lowercase
    else:
        return False


def main():
    passwd = input("Enter Password: ")

    if password(passwd):
        print("Good Password")
    else:
        print("Password doesn't meet the criteria for a good password")


if __name__ == '__main__':
    main()