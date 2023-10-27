# TO CAPITALIZE THE CONTENT OF THE INPUT FILE
filename = input("Enter file's absolute path: ")
try:
    userFile = open(filename, "r")
except:
    print("File name entered is incorrect.")
    quit()

f= open(filename, 'r')
content= f.read()
print(str.upper(content))
f.close()
