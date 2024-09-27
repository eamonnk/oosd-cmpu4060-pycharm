print("J".lower =="j".lower)

# name1 = "Jane"
# name2 = "Jack"
# pres = name1 == name2
# res = name1 < name2

"." < ":"

# look up operator precedence in python >>

name = "Charlie"
name[3] # calls a letter fromthe for string
name[2:3] # include 2 but don't include 3
name[2,7]
name[2:]
name[:3].upper()
name[:3].lower() + name[5]

name = "Charlie"
# these are equivalent to the first 5 expressions in [CS-5]
name[-7] # can usd negatrive indices - 7 minus 7 same as [0]
name[-4]
name[-5:-3]
name[-3:]
name[:-4]


# Immutability
name = "Johnathan"
shorter = name.replace("natha", "")
name
shorter

everythime you use a method think what is it doing >>> strings are immutable!