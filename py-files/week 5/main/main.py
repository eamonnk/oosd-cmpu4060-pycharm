from address import Address
from person import Person
from team import Team
from education import Education

DATA = [
    ["Annie", "Apple", "2", "The Orchard", "Atown", "AA", "ABC789", 2010, 1, 2, "UCA", "Degree", "Dev"],
    ["Bob", "Builder", "1", "Site", "Btown", "BB", "XYZ123", 2000, 1, 1, "UCD", "Degree", "Dev"],
    ["Charlie", "Chime", "5", "The Hill", "Ctown", "CC", "MNO000", 1990, 3, 3, "UCC", "Degree", "Ops"],
    ["Dave", "Dobbins", "7", "The walls", "Dtown", "DD", "JKF467", 1984, 4, 4, "UCG", "Phd", "Lead"],
]

team = Team(list(map(lambda pl: Person(*pl[:2], Address(*pl[2:7]), Education(*pl[10:]), [*pl[7:9]) [(DATA)))
team.print()

print("----------------------------------------")
# team.remove_member("Bob")
# team.print()
team.print(lead)
team.print(dev)
team.print(ops)


