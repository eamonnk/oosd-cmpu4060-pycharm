import random
import string
from collections import deque
#random.choice(string.ascii_letters)

### source
#  https://stackoverflow.com/questions/2823316/generate-a-random-letter-in-python
#d = ''.join(chr(random.randrange(97,97+26)) for i in range(10))

ru_flag=0
while status <3:
    dran= deque (''.join(chr(random.randrange(97,97+26)) for i in range(10)))
    print(len(dran))
    print()
    ru_flag+=1
    