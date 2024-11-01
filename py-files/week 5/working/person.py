from datetime import datetime
from address import Address

class Person:

    def __init__(self, n, s, a, y, m, d, r):
        self.name=n
        self.surname=s
        self.address=a
        self.dob=datetime(y, m, d)
        self.rit=r

    def print(self):
        print("name is: ", self.name)
        print("surname is: ", self.surname)
        self.address.print()
        print("dob modified is: ", self.dob.strftime("%d/%m/%Y"))
        print("role in team: ", self.rit)

    def get_age(self):
        date_diff=datetime.now() - self.dob
        return round(date_diff.days/365.25)


#
# p1=Person("Bob", "Builder", Address("1", "site", "Btown", "BB", "BBB9897"), 2000, 1, 1,)
# p1.print()
# print("Bobs age is: ", p1.get_age())
# print(" ")
# p2=Person("annie", "apple", Address("2", "site", "Atown", "CC", "CCC123"),1973, 9, 17)
# p2.print()
# print("Annie's age is: ", p2.get_age())