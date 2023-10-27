def average ():
   numbers = []
   sum = 0
   average = 0.0

   while(True): # will always run until I reach the break
    user_input_num = int(input('Enter values, enter 0 to stop ')) # float
    if user_input_num ==0:
      break
    else:
      numbers.append((user_input_num))

    for item in numbers:
      sum += item # calculate the sum
    average = sum/(len(numbers))
   print("average is %.2f "%average)

average ()
# input_string = input('Enter elements of a list separated by space ')
# print("\n")
# user_list = input_string.split(" ")
# sum = 0
# # convert each item to int type
# for i in range(len(user_list)):
#     # convert each item to int type
#     if(user_list[i]==0):
#         break
#     user_list[i] = int(user_list[i])
#     sum = sum+user_list[i]
# print("Average of numbers is %.2f" %(sum/len(user_list)))


