# import datetime
# also as below import

from datetime import datetime
#import datetime as dt (i.e. short version of name and can use just dt instead of datetime everywhere

from address import Address

class Person:
    pub = "hellp"
    __priv = "go home"

   #if you want somethig private put two underscores in the name

    def __init__(self, n, s, y, m, d):
        self.name = n
        self.surname = s
        self.address = a
        self.dob = datetime(y, m, d)

    def print(self):
        print("name is: ", self.name)
        print("surname is: ", self.surname)
        self.address.print()
        print("dob is: ", self.dob.strftime("%d/%m/%Y"))

def get_age(self):
        dateDiff - datetime.datetime.now()
        return round(dateDiff.days/365.25)


p1 = Person("Bob", "Builder", Address("1", "Site", "Btown", "BB", "XYZ", 200, 1, 1)
p1.print()
print("Bobs age: ", p1.get_age())

p2 = Person("Annie", "Apple", Address("2", "The Orchard", "Atown", "AA", "ABC231"), 2010, 1, 2)
p2.print()
print("Annies age: ", p2.get_age())


print(p2.pub)
print(p2.__priv)