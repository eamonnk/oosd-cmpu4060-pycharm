# do not write code like this below
def write_message_to_supplier(height, age):
    if height > 180 and age > 18:
        print("This person needs a dark tshirt and size large")
    if height <= 180 and height > 150 and age < 18:
        print("This person needs a dark tshirt and size medium")
    if height <= 150 and age < 18:
        print("This person needs a dark tshirt and size small")

#do like the below--- use else!!
# 6 conditions but onyl two variables ==>> can do in two cecks, not 6!

def def write_message_to_supplier(height, age):
    if height > 180:
        size ="Large"
    elif heoght > 150:
        size = "Medium"
    else
        size ="Small"
    if age > 18:
        person=adult
        top="dark"
    else:
        person=youth
        top="bright"

    print("This person needs a {} t-shirt, size{}".format(colour, size))