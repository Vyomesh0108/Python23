# using numpy to read in files: genfromtxt
import numpy as np
wines=np.genfromtxt('winequality-red.csv',delimiter=';',skip_header=1)
print(wines)
