# Question -3
# Python uses the # character to mark the beginning of a comment. The comment endsvat the end
# of the line containing the # character.
# In this exercise, you will create a program that removes all of the comments from a Python source file:
# • Check each line in the file to determine if a # character is present.
# • If it is then your program should remove all of the characters from the # character to the
# end of the line (we’ll ignore the situation where the comment character occurs inside of a string).
# • Save the modified file using a new name that will be entered by the user.
# • The user will also enter the name of the input file.
# • Ensure that an appropriate error message is displayed if a problem is encountered while accessing the files.


# function to remove commented lines from the file
def remove_comments(input_file, output_file):
    try:
        with open(input_file, 'r') as input_file:
            with open(output_file, 'w') as output_file:
                for line in input_file:
                    # Check if '#' is present in the line
                    if '#' in line:
                        pos = line.rfind('#')  # find the position of the comment character
                        # check if the comment character is in string or not
                        # if it is in string then write the whole line as it is
                        if (line[pos-1] and line[pos+1] == '\"') or (line[pos-1] and line[pos+1] == '\''):
                            output_file.write(line)
                            continue
                        # Remove everything from '#' to the end of the line
                        line = line.split('#', 1)[0]
                    if len(line) > 0:
                        line = line.rstrip('\n')
                        output_file.write(line+'\n')
        print("Comments removed and saved to", output_file)
    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print("An error occurred:", str(e))


# Take input and output filename from the user
input_file_name = input("Enter the name of the input file: ")
output_file_name = input("Enter the name of the output file: ")

# call the function
remove_comments(input_file_name, output_file_name)

