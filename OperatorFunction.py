import operator

a = 4
b = 3
li = [1, 5, 6, 7, 8]
s1 = "geeksfor"
s2 = "geeks"
c = 1
d = 0

print(operator.add(a, b))
print(operator.sub(a, b))
print(operator.mul(a, b))
print(operator.truediv(a, b))
print(operator.floordiv(a, b))
print(operator.pow(a, b))
print(operator.mod(a, b))
print(operator.lt(a, b))
print(operator.le(a, b))
print(operator.eq(a, b))
print(operator.gt(a, b))
print(operator.ge(a, b))
print(operator.ne(a, b))

for i in range(0,len(li)):
    print(li[i],end=" ")

operator.setitem(li,3,3)
operator.delitem(li,1)
print(operator.delitem(li,3))
operator.setitem(li,slice(1,4),[2,3,4])
operator.delitem(li,slice(2,4))
print(operator.getitem(li,slice(0,2)))
print(operator.concat(s1,s2))
print(operator.and_(c,d))
print(operator.or_(c,d))
print(operator.xor(c,d))
print(operator.invert(c))