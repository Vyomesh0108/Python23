# Write a program that determines the name of a shape from its number of sides. Read
# the number of sides from the user and then report the appropriate name as part of
# a meaningful message. Your program should support shapes with anywhere from 3
# up to (and including) 10 sides. If a number of sides outside of this range is entered
# then your program should display an appropriate error message.

# Read the number of sides from the user
num = int(input('Please enter the number of sides'))

if num == 3:
    print('it is a triangle')
elif num == 4:
    print('it is a quadrilateral')
elif num == 5:
    print('it is a pentagon')
elif num == 6:
    print('it is a hexagon')
elif num == 7:
    print('it is a heptagon')
elif num == 8:
    print('it is a octagon')
elif num == 9:
    print('it is a nonagon')
elif num == 10:
    print('it is a decagon')
else:
    print('sorry, the program does not support this shape')