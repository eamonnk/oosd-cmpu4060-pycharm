
x_int_1=int(input("Please enter an integer value: "))
y_int_2=int((input("Please enter another integer value: ")))

mod=x_int_1 % y_int_2

if mod == 0:
    print (str(y_int_2) + " is a factor of " + str(x_int_1))
else:
    print (str(y_int_2) + " is not not a factor of " + str(x_int_1))
