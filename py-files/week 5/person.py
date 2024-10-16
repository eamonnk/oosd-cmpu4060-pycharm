from person import Person
from address import Address

class Team:
    def __init__(self, tm):
        self.teamMembers = tm

    def add_member(self, p):
        self.teamMemebrs.append(p)

    def remove_member(self, name):
        index = list(map(lambda tm: tm.name, self.teamMembers)).index(name)
        self.teamMembers.pop(index)

    def print(self):
        for index, tm in enumerate (self.teamMembers):
            print("[{}]". format(index +1))
            tm.print()

team = Team()
team.add_member(Person("Bob", "Builder", Address("1", "Site", "Btown", "BB", "XYZ"), 200, 1, 1))
team.add_member(Person("Annie", "Apple", Address("2", "The Orchard", "Atown", "AA", "ABC231"), 2010, 1, 2))
print("Whole team")
team.print()

print("\n")
team.remove_member("Bob")
print("After BOb has left")
team.print()