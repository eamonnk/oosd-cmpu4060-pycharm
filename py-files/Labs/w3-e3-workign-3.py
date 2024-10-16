# Define a list of ranges
marks_range = [range(80, 100),  range(70, 79), range(60, 69), range(55, 59),
           range(50, 54), range(40, 49), range(35, 39), range(1, 34)]

grades=['A', 'B+', 'B', 'B-', 'C+', 'C', 'D', 'F']
marks_and_grades=tuple((zip(marks_range, grades)))
print(marks_and_grades)
print(type(marks_and_grades))
list(enumerate(marks_and_grades))

# Take an integer input from the user (e.g., their score)
user_input = int(input("Enter an integer (score): "))

# Variables to store the matched range and corresponding grade
matched_range = None
matched_grade = None

# Iterate through the tuple and check if the input is in any of the ranges
for idx, (index, (r, grade)) in enumerate(marks_and_grades):
    if user_input in r:
        matched_range = r
        matched_grade = grade
        print(f"{user_input} is in range {r} (grade: {grade})")
        break  # Exit loop once the grade is found

# If no matching range is found
if matched_range is None:
    print(f"{user_input} does not fall within any of the specified ranges.")
else:
    # Output the corresponding grade
    print(f"Matched range: {matched_range}")
    print(f"Corresponding grade: {matched_grade}")
