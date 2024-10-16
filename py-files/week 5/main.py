from address import Address
from person import Person
from team import Team

DATA = [
["Annie", "Apple", "2", "The Orchard", "Atown", "AA", "ABC231", 2010, 1, 2],
["Bob", "Builder", "1", "Site", "Btown", "BB", "XYZ", 200, 1, 1],
["Charlie", "Chime", "5", "The Hill", "Ctown", "CC", "MNO000", 1990, 3, 3],
]

map(lambda pl: Person(*pl[:2], Address(*pl[2:7], *pl[7:]), DATA)
team = Team(list((map(lambda pl: Person(*pl[:2], Address(*pl[2:7], *pl[7:]), DATA)))
team.print()