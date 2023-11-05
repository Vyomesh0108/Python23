import numpy as np

# 1D Array
# arr = np.array([1, 2, 3, 4, 5])
# print(arr[0] + arr[2])

# 2D Array
# ([Elements[Items]])
# y = np.array([[1, 2, 3], [4, 5, 6]])
# print(y[1, 1])

# 3D Array
# z = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
# print(z[0, 1, 1])  # 5
# print(z[1, 0, 2])  # 9
# print(z[1, 1, 2])  # 12
# print(z[0, 1, 0])  # 4
# print(z[1, 0])
# print(z[-1])

# Range in 1D Arrays
# arr = np.array([1, 2, 3, 4, 5])
# print(arr[1:3])
# print(arr[0:4:2])
# print(arr[3:])
# print(arr[:4])
# print(arr[-3:-1])

# Range in 2D Arrays
# y = np.array([[1, 2, 3], [4, 5, 6]])
# print(y[1, 0:2])

# Shape of Arrays
# print(y.shape)  # Gives output in (Elements, Items)

# Reshape Array
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
# print(arr.ndim)

# Change array into 4 elements
# new_arr = arr.reshape(4, 3)
# print(new_arr)
# print(new_arr.ndim)

# new_arr2 = arr.reshape(2, 3, 2)
# print("Reshape Array")
# print(new_arr2)
# print(new_arr2.ndim)

# 1D Array
# arr_1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

# for x in arr_1:
#     print(x)

# 2D Array
# arr_2 = np.array([[1, 2, 3], [4, 5, 6]])

# for x in arr_2:
#     print(x)

# for x in arr_2:
#     for y in x:
#         print(y)

# 3D Array
# arr_3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

# for z in arr_3:
#     print(z)
#
# for x in arr_3:
#     for y in x:
#         print(y)
#
# for x in arr_3:
#     for y in x:
#         for z in y:
#             print(z)


# nditer() for 3D Arrays
# for x in np.nditer(arr_3):
#     print(x)

# Create an Array start from 0, ends at 59 and stop size is 5
arr = np.arange(0, 60, 5)
# print(arr)
# 3 Elements and 4 items in each element
new_arr = arr.reshape(3, 4)
print(new_arr)

# for x in np.nditer(new_arr):
#     print(x)

# Order = 'C', 'C' is used for Rows
print("Sorted the output in form of Rows")
# Rows
for x in np.nditer(new_arr, order='C'):
    print(x)

# Order = 'F', 'F' is used for Columns
print("Sorted the output in form of Columns")
# Columns
for x in np.nditer(new_arr, order='F'):
    print(x)

# s = np.arange(3, 31, 3)
# print(s)
# new_s = s.reshape(5, 2)
# print(new_s)