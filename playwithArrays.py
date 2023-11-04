import numpy as np

arr=np.arange(0,60,5)
arr_new=arr.reshape(3,4)
print(arr_new)
# #
print('Rows first')
for x in np.nditer(arr_new, order='C'): # row first set by default
    print(x)
print('Columns first')
for x in np.nditer(arr_new, order='F'): # column first
    print(x)

y=np.zeros((3,),dtype=int)
print(y)
z=np.arange(5,dtype=float) # start is optionl, by default is 0/ Step size is optional, default is 1
print(z)
#
s=np.arange(3,25,3)
print(s)

# an array filled with ones: by default float
t=np.ones(5)
print(t)
## an array filled with ones: integer
w=np.ones((5,),dtype=int)
print(w)

