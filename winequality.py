import csv
import numpy as np
with open('winequality-red.csv','r') as f:
    wines=list(csv.reader(f,delimiter=';'))
#print(wines[:3])

qualities = [float(i[-1]) for i in wines[1:]]

# Calculate the average
average=sum(qualities)/len(qualities)
print(average)
