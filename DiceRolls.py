# Question -2
# In this exercise you will simulate 1,000 rolls of two dice. Begin by writing a function that
# simulates rolling a pair of six-sided dice.
# *Your function will not take any parameters.
# * It will return the total that was rolled on two dice as its only result.
# Write a main program that uses your function to simulate rolling two six-sided dice 1,000 times.
# As your program runs, it should count the number of times that each total occurs. Then it should
# display a table that summarizes this data.
# Express the frequency for each total as a percentage of the total number of rolls.
# Your program should also display the percentage expected by probability theory for each total.

# import random
#
#
# def roll_dice():
#     # Simulate rolling two six-sided dice
#     die1 = random.randint(1, 6)
#     die2 = random.randint(1, 6)
#     return die1 + die2
#
#
# def main():
#     # Initialize a dictionary to count the frequency of each total
#     frequency = {i: 0 for i in range(2, 13)}
#
#     # Simulate rolling the dice 1,000 times
#     total_rolls = 1000
#     for _ in range(total_rolls):
#         total = roll_dice()
#         frequency[total] += 1
#
#     # Display the table summarizing the data
#     print("Total\tPercentage\tExpected Percentage")
#     for total, count in frequency.items():
#         percentage = (count / total_rolls) * 100
#         expected_percentage = (count / 36) * 100  # Probability theory
#         print(f"{total}\t\t{percentage:.2f}\t\t{expected_percentage:.2f}")
#
#
# if __name__ == "__main__":
#     main()


# OR

import numpy as np


def dice_roll(total_rolls):
    return np.random.randint(1, 7, size=(total_rolls, 2)).sum(axis=1)


def main():
    recurrence = np.zeros(11)
    total = 1000

    rolls = dice_roll(total)
    for i in rolls:
        recurrence[i - 2] += 1

    print("Total\tSimulated Percent\tExpected Percent")
    for i in range(2, 13):
        simulated_percent = recurrence[i - 2] / total * 100
        expected_percent = (6 - abs(7 - i)) / 36 * 100
        print(f"{i}\t\t\t{simulated_percent:.2f}\t\t\t{expected_percent:.2f}")


if __name__ == "__main__":
    main()

