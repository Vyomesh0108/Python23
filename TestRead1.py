# 3 steps: Open- Read- Close
# Exceptions Handling
# f=open('python.txt','r') # Use r for read mode
# try:
#     contents=f.read() # Read all the data in my file
#     print(contents) # processing in your program
# finally:
#     f.close()

#
# with open('python.txt') as f: # define the scope of work
#     contents = f.read()
#     print(contents)
#     # exit() will be automatically executed --> Close the file and release any resources
# print('Hello')

# ******************** readline() **************************
# file = open("python.txt", "r")
# example1 = file.readline() # returns one line at a time, as a STRING
# example2 = file.readline() # number of bytes to return
# print(example1)
# print(example2)

# ******************** readlines() **************************
# file = open("python.txt", "r")
# example1 = file.readlines() # the whole file is returned as a LIST of STRING
# example2 = file.readlines(-1) # the whole file is returned as a LIST of STRING
# #example2 = file.readlines(50) # the lines exceeding the number of bytes will NOT be returned
# #example2 = file.readlines(-2) # the whole file is returned as a LIST of STRING
# print(example1)
# print(example2)

