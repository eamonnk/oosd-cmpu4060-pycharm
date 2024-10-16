'''
Week 3- EX 6 - Pasword
'''

# assign string to variable password
password='password'

# read password input from user
pwd_attempt=input("Please enter your password: ")

# set tries value to 1 after first attempt
# this will ber used in while loop to iterate
tries=1

# while the tries is less than 3
# check if password is correct and if not let user know,
# increase tries count and perform while loop again
while tries <= 3:
    if pwd_attempt == password:
        print("Thanks. You are logged in now. ")
        exit()

    elif pwd_attempt != password:
        pwd_attempt=input("The password you entered is not correct. Please enter the password: ")
        tries+=1

# if tries count is greater than 3, let user know
# they have exceeded try limit and ask them top contact the administrator
if tries > 3:
    print("You have entered an incorrect password too many times. Please contact the administrator. ")
    exit()
