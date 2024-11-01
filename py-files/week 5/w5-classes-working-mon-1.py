import datetime

class Person:

    def __init__(self, n, s, y, m, d):
        self.name=n
        self.surname=s
        self.dob=datetime.datetime(y, m, d)

    def print(self):
        print("name is: ", self.name)
        print("surname is: ", self.surname)
        print("dob modified is: ", self.dob.strftime("%d/%m/%Y"))

    def get_age(self):
        date_diff=datetime.datetime.now() - self.dob
        return round(date_diff.days/365.25)



p1=Person("Bob", "Builder", 2000, 1, 1)
p1.print()
print("Bobs age is: ", p1.get_age())

p2=Person("annie", "apple", 1973, 9, 17)
p2.print()
print("Annie's age is: ", p2.get_age())

#t=Simple()
#s.print()
#t.print()
#print("printing s.x from outside: ", s.y)
datetime.datetime.now.strftime("%d/%m/%Y")