# Define a list of ranges
marks_range = [range(80, 100),  range(70, 79), range(60, 69), range(55, 59),
           range(50, 54), range(40, 49), range(35, 39), range(1, 34)]

grades=['A', 'B+', 'B', 'B-', 'C+', 'C', 'D', 'F']
marks_and_grades=tuple((zip(marks_range, grades)))
print(marks_and_grades)
print(type(marks_and_grades))
list(enumerate(marks_and_grades))

# Take an integer input from the user
user_mark = int(input("Enter your mark: "))

# Flag to track if the number is found in any range
found = False

# Iterate through the list of ranges with their index
for i, r in enumerate(marks_range):
    if user_mark in r:
        print("{user_mark} is in the range {r} (index {i} in the list).")
        print(f"You achieved a score of " + {i} +
        found = True
        break  # Exit the loop once the number is found

# If the number is not in any of the ranges
if not found:
    print(f"{user_mark} is not within any of the specified ranges.")
