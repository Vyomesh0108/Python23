# A particular zoo determines the price of admission based on the age of the guest.
# Guests 2 years of age and less are admitted without charge. Children between 3 and
# 12 years of age cost $14.00. Seniors aged 65 years and over cost $18.00. Admission
# for all other guests is $23.00.
# Create a program that begins by reading the ages of all of the guests in a group
# from the user, with one age entered on each line. The user will enter a blank line to
# indicate that there are no more guests in the group. Then your program should display
# the admission cost for the group with an appropriate message. The cost should be
# displayed using two decimal places.
# guest_age_list = []
# while(True):
#     user_input_age = input()
#     if user_input_age is "":
#         break
#     else:
#         guest_age_list.append(int(user_input_age))
# total_cost = 0.0
# for age in guest_age_list:
#     if age >= 3 and age <= 12:
#         total_cost += 14
#     elif age >= 65:
#         total_cost += 18
#     else:
#         total_cost += 23
#
# print("Total cost is %.2f"%total_cost)


# Answer 2
Baby_Age =2
Child_Age =12
Senior_Age=65
total=0.0

line=input('enter the age of the person: enter blank to finish')
while line != '':
    age = int(line)
    if age <=Baby_Age:
        total=total+0
    elif age <=Child_Age:
        total = total + 14
    elif  age <=Senior_Age:
        total = total + 18
    else:
        total = total + 23
    line = input('enter the age of the person: enter blank to finish') # next input value
print('the total is %.2f' % total)