import sys

print(sys.version)
print("")

# stdin
# for line in sys.stdin:
#     if 'q' == line.rstrip():
#         break
#     print(f'Input : {line}')
#
# print("Exit")

# stdout
sys.stdout.write("Vyomesh")
print("")


# stderr
def print_to_stderr(*a):
    # Here a is the array holding the objects
    # Passed as the argument of the function
    print(*a, file=sys.stderr)


print_to_stderr("Hello World")

print("")
# Command Line Arguments
# Total Arguments
n = len(sys.argv)
print("Total arguments passed:", n)

# Arguments passed
print("\n Name of Python script:", sys.argv[0])

print("\n Arguments passed:", end=" ")
for i in range(1, n):
    print(sys.argv[i], end=" ")

# Addition of numbers
Sum = 0

for i in range(1, n):
    Sum += int(sys.argv[i])

print("\n\n Result:", Sum)

print("")
# Exiting
age = 17

if age < 10:
    # exits the program
    sys.exit("Age less than 18")
else:
    print("Age is not less than 18")

print("")
# Working with modules
print(sys.path)

print("")
# Truncating the values of sys.path
# Removing the values
sys.path = []

# importing pandas after removing values
import pandas

print(sys.modules)

print("")
# Reference count

a = 'Vyomesh'

print(sys.getrefcount(a))