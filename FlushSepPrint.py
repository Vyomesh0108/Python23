# Flush in print() function

import time

count_seconds = 3
for i in reversed(range(count_seconds + 1)):
    if i > 0:
        print(i, end=">>>", flush=True)
        time.sleep(3)
    else:
        print('Start')


# Sep in print() function
a = 12
b = 12
c = 2023
print(a,b,c,sep='/')