# Question -1
# Create a program that determines and displays the number of unique characters in a string entered by the user.
# For example, Hello, World! has 10 unique characters while zzz has only one unique character.
# * Use a dictionary or set to solve this problem.
# * Define a function

# Created an 'unique_char' function with 'user_string' as an argument
def unique_char(user_str):

    # Created empty set to store the unique characters
    char_set = set()

    # For each character in string
    for ch in user_str:
        # Add each unique character in the set() which I created above
        char_set.add(ch)
    # Returns the length of the set() which contains unique characters
    return len(char_set)


# Taken string as an input from user.
user_string = input("Enter a String: ")

# Call the function
result = unique_char(user_string)
# Prints the total number of unique characters from the string entered by user
print(f'Total number of unique characters in {user_string} is {result}')
