from operator import truediv

f1 = lambda  x : x > 3
f1(2) -- is false
f1(4) -- is true



f1 = lambda  x, y:xy

----
 some names
names = ["ben", "con", "ann", "dan"]
# define a lambda expression that returns the
# index in the list 'names' for the given string value
get_index_for_name = lambda nm : names.index(nm)
# use it
get_index_for_name('ann')
get_index_for_name('ben')

# some scores
scores = [23, 67, 34, 12]
# define a lambda expression that returns the
# value in the list 'scores' corresponding by position
# to the given value in the list 'names'
get_score_for_person = lambda nm : scores[names.index(nm)]
get_score_for_person("ben")
get_score_for_person("dan")

# sort the name list by scores, using
# sorted(), which does not modify the list;
# we need the original list intact as
# it is being used in the lambda expression
sorted(names, key=get_score_for_person)
# or
sorted(names, key=lambda n : scores[names.index(n)]

sorted(names, key=(lambda x: x[2]))
sorted(names)

getlower=(lambda s: s.lower())
sorted(names, key=getlower)

xs=['xxxx', 'x', 'xxx', 'xx']

xss=['aaaa', 'd', 'bbb', 'cc']
sorted(xss, key=len)

----example for darts scores---
scores = [17, 18, 22, 6]
sorted(names, key=(lambda nm: scores[names.index(nm)] ))

sorted(names, key=(lambda nm: scores[names.index(nm)] ),reverse=True)

--question---
wheree is nm being defined
nm is a placeholder nm is just any name could ahve calle dit xsits a placeholder for input

f= lambda x: put_into_toaster(x)
f = lanbda x: x+2

x is placeholder of thing that will go in but we don't know yet what it is' thats going in
f is not a value its a behaviour

--run this....
f = lambda x, y: x+y+2
f(1, 2)

