# Taking height from the user in the feet and inches
height = float(input("\n Enter Height in feet and inches: "))

# Value of one foot is 12 inches
one_foot = 12
# Value of one inches is 2.54 centimeters
one_inches = 2.54

# Found height in centimeters by multiplying values of foot with inches and then that value is multiply by height
total_height_in_cm = height * (one_foot * one_inches)

# Finally, the height is printing in centimeters
print("\n Total height in centimeter is : ",round(total_height_in_cm,2))
