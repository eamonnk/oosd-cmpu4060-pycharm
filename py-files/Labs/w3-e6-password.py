password='password'

pwd_attempt=input("Please enter your password: ")

tries=1

while tries <= 3:
    if pwd_attempt == password:
        print("Thanks. You are logged in now. ")
        exit()

    elif pwd_attempt != password:
        pwd_attempt=input("The password you entered is not correct. Please enter the password: ")
        tries+=1

if tries > 3:
    print("You have entered an incorrect password too many times. Please contact the administrator. ")
    exit()
