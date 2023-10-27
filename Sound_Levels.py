
# Taken the decibel values from the user in the float.
decibels = float(input("Enter the sound levels in decibels: "))

# Use if statement for checking the condition
# It checks if the decibel value is greater than 40, then it is the quietest sound.
if decibels < 40:
    print("\n This is quieter than the Quiet Room!")
# If the decibel value is equals to 40, then it is sound of quiet room.
elif decibels == 40:
    print("\n This is the sound of the Quiet Room!")
# If the decibel value is greater than 40 and less than 70, then the sound is between Quiet Room and Alarm Clock.
elif 40 < decibels < 70:
    print("\n The noise level is between the sound of Quiet Room and Alarm Clock!")
# If the decibel value is equals to 70, then it is sound of Alarm Clock
elif decibels == 70:
    print("\n This is the sound of the Alarm Clock!")
# If the decibel value is greater than 70 and less than 106, then the sound is between Alarm Clock and Gas Lawnmower.
elif 70 < decibels < 106:
    print("\n The noise level is between the sound of Alarm Clock and Gas Lawnmower!")
# If the decibel value is equals to 106, then it is sound of Gas Lawnmower
elif decibels == 106:
    print("\n This is the sound of the Gas Lawnmower!")
# If the decibel value is greater than 106 and less than 130, then the sound is between Gas Lawnmower and Jackhammer.
elif 106 < decibels < 130:
    print("\n The noise level is between the sound of Gas Lawnmower and Jackhammer!")
# If the decibel value is equals to 130, then it is sound of Jackhammer
elif decibels == 130:
    print("\n This is the sound of the Jackhammer!")
# If the decibel value is greater than 130, then it is the loudest sound.
elif decibels > 130:
    print("\n This is the loudest sound than the Jackhammer!")
# If the decibel value is
else:
    print("\n Invalid input. Please provide a valid sound decibels")