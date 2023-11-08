for i in range(10):
    print(" "+str(i), end="")

print(" ")

for i in range(1, 11):
    print(" "+str(i), end="")

print(" ")

# Even Numbers ↓
for i in range(2, 11, 2):
    print(" "+str(i), end="")

print()

# Odd Numbers
for i in range(1, 10, 2):
    print(" "+str(i), end="")

print(" ")

# Loop using zip() function

fruits = ["Apple", "Banana", "Cherry"]
colors = ["Red", "Yellow", "Red"]

for fruits, colors in zip(fruits, colors):
    print(fruits, "is", colors)