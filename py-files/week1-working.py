exit()
e# or
quit()

print(3)

round(4.3)

help(str)
help(True)
help(help)


Roughly anything of substance, i.e. anything that has a value and a type, is an object in Python. Thus a number or a piece of text is an object, as are more complicated structures with many pieces of individual information.

A function can be associated with a particular type of object and in that case it is called a method. Methods are called with the syntax
<object name or value>.<method_name>()

The example in code snippet [CS-5] is that of the method upper called on an object containing the text "hello". Try it out.
Example of a method (run interactively) [CS-5]

"hello".upper()

"hello".lower()

# generate random number between 1 and 10
random.randint(1, 10) # error!

# the random module must be imported
import random
random.randint(1, 10)

print("Enter some text:")
input()
