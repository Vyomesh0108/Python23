my_list=[] # empty list
my_list=[1,2,2] #list of integer, it allows duplicate values
my_list2=['hello',23,3.5] # list with mixed data types

# Nested list
my_list=["Hello",3,[1,2,3,"Welcome"],[45.67,[1,0,"Emma"]]]

#Accessing the list elements
# Index starts at 0

my_list=["p","y","t","h","o","n"] # index range?  ->0 to 5
#print(my_list[0]) #p
#print(my_list[3])   #h
#print(my_list[6]) # indexError
#print(my_list[-1])  #n
# display the "o"
#print(my_list[4])
#print(my_list[-2])
# print(my_list[2:5]) # it returns a list
# print(my_list[2:])
# print(my_list[:-2]) # from the begin to -2
# print(my_list[:])
# print(my_list)

# accessing the nested list
my_nlist=[23,[2,4,6]]
my_nested_list=["welcome",[1,2,3]]
# print("Accessing the nested list")
# print(my_nested_list[0])
#print(my_nested_list[0][0]) # w
# print(my_nested_list[1])
# print(my_nested_list[1][1])#2
# # display the element 3?
# print(my_nested_list[1][2])
# print(my_nlist)
# print(my_nlist[0]) #23
#print(my_nlist[0][0]) #?
# print(my_nested_list[0][3])#c
# a="welcome"
# print(a[3:4])

# Changing the list elements
x=[1,3,5,7]
# # Set the first element to 11: UPDATE
x[0]=11
print(x)
# # Multi-Update
# x[1:3]=[45,67]
# print(x)

# Add an element
# x.append(9)
# print(x)
# # Add multi-values
# x.extend([3,9,45,600])
# print(x)
# y=["hello"," world"]
# z=y+x
# print(x+y)
# print(z)
# print(x*2)
# insert an item
# w=[1,6]
# w.insert(1,3)
# print(w)
# w[2:2]=[18,56]
# print(w)
# w.clear()
# print(w)
# delete an element
#del w[1]
#print(w)

# del w[1:3]
# print(w)
#
# del w # Remove the list
# print(w) # it does not exist any longer

# a=[2,4,2,7,2,9,2]
# print(a.count(2)) # retrurns the number pof occurence of a value
# a.sort()
# print(a)
# b=["s","e",23] # in alphabetical order
# b.sort()
# print(b)
r=[7,5,2,1,3]
r.sort() # in ASC
print(r)
r.sort(reverse=True)# DESC way
print(r.sort())
print("the reversed list is ",r)
del r
print(r)