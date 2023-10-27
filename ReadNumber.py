# Question 4:

# Write a program that reads numbers from the user until a blank line is entered.
# - Your program should display the average of all the values entered by the user.
# - Then the program should display all the below average values, followed by all the
# average values (if any), followed by all of the above average values.
# - An appropriate label should be displayed before each list of values.

# Created an empty list for storing numbers enter by the user.
number = []
while True:
    # This will take input from the user
    user = input('Please Enter only numbers: ')
    # If the user input is blank line then the statement will break and user input will be appended to the number list.
    if user == '':
        break
    number.append(int(user))

# Calculate average
average = sum(number) / len(number)

# Created 3 empty lists
# Categorize numbers
below_average = []
average_values = []
above_average = []

for number in number:
    # If the values of number list in below the overall average then that values will be appended to the below_average list.
    if number < average:
        below_average.append(number)
    # If the values of number list is equals to the overall average then that values will be appended to the average_values list.
    elif number == average:
        average_values.append(number)
    # Rest, values of number list is above the overall average then that values will be appended to the above_average list.
    else:
        above_average.append(number)

print("\n")
print(f'The average is {average}')
print(f'The values below the average are {below_average}')
print(f'The values above the average are {above_average}')
print(f'The average values are{average_values}')

# OR
print("\n")

# List to store numbers
no = []
non_numeric_inputs = []


def is_number(input_string):
    return True if input_string.replace(".", "").isnumeric() else False


# Read numbers from the user until a blank line is entered
while True:
    num = input("Enter a number (or press Enter to finish): ")
    if num == "":
        break
    if is_number(num):
        no.append(float(num))
    else:
        non_numeric_inputs.append(num)

# Calculate the average of all values
avg = sum(no) / len(no) if no else 0

# Categorize numbers into below average, average, and above average
below_average_values = [num for num in no if num < average]
average_values = [num for num in no if num == average]
above_average_values = [num for num in no if num > average]

# Display the average and categorized values
if no:
    print("Average:", average)
    print("Below Average Values:", below_average_values)
    print("Average Values:", average_values)
    print("Above Average Values:", above_average_values)
    print("Non Numeric Inputs", non_numeric_inputs)
else:
    print("At-least one numeric value is needed for computing.")
