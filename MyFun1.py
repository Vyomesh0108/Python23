print("Hello World")
print("VALUE OF __NAME__ : " + __name__)

# "__NAME__" → Dunder Variable. It is automatically created by python.
# If same program is run directly in which this variable is used it returns "__main__".
# If same other program indirectly calls a program which contains dunder name then it returns current program name.

if __name__ == "__main__":
    print("\n Current Program is directly run by user")
else:
    print("\n It is called by another program")


def show():
    print("Welcome to the world of functions")
    print("We are in functions")


print("Nice Thank You")
