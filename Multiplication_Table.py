# Q) WAP to enter number & print multiplication table?

no = int(input("Enter No: "))

for i in range(1, 11):
    print(str(no) + "X" + str(i) + "=" + str(no * i))

print("")

#             ↑ OR ↓

no = int(input("Enter No: "))

for i in range(1, 11):
    print(no, 'X', i, '=', no * i)
