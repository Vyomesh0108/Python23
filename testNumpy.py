import numpy as np

# Create an array
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr)) # numpy.ndarray
#

# Use a tuple to create the numpy array
arrt=np.array((1,2,3,4,5))
print(arrt)
#
# Dimensions in Arrays
# 0D array: scalars
x=np.array(12)
print(x)
print(type(x))

# 1D array
arr = np.array([1, 2, 3, 4, 5])
print(arr)
#
# 2D arrays
y=np.array([[1, 2, 3], [4, 5, 6]])
print(y)
# 3D arrays
z=np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(z)

# ndim : attribute --> int value: the dimension of your ndarray
x=np.array(12)
arr = np.array([1, 2, 3, 4, 5])
y=np.array([[1, 2, 3], [4, 5, 6]])
z=np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(x.ndim)
print(arr.ndim)
print(y.ndim)
print(z.ndim)

# Access elements in Numpy
arr = np.array([1, 2, 3, 4, 5])
print(arr[0]+arr[2]) # Add the first and the third elets

# Access 2D Arrays
y=np.array([[1, 2, 3], [4, 5, 6]])
print(y[0,1])
# return number 5?
print(y[1,1])

# Access 3D Arrays
z=np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(z[0,1,1]) # 5
print(z[1,0,2]) #9
print(z[1,0]) #[7 8 9]
print(z[-1]) # [[ 7  8  9] [10 11 12]]


arr = np.array([1, 2, 3, 4, 5,6, 7, 8])
print(arr[1:3]) # the index 3 is not included
print(arr[0:4:2])
# from index 3 to the end?
print(arr[3:])
# # from start to index 3 not included?
print(arr[:3])
print(arr[-3:-1])

y = np.array([[1, 2, 3], [4, 5, 6]])
# return 4 and 5?
print(y[1, 0:2])

# Shape of an array: shape is an attribute
y = np.array([[1, 2, 3], [4, 5, 6]])
print(y.shape) # (2, 3)

# Reshaping your array
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
# dimension?
print(arr.ndim)
# change the array into 4 elements (dimensions) with 3 items each?
new_arr=arr.reshape(4, 3)
print(new_arr)
print(new_arr.ndim)
new_arr_3=arr.reshape(2,3,2)
print(new_arr_3)

# Iterating over the array
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
for x in arr:
    print(x)

arr = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr:
    for y in x:
        print(y)
#
arr=np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in arr:
    for y in x:
        for z in y:
            print(z)

# nditer()
arr=np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in np.nditer(arr):
    print(x)