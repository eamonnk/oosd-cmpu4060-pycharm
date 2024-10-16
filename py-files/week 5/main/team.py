from person import Person
from address import Address

class Team:
    def __init__(self, tm=[]):
        self.teamMembers = tm

    def add_member(self, p):
        self.teamMembers.append(p)

    def remove_member(self, name):
        index = list(map(lambda tm: tm.name, self.teamMembers)).index(name)
        self.teamMembers.pop(index)

    def print(self, tr=""):
        list_for_printin = self.teamMembers


        if tr in ['lead', 'dev', 'ops']:
           list_for_printing =  list(filter(lambda tm: tm.rit == tr, self.teamMembers))

        for index, tm in enumerate(list_for_printing):
            print("[{}]".format(index + 1))
            tm.print()


# team = Team()
# team.add_member(Person("Bob", "Builder", Address("1", "Site", "Btown", "BB", "XYZ123"), 2000, 1, 1))
# team.add_member(Person("Annie", "Apple", Address("2", "The Orchard", "Atown", "AA", "ABC789"), 2010, 1, 2))
# print("Whole team: ")
# team.print()
#
# print("\n")
# team.remove_member("Bob")
# print("After Bob has left: ")
# team.print()
