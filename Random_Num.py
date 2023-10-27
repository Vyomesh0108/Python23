# Question -3
# This exercise examines the process of identifying the maximum value in a collection of integers.
# Each of the integers will be randomly selected from the numbers between 1 and 100.
# The collection of integers may contain duplicate values, and some of the integers between 1 and 100 may not be present.
# * Use randrange and import the relative python library to generate the random numbers.


# Imported Random and randrange Library
import random
from random import randrange

# Taken a number of integers in want to generate randomly.
num = 10

# Generated random numbers between 1 amd 100 and set the range of the numbers
num_integer = [random.randrange(1, 101) for x in range(num)]

# Printed the generated numbers
print("Random Generated Numbers: ",num_integer)

# Found the Maximum value from the randomly generated numbers
max_num = max(num_integer)

# Printed the maximum values from the randomly generated numbers
print("Maximum Value of Numbers is ",max_num)

