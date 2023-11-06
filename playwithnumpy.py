import numpy as np
import matplotlib.pyplot as plt
a=np.array([(1,2,3),(3,4,5)])
b=np.array([(1,2,3),(3,4,5)])
print(a.size) # returns the number of elements
print(a.sum())
print(a+b)
# axis 1: rows
# axis 0: columns
a = np.array([(1,2,3),(3,4,5)])
# At axis=0 it will sum 1+3, 2+4, 3+5 from above array
# At axis=1 it will sum of 1+2+3 and 4+5+6 from above array
print(a.sum(axis=0)) #[4 6 8]
print(a.sum(axis=1))

x=np.arange(0,3*np.pi,0.1)
y=np.sin(x)
# Plot the graph
plt.plot(x,y)
# To see the graph..
plt.show()