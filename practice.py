# Write a program that displays a temperature conversion table for degrees Celsius and
# degrees Fahrenheit. The table should include rows for all temperatures between 0
# and 100 degrees Celsius that are multiples of 10 degrees Celsius. Include appropriate
# headings on your columns. The formula for converting between degrees Celsius and
# degrees Fahrenheit can be found on the internet.
MIN_val=0
Max_val=100
#print('         ',end='')
for i in range(MIN_val,Max_val+1,10): # range(0,101,10)
    print('%4d'%i, end='')
print() # new line
for j in range(MIN_val,Max_val+1,10):
    print('%4d' %(j*1.8+32), end='')




