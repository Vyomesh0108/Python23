
# Taken the name of months from the user in the form of string.
month = input("\n Enter Name of the Month: ")

# Created a list of months which has 31 days
month_of_31_days = ["January", "March", "May", "July", "August", "October", "December"]

# Created a list of month which has 30 days
month_of_30_days = ["April", "June", "September", "November"]

# I used the if statement to find the days of the month
# This statement checks the name of months in the list of 31 days per month;
# if the name of the month matches the name inside the list
# Then, it prints the output or looks for other conditions.
if month in month_of_31_days :
    print("\n Number of Days in "+month+" is 31")
# This statement checks the name of months in the list of 30 days per month;
# if the name of the month matches the name inside the list
# Then, it prints the output or looks for other conditions.
elif month in month_of_30_days:
    print("\n Number of Days in "+month+" is 30")
# If name of the month is equals to February, then it will take an input of the years form the user
elif month == "February":
    year = int(input("\n Enter Year: "))

    # This condition checks that if the year is divisible by 4, and it is also divisible by 400, but
    # If it is not divisible by 100, it is a leap year of 29 days.
    # But, if the year does not satisfy this statement, it is 28 days a month.
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        print("\n Number of Days in February of the "+str(year)+" is 29 days and this year called as leap year")
    else:
        print("\n Number of Days in February of the " + str(year) + " is 28 days")
# This will appear when the user is going to enter the wrong input or the wrong name of the month.
else:
    print("\n Please Enter the Correct Name of the Month!!!!")