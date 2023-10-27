# Finding interest per year on the amount deposited by user

# Money is deposited in the savings account by the user
money_deposited = float(input("Enter the amount you want to deposit in the savings: "))

# The total amount of money in the savings accounts after user deposited money
print("\n Money in saving account: "+str(money_deposited))

# Total interest rate per year or annually
interest_per_year = 4

# I am going to use for loop for finding interest rate for 1st, 2nd, and 3rd year.
for time in range(1,4):
    # Here, I have multiply the time with interest rate and I divided it with 100.
    # Then, I multiply that value with amount of money deposited by user.
    # This way I found the total interest per year
    total_interest = money_deposited * (time * interest_per_year / 100)

    # Once, I found the interest, I simply added the interest with the money deposited by user
    # This way I found the total amount with the interest per year
    total_amount = money_deposited + total_interest

    # Then, I printed the total amount of per year after adding interest rate annually
    print("\n The final amount after "+str(time)+" year with interest is : ",round(total_amount,2))