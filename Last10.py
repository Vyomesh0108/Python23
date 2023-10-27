filename = input("Enter file's absolute path: ")
try:
    userFile = open(filename, "r")
except:
    print("File name entered is incorrect.")
    quit()
lines = userFile.readlines(-1)
print("\nAll lines in provided files are: ")
print(lines)
print("\nLast 10 lines in provided files are: ")
count = 1
for line in lines[-10:]:
    print(str(count) + ". " + line)
    count = count + 1

# *************************** Solution 2 *******************************
filename = input("Enter file's absolute path: ")
try:
    userFile = open(filename, "r")
except:
    print("File name entered is incorrect.")
    quit()
lines = []
for line in userFile:
    lines.append(line)
    if len(lines)>10:
        lines.pop(0)

print("\nLast 10 lines in provided files are: ")

for line in lines:
    print(line, end='')
