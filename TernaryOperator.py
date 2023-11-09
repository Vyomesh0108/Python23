# Simple Ternary Example

a, b = 10, 20

# Copy value of a in min if a < b else copy b
mini = a if a < b else b

print(mini)

# Using if-else statement
# if a != b:
#     if a > b:
#         print("a is greater than b")
#     else:
#         print("b is greater than a")
# else:
#     print("Both a and b are equal")

# Above code using in ternary operator
print("Both a and b are equal" if a == b else "a is greater than b" if a > b else "b greater than a")

# Ternary Operator using Tuple
print((b, a)[a < b])

# Ternary Operator using Dictionary
print({True: a, False: b}[a < b])

# Ternary Operator using Lambda
print((lambda: b, lambda: a)[a < b]())

# Print in if Ternary Operator
a = 5
b = 7

print(a, "is greater") if (a>b) else print(b, "is greater")

