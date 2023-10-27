# # Unix-based operating systems usually include a tool named head. It displays the
# # first 10 lines of a file whose name is provided as a command line parameter. Write
# # a Python program that provides the same behavior. Display an appropriate error
# # message if the file requested by the user does not exist or if the command line
# # parameter is omitted.
def head(fileName):
    try:
        file = open(fileName, 'r')
        for i in range(10):
            read = file.readline()
            print(read, end="")
        file.close()
    except:
        print("File not found.")
        quit()

f = input("Please enter the name of the file: ")
head(f)

# ********************* Solution 2 ****************************
def head(fileName):
    try:
        file = open(fileName, 'r')
        count=0
        read = file.readline()
        while count < 10 and read !='':
            count =count+1
            print(read, end="")
            read = file.readline()
        file.close()
    except:
        print("File not found.")
        quit()

f = input("Please enter the name of the file: ")
head(f)
