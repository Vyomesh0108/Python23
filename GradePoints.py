# Question 1:

# In this exercise you will compute the grade point average of an arbitrary number of letter grades entered by the user.
# The user will enter blank line to indicate that all of the grades have been provided.
# For example, if the user enter A, followed by C+, followed by B, followed by blank line then your program should report
# a grade point average of 3.1
# Your program needs to do error checking: Each value entered by the user must always be a valid letter grade or a blank line.

# Map alphabetical grades to respective points/mathematical values using dictionary
grade_points = {
    'A+': 4.0,
    'A': 4.0,
    'A-': 3.7,
    'B+': 3.3,
    'B': 3.0,
    'B-': 2.7,
    'C+': 2.3,
    'C': 2.0,
    'C-': 1.7,
    'D+': 1.3,
    'D': 1.0,
    'F': 0.0
}
sum_of_grade_points = 0.0
total_courses = 0

while 1:
    grade_letter = input("Enter grade letter to calculate average or leave it blank: ").upper()
    # The upper function is used to change the input value to uppercase so that it maps to the dictionary keys
    if grade_letter == '':
        break
    elif grade_letter in grade_points:
        sum_of_grade_points += grade_points[grade_letter]
        total_courses += 1
    else:
        print("Please enter a valid grade letter point")

if total_courses > 0:
    average = sum_of_grade_points/total_courses
    print("\n")
    print("The average score is %.2f " % average)
else:
    print("Invalid data")


# OR

def letter_to_gpa(letter_grade):  # (User-Defined Functions, n.d.)
    grades = {
        'A': 4.0, 'A-': 3.7, 'B+': 3.3, 'B': 3.0, 'B-': 2.7,
        'C+': 2.3, 'C': 2.0, 'C-': 1.7, 'D+': 1.3, 'D': 1.0, 'D-': 0.7, 'F': 0.0
    }
    # 'None' is used as a default return value when the input letter
    # grade is not found in the 'grades' dictionary.
    return grades.get(letter_grade.upper(), None)

# Compute GPA from user input
total_gpa = 0.0
count = 0

while True:
    grade = input("Enter a letter grade (or press Enter to calculate GPA): ")

    if not grade:  # If the user enters a blank line, calculate GPA and exit loop
        if count > 0:
            gpa = total_gpa / count
            print(f"Grade Point Average (GPA): {gpa:.2f}")  # Usage of f'string
        else:
            # Printing a message to enter a valid grade.
            print("Please enter at-least one valid grade to calculate GPA.")
        break

    gpa_value = letter_to_gpa(grade)
    if gpa_value is not None:
        total_gpa += gpa_value  # usage of compound assignment operator
        count += 1
    else:
        # Printing a message to enter valid grades among the given.
        print("Invalid grade. Please enter a valid grade (A, A-, B+, B, B-, C+, C, C-, D+, D, D-, F).")




