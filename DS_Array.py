from array import *

array1 = array('i', [10, 20, 30, 40, 50])
print(array1[0])
print(array1[2])

print("\n")

print("Insertion")
# Insertion Operation

array1 = array('i', [10, 20, 30, 40, 50])
array1.insert(1, 60)

for i in array1:
    print(i)

print("\nDeletion")
# Deletion Operation

array1 = array('i', [10, 20, 30, 40, 50])
array1.remove(40)

for x in array1:
    print(x)

print("\nSearch")
# Search Operation

array1 = array('i', [10, 20, 30, 40, 50])
print(array1.index(40))

print("\nUpdate")
# Update Operation

array1 = array('i', [10, 20, 30, 40, 50])

array1[2] = 80

for z in array1:
    print(z)
