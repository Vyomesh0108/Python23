# Taking the input in the form of cents from the user
cents = int(input("\n Enter number of cents: "))

# 1 toonie = 200 cents
toonies = 200
# 1 1oonie = 100 cents
loonies = 100
# 1 quarter = 25 cents
quarters = 25
# 1 dime = 10 cents
dimes = 10
# 1 nickel = 5 cents
nickels = 5
# 1 penny = 1 cent
pennies = 1

# Here, I have taking if condition
# If the value of cents is greater than 200 then it will divide the cents from the toonies
if cents >= 200:
    toonies = cents / toonies

# If the value of cents is greater than 100 then it will divide the cents from the loonies
if cents >= 100:
    loonies = cents / loonies

# If the value of cents is greater than 25 then it will divide the cents from the quarters
if cents >= 25:
    quarters = cents / quarters

# If the value of cents is greater than 10 then it will divide the cents from the dimes
if cents >= 10:
    dimes = cents / dimes

# If the value of cents is greater than 5 then it will divide the cents from the nickels
if cents >= 5:
    nickels = cents / nickels

# Pennies are equals to cents
pennies = cents

# Printed the number of Toonies according cents
print("\n"+str(cents)+" cents equals to : "+str(toonies)+" toonies")

# Printed the number of Loonies according cents
print("\n"+str(cents)+" cents equals to : "+str(loonies)+" loonies")

# Printed the number of Quarters according cents
print("\n"+str(cents)+" cents equals to : "+str(quarters)+" quarters")

# Printed the number of Dimes according cents
print("\n"+str(cents)+" cents equals to : "+str(dimes)+" dimes")

# Printed the number of Nickels according cents
print("\n"+str(cents)+" cents equals to : "+str(nickels)+" nickels")

# Printed the number of Penny according cents
print("\n"+str(cents)+" cents equals to : "+str(pennies)+" pennies")