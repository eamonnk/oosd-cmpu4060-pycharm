'''
#class Simple:
    x = "a"
    y = "b"

    def print(self):
        print("x is: ", self.x)
        print("y is: ", self.y)



class Simple:
    x = "a"
    y = "b"

    def print(self):
        print("x is: ", self.x)
        print("y is: ", self.y)

a = Simple()
t = Simple()

s.print()
t.print()
'''
# import datetime
# alsoi as below import 

from datetime import datetime
#import datetime as dt (i.e. short version of name and can use just dt instead of datetime everywhere

class Person:
   pub = "hellp"
   __priv = "go home"

   #if you want somethig private put two underscores in the name

def __init__(self, n, s, y, m, d):
       self.name = n
       self.surname = s
       self.dob = datetime.datetime(y, m, d)

def print(self):
        print("name is: ", self.name)
        print("surname is: ", self.surname)
        print("dob is: ", self.dob.strftime("%d/%m/%Y"))

def get_age(self):
       dateDiff - datetime.datetime.now()
       return round(dateDiff.days/365.25)


p1 = Person("Bob", "Builder", 200, 1, 1)
p1.print()
print("Bobs age: ", p1.get_age())

p2 = Person("Annie", "Apple", 2010, 1, 2)
p2.print()
print("Annies age: ", p2.get_age())


print(p2.pub)
print(p2.__priv)
# purpose of constructor is tocreate the object #

'''
import datetime

https://www.w3schools.com/python/python_datetime.asp

class datetime:
    pub = "hellp"
    __priv = "go home"

   #if you want something private put two underscores in the name

    def __init__(self, d, t):
        self.date = d
        self.time = t

    def print(self):
        print("name is: ", self.name)
        print("surname is: ", self.surname)


p1 = Person("Bob", "Builder")
p1.print()

import datetime

t1 = (2014, 25, 12)
t2 = datetime.datetime.now()
t2=t2-t1


import datetime
# d1 = datetime.datetime.now()
# time.sleep(1)
# d2 = datetime.datetime.now() # after a 5-second or so pause
# d2 - d1#
# datetime.timedelta(0, 5, 203000)
# dd = d2 - d1
# print (dd.days) # get days
# print (dd.seconds) # get seconds
# print (dd.microseconds) # get microseconds
# print (int(round(dd.total_seconds()/60, 0))) # get minutes
        '''