from address import Address
from person import Person
from team import Team

DATA = [
    ["Annie", "apple", "2", "site", "Atown", "AA", "AAA123",1973, 2, 2, 'dev'],
    ["Bob", "Builder", "1", "site", "Btown", "BB", "BBB9897", 2000, 1, 1, 'ops'],
    ["Charlie", "China", "3", "site", "Ctown", "CC", "CCC123",1990, 3, 3, 'dev'],
    ["Derek", "Downs", "4", "site", "Dtown", "DD", "DDD678",1984, 4, 4, 'lead']
]
#to get first and second name, then
team =[]
Team(list(map(lambda pl: Person(*pl[:2], Address(*pl[2:7]), *pl[7:]), DATA )))
print(team)
print('-----------------------------------')
team.print('lead')
print('-----------------------------------')
team.print('dev')
print('-----------------------------------')
team.print('ops')
print('-----------------------------------')

