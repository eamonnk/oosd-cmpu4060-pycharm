### sets ####
l = [1, 1, 2, 23, 1, 3, 6, 7, 7, 8, 23, 1, 1, 9, 2, 22, 34]

set(l)
len(set(l))
len(l)
set
s.add(11)
s
s.isdisjoint({1, 100})
s.isdisjoint({99, 100})
s2={1, 1, 1, 3, 4, 5, 5, 7, 8, 9, 9}
s2
s3={[1,2], 1, False, "abc"} # unhashable type: 'list' get error...
s4={"ayz", 1, 3, 'abc'}
s4
########  dictionaries  #####
dictionary = {x: x**2 for x in range(10)}
print(dictionary)

print(list(zip(['one', 'two', 'three'], [1, 2, 3],['a','b','c'])))
print(dict(zip(['one', 'two'], [1, 2])))
d = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
print("d: ", d)
print(d.items())
print(d.keys())

###### deque #####
# how does list do FiFO and LIFO.. fine is using from right.. but takign form left is hardder with list
# taking elements from left or right
# Deque lets you take from Left or Right or Extend to Left or Right
l = [1, 2, 3]
l
l.pop() # --- good for stack as takes from end...
l.insert(0,0)
l.extend([4,5])
