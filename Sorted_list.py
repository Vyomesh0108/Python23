# Solution 1
z=[]

x=int(input("Enter values for sorting(enter 0 for stopping the input): "))
while x!=0:
      z.append(x)
      x = int(input("Enter values for sorting(enter 0 for stopping the input): "))

def print_sorted(z) :
    z.sort()
    for i in z:
        print(i)
    '''print(sorted(z))'''
print_sorted(z)

# Solution 2
z=[]
while(1):
    x=int(input("Enter values for sorting(enter 0 for stopping the input): "))
    if x != 0 :
        z.append(x)
        continue
    else:
        break

def print_sorted(z) :
    z.sort()
    for i in z:
        print(i)
    '''print(sorted(z))'''
print_sorted(z)
