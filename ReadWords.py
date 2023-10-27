# Question 3:

# In this exercise, you will create a program that reads words from the user until the user enters a blank line.
# After the user enters a blank line your program should display each word entered by the user exactly once.
# The words should be displayed in the same order that they were entered.

# First, I have created an empty list for storing user's input
words = []

print("Please Hit Enter Once you finish")

# While True means it will continue to read further code
while True:
    # This will take inputs from the user in string format
    user_input = input("Enter Words You Want to Read: ")

    # If the user input is 'NULL' or blank line then, the condition is break.
    if user_input == "":
        break
    # Once the condition is break, It will append the 'words' empty list with user input
    words.append(user_input)

# Now, I have created another empty list for displaying the user input
word_list = []
# This for-loop goes to the every values inside the 'words' list
for user_input in words:
    # If the value which is entered by the user is not in newly created 'word_list'.
    # Then that values will be appended to the new list
    if user_input not in word_list:
        word_list.append(user_input)

print("\n Words Enter By The User: ")
# This will print the value inside the 'word_list'
for user_input in word_list:
    print(user_input)

# OR
print("\n")

# List to store words entered by the user.
word_l = []

# Read words from the user until a blank line is entered
while True:
    word = input("Enter a word (or press Enter to finish) : ")

    if word == "":
        break
    word_l.append(word)

# Display unique words in the order they were entered
statement = "Words entered by user in the same order & avoiding duplicates:" if word_l else "No words entered."
print(statement)

# To keep track of seen words (Python set(), n.d.)
seen_words = set()

for wordd in word_l:
    # To check if word exists in seen_words.
    if wordd not in seen_words:
        print(wordd)
        # seen_words is a set used to store unique words entered by the user.
        seen_words.add(wordd)

