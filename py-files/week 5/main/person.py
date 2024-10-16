from datetime import datetime
from address import Address
from education import Education


class Person:

    def __init__(self, n, s, a, y, m, d, tmt=''):
        self.name = n
        self.surname = s
        self.address = a
        self.dob = datetime(y, m, d)
        self.teamMemberType = tmt
        #  self.rit?

    def print(self):
        print("name is: ", self.name)
        print("surname is: ", self.surname)
        self.address.print()
        print("dob is: ", self.dob.strftime("%d/%m/%Y"))
        print("team member Type is: ", self.teamMemberType)

    def get_age(self):
        date_diff = datetime.now() - self.dob
        return round(date_diff.days/365.25)


# p1 = Person("Bob", "Builder", Address("1", "Site", "Btown", "BB", "XYZ123"), 2000, 1, 1)
# p1.print()
# print("Bob's age: ", p1.get_age())
# print("")
# p2 = Person("Annie", "Apple", Address("2", "The Orchard", "Atown", "AA", "ABC789"), 2010, 1, 2)
# p2.print()
# print("Annie's age: ", p2.get_age())

