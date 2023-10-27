num = 4
if num < 0:
    print('negative number')
else:
    if num == 3:
        print('the number is 3')
    else:
        print('the number is different than 3')

a = ['hello','bar','zen']
for i in a:
    print(i)
x = iter(a)
print(next(x))
print(next(x))
print(next(x))
print(next(x))
