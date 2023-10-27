# my_dict={}
mydict={1:'good',2:'very good',3:'perfect',4:'wow'} # the keys are int
# print(mydict[1])
# print(mydict.get(1))
# print(mydict.get(6))
# #print(mydict[6])
# my_dict={'name':'emma','age':22,'salary':2136.78,2:'perfect'} # dict with mixed keys
# print(my_dict['name'])
#
# # Use of dict()
# mydict1=dict({1:'good',2:'bad'})
# print(mydict1[2])
# # update a value
# mydict1[2]='very good'
# print(mydict1)

# Delete items from dict
mydict2={1:3,2:6,3:9,4:12,5:15}
print(mydict2)
print(mydict2.pop(3)) #  delete the item with key=3 and returns its value
print(mydict2)
print(6 in mydict2.values())
# remove all items
mydict2.clear()
print(mydict2)
# delete the dict
del mydict2
#print(mydict2)

d={1:'a',2:'b',3:'c'}
# test if a key is present in the dict
print(1 in d) # Boolean: True
print(1 not in d) # Boolean: False
print(9 in d) # Boolean: False
# Test if a specific value exists in the dict
print('a' in d.values()) # Boolean true

d={'name':'John','age':32,'year':1989,'year':2000}
print(d)

f={90:'A',80:'B',70:'C',60:'D',50:'F'}
# The number of items
print(len(f)) # returns the number of items

# A list inside a dict
e={1:'A','daysofweek':['Monday','Thursday','Friday'],'Fulltime':False}
print(e)
print(e['daysofweek'])
print(e['daysofweek'][0])
print(type(e))