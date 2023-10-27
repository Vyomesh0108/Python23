# #A triangle can be classified based on the lengths of its sides as equilateral, isosceles
# or scalene. All 3 sides of an equilateral triangle have the same length. An isosceles
# triangle has two sides that are the same length, and a third side that is a different
# length. If all of the sides have different lengths then the triangle is scalene.
# Write a program that reads the lengths of 3 sides of a triangle from the user.
# Display a message indicating the type of the triangle.

# Read the length of 3 sides from the user
x=float(input("enter 1st side of triangle: "))
y=float(input("enter 2nd side of triangle: "))
z=float(input("enter 3rd side of triangle: "))

# identify the type of the triangle
if x == y and y == z:  #if x==y==z :
    print("Equilateral Triangle")
elif (x == y) or y == z or z == x:
    print('Isoscele Triangle')
else:
    print('Scalene Triangle')

