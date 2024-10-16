'''
Week 3- EX 2 - Dividing
'''

# prompt for integer input from user and store them as integers
x_int_1=int(input("Please enter an integer value: "))
y_int_2=int((input("Please enter another integer value: ")))

# insert into an if statement that if it is equal zero it is a factor else print its nto a factor
if x_int_1 % y_int_2 == 0:
    print (str(y_int_2) + " is a factor of " + str(x_int_1))
else:
    print (str(y_int_2) + " is not not a factor of " + str(x_int_1))
