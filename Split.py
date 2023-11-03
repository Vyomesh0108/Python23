# split function for taking inputs

# Taking 2 inputs at a time
x, y = input("Enter two values: ").split()
print("Number of boys : ", x)
print("Number of girls : ", y)

# Taking 3 inputs at a time
x, y, z = input("Enter three values: ").split()
print("Total Number of Students : ", x)
print("Number of boys are : ", y)
print("Number of girls are : ", z)

# Taking 2 inputs at a time in different way
a, b = input("Enter two values: ").split()
print("First number is {} and second number is {}".format(a, b))

# Taking multiple inputs at a time
# and type casting using list() function
x = list(map(int, input("Enter multiple values: ").split()))
print("List of students: ", x)