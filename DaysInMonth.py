m = int(input("Enter the month as number between 1 and 12:"))
y = int(input("Enter the year in 4 digits:"))


def daysinmonth(month, year):
    if 1 <= month <= 12:
        if month == 2:
            if year % 4 == 0:  # leap year
                if year % 100 == 0:
                    if year % 400 == 0:
                        print('Month', month, 'has 29 days')
                    else:
                        print('Month', month, 'has 28 days')
                else:
                    print('Month', month, 'has 29 days')
            else:
                print('Month', month, 'has 28 days')
        else:
            if month in [1, 3, 5, 8, 10, 12]:
                print('Month', month, 'has 31 days')
            else:
                print('Month', month, 'has 30 days')
    else:
        print('Month provided is invalid')


daysinmonth(m, y)
