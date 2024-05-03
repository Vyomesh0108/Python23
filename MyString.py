print("GTU"*5)      # Prints "GTU" 5 Times
print()

for i in range(1, 6):
    print("*"*i)    # Draws Pattern

print()

for i in range(5, 0, -1):
    print("*"*i)    # Draws Pattern

print()

print(10*5)         # Multiply 10*5
print()

print([10]*5)       # Prints '10' 5 Times
print()

a = "gtu"
b = "GTU"

print("SAME : ",a.__eq__(b))    # Dunder __eq__ means 'Equals to'
print("NOT SAME : ",a.__ne__(b))    # Dunder __ne__ means 'Not Equals to'
print("BIGGER : ",a.__gt__(b))    # Dunder __gt__ means 'Greater than'
print("SMALLER : ",a.__lt__(b))    # Dunder __lt__ means 'Less than'
print()

st = "HELLO WORLD OYE"
print("Length : ",len(st))      # represents length of st
print()

for ch in st:
    print(ch, end="")           # Character in String

print()

print(st[6:11])     # Showing character from 6 to 11
print()
print(st[::1])
print()
print(st[::2])
print()
rev = st[::-1]      # Reverse String
print("REVERSE : ",rev)
print()

print(st.split(" "))    # Split string by space
print()
print(st.split("O"))    # Split String by 'o'
print()

st = st.lower()        # Convert String to Lowercase
print(st)
print()

st = st.upper()        # Convert String to Uppercase
print(st)
print()

st = st.capitalize()    # Convert String to Capitalize
print(st)
print()

st = "BALAGURUSAMY"

print('GURU' in st)
print()
print('GURU' not in st)
print()

st = "PRIYANKA CHOPRA"
st = st.replace('A', 'O')       # Replacing Letters from String
print(st)
print()

a = "Vyomesh"
b = 20
c = 5.5

st = "My Name is {}. I am {} years old. My Height is {}ft."
print(st.format(a,b,c))
print()

st = f"My Name is {b}. I am {c} years old. My Height is {a}ft."
print(st)
print()

st = "           gtu            ma    jalsa     "
print(st.strip(),"hello")

# for escaping the single quote use \' or you can use double quote
x = 'doesn\'t'
print(x)
x = "doesn't"
print(x)

# \n means next line
# we can use raw string 'r' by adding it before the single quote
print(r'C:/show/name')

# Two or more string literals next to each others are automatically connected with each other
print('Py' 'thon')

