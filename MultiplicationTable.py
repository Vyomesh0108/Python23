# Question 2:

# In this exercise you will create a program that displays a multiplication table that shows the products if all
# combinations of integers from 1 times 1 up to and including 10 times 10.
# Your multiplication table should include a row of labels across the top of it containing the numbers 1 through 10.
# It should also include labels down the left side consisting of the numbers 1 through 10.

# Solution:

# First, I assigned a value to 'no' as 10.
no = 10

# Then, I use print statement for keeping some space from the starting point.
print(" ", end=" ")
# I used for-loop statement for executing this problem.
# This for-loop is used to print the first row label of the program.
# Taken 'i' as the variable for the for-loop, and set the range, initially starting from 1, and then it will continuously
# increment the 'no' till it reaches to '10'.
for i in range(1, no+1):
    # This is the formatted string which begins with 'f'.
    # Inside this formatted string, 'i' represents the variable of for-loop.
    # ':5' this will reserve 5 spaces from the number.
    # It will print the value of 'i' with width of 5 characters, and every number is separated by space at the end.
    print(f"{i:5}", end=" ")
print()

# Here, I have taken another for-loop which will print the multiplication table with the label on left side.
# This 'i' is for the columns
for i in range(1, no+1):
    # It will print the value of 'i' with the width of 2 characters, and every number is separated by the space at the end.
    print(f"{i:2}", end="  ")
    # This is used for giving the extra space between the character at the end.
    print(end="  ")
    # This 'j' is for the rows
    # Taken 'j' as the variable, and set the range, initially starting from 1, and then it will continuously increment
    # the 'no' till it reaches to '10'.
    for j in range(1, no+1):
        # This will first convert the int 'i' and 'j' into string, then it will print the product of 'i' and 'j'.
        # Finally, It will print the product of 'i' and 'j' with width of 4 characters, and each number is separated
        # by the space at the end
        print(f"{str(i*j):4}",end="  ")
    print()


# OR
print("\n")
print("\n")

# Print column labels
print("    ", end="")
# Column Label Loop
for i in range(1, 11):
    # Usage of f'string with end
    print(f"{i:4}", end="")
print("\n " + " " * 5 + "-" * 40)

# Print rows with labels and multiplication results
# Row lable (Outer loop)
for i in range(1, 11):
    # Usage of f'string with end
    print(f"{i:2}  |", end="")
    # Usage of f'string with end
    # Column loop (Inner Loop)
    for j in range(1, 11):
        result = i * j
        print(f"{result:4}", end="")
    # Used to move the cursor to the next line, print() =
    print()
print("\n")