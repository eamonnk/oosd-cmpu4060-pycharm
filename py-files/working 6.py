a_string = "hohoho"
an_int = 12345
a_list = ["hello", 4, a_string, 5.6, "a", an_int, True]
type(a_list)
empty_list = []
listWithListElement = ["hi", ["Jane", "Doe", 21], True, 55.3]

# ---operations that do not chnage the list object

["a", "b"] + ['c', 'd']
['1', '2'] * 3

a_string = "hohoho"
an_int = 12345
a_list = ["hello", 4, a_string, 5.6, "a", an_int, True]
a_list + ['additional string']
# check if a_list has changed
a_list


laugh = "hohoho"
letters = ["a", "b", 'c']
a_list = ["hello", 4, letters, 5.6, "a", laugh, True]
a_list
a_list[0]
a_list[2:5]
a_list[5:]
a_list[:-5]

# accessing element in sublist
a_list[2][1]

# accessing substring in string element
a_list[5][:2]

----
myList = ["hello", "hi", 5, "how are you"]
myList
myList[2] = "bonjour"
myList

myList = ["hello", "hi", 5, "how are you"]
myList
myList[2:3] = ["bonjour", "hola"]
myList
myList[-1:] = ["good day"]
myList

# -----
names = ['ben', 'con', 'don', 'ann']
names
names.sort()
# names has changed in place
names

# now try using sorted() to preserve the original list
games = ['scrabble', 'ludo', 'monopoly', 'carcasonne']
games
sorted(games)
# check games again (should not have changed)
games
-----
# try to sort a list with types that cannot be compared
mixed_list = ['abcd', 34, '', 'aaa', 0, 4, 0.0]
mixed_list.sort() # error!
# however if all types can be compared:
another_mixed_list = [2, True, 0.2]
another_mixed_list.sort
# True compared as 1 and the sort works
another_mixed_list


------
# use the bool() casting function as key
#-------------------
mixed_list = ['abcd', 34, '', 'aaa', 0, 4, 0.0]
mixed_list.sort() # error
# pass key to convert to boolean
mixed_list.sort(key=bool)
# elements that equate to False are listed first
mixed_list

# use the len() function as key
#-------------------
word_list = ['hello', 'hi', 'how are you']
word_list
word_list.sort(key=len)
# words are sorted by length
word_list

sorted(word_list)
# use a lambda expression as key
#-------------------
# some names
names = ["ben", "Con", "ann", "Dan"]
# try to sort them
names.sort()
# order is not alphabetical because
# because some names are capitalised;
# we use a lambda expression to
# convert to all-lower before sorting
names.sort(key=lambda n : n.lower())


------

list1 = ['abc', 123, 1.23, True]
list2 = list1
list1
list2

# check it is the same list
list1[1] = 456
list1
list2

---need a new copy. makr a proper copy
list1 = ['abc', 123, 1.23, True]
list2 = list1[:]
list3 = list1.copy()

# check copies are different lists
list2.append('newEl')
list3.remove('abc')
list1
list2
list3

--- deep copy is a copy where valeus at next level if are any lists pointed to byb the list,
--- deep copy >> copy everything the whole tree
-- a shallow copy

-- remember
-- to getc a proper copy of a list you need to do something special... can't just dpo list 1 = list 2'