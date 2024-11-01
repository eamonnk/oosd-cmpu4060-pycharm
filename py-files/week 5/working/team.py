from person import Person
from address import Address

class Team:

    def __init__(self, tm=[]):
        self.teamMembers=tm

    def add_member(self, p):
        self.person=p
        self.teamMembers.append(p)

    def remove_member(self, name):
        index=list(map(lambda tm: tm.name, self.teamMembers)).index(name)
        self.teamMembers.pop(index)

# tr is default parameter when printing , below, to just print everything
    def print(self, tr=""):
        list_for_printing = self.teamMembers

        if tr in ['lead', 'ops', 'dev']:
            list_for_printing=list(filter(lambda tm: tm.rit == tr, self.teamMembers))

        for index, tm in enumerate(list_for_printing):
            print("[{}]".format(index +1))
            tm.print()

# # rit = role in team
# # lambda what and afte r: then when do we want it to be filtered
# #   def print(self):
# #        for index, tm in enumerate(self.teamMembers):
# #             print("[{}]".format(index +1))
# #             tm.print()
#
#
# team=Team()
# team.print()
# team.add_member(Person("Bob", "Builder", Address("1", "site", "Btown", "BB", "BBB9897"), 2000, 1, 1,))
# team.add_member(Person("annie", "apple", Address("2", "site", "Atown", "CC", "CCC123"),1973, 9, 17))
# print("  ")
# print(" Whole Team ")
# team.print()
#
# team.remove_member("Bob")
# print(" After Bob has left")
# team.print()