import csv
import numpy as np
with open('winequality-red.csv','r') as f:
    wines=list(csv.reader(f,delimiter=';'))
awines=np.array(wines[1:],dtype=float)
print(awines)
print(awines.shape)

