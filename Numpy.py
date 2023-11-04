import numpy as np

# 1D Array
# Create an Array
print("1 Dimensional Array")
arr = np.array([1, 2, 3, 4])
print(arr)
print("Dimensions :",arr.ndim)
# print(type(arr))

print("")

print("2 Dimensional Array")
# 2D Array
arr2d = np.array([[1, 2, 3],[4, 5, 6]])
print(arr2d)
print("Dimensions : ",arr2d.ndim)

print("")
print("3 Dimensional Array")
# 3D Array
arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr3d)
print("Dimensions : ",arr3d.ndim)

print("")
# Create an Array with Tuple
arrt = np.array((5, 6, 7))
print(arrt)

print("")
# Scalars - Elements in Array
x = np.array(12)
print(x)
print(type(x))

print("")
