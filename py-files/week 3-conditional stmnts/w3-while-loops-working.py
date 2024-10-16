# number = 1
# while number < 11:
# print(1)
# number = number + 1

# import random
# instance=1
# while instance<=10:
#      print(random.randint(1, 12))
#      instance=instance+1

# import random
# IterCount = random.randint(1, 10) while IterCount > 0:
#  print(1)
#  IterCount -= 1



import random
# umber = random.randint(1, 11)
# while number != 11:
#   print(number)
#  number = random.randint(1, 11)

theWord = input("Please enter a word: ")
wordLength = len(theWord)
index = 0
while index < wordLength:
   c = theWord[index]
   print("{0}[{1:b}]".format(c, ord(c)))
   index += 1

