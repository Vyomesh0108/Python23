# ************************ Use File Object and Iterator Execution Time Performance Test ****************
import time

start = time.time()
count = 0
with open("python.txt") as file: # returns a file object
    for line in file: # iterator
        print(line)
        count = count + 1
end = time.time()
print("Execution time in seconds: ", (end - start))
print("No of lines printed: ", count)
