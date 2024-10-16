theWord = input("Please enter a word: ")
wordLength = len(theWord)
index = 0
while index  < wordLength:
   c = theWord[index]
   print("{0}[{1}]".format(c, ord(c)))
   index += 1