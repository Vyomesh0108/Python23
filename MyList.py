lst = [10, 20, 5.6, "Vyomesh", "Deepak", "Mistry", 3.14]

print(lst)

lst[1] = "Vrutti"
lst.insert(4, "Panipuri")
lst.remove("Deepak")
print(lst.pop())

for value in lst:
    print(value, end=" ")

print("")

name = []

for i in range(1, 5):
    st = input("Enter Name: ")
    name.extend([st])

print(name)

print("")

odds = []

for i in range(1, 20, 2):
    odds.append(i)

print(odds)

even = []

for i in range(0, 21, 2):
    even.append(i)

print(even)

# Taking 2 inputs at a time using list
x, y = [int(x) for x in input("Enter two values: ").split()]
print("First Number is : ", x)
print("Second Number is : ", y)

# OR

# x, y = [int(x) for x in input("Enter two values : ").split()]
# print("First number is {} and second number is {}".format(x, y))

# Taking 3 inputs at a time using list
x, y, z = [int(x) for x in input("Enter two values: ").split()]
print("First Number is : ", x)
print("Second Number is : ", y)
print("Third Number is : ", z)

# Taking multiple inputs at a time
x = [int(x) for x in input("Enter multiple values : ").split()]
print("Number of list is : ", x)
