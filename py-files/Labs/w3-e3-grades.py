'''
Week 3- EX 2 - Dividing
'''
per_mark=int(input("Please enter your percentage mark value: "))

# if statement to check if score is outside the acceptable range
# if so to inform the user and ask them to run the program again
# then a series of statements to match the inputted score to a range and
# print out the corresponding grade.
if per_mark < 0 or per_mark > 100:
    print(" Your percentage mark value is invalid,\n Please run the program again to enter a valid mark between 0 and 100 ")

elif per_mark >= 80 <=100:
    print("You received a Grade A ")

elif per_mark >= 70 <=79:
    print("You received a Grade B+ ")

elif per_mark >= 60 <=69:
    print("You received a Grade B")

elif per_mark >= 55 <= 59:
    print("You received a Grade B- ")

elif per_mark >= 50 <= 54:
    print("You received a Grade C+")

elif per_mark >= 40 <= 49:
    print("You received a Grade C")

elif per_mark >= 35 <= 39:
    print("You received a Grade D")

elif per_mark >= 0 <= 34:
    print("You received a Grade F")