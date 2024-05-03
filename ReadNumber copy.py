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
