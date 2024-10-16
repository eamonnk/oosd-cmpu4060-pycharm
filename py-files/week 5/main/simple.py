
class Simple:
    def __init__(self):


    def print(selfself):


    def zget(self):
        print("z has been accessed!")
        return self._z

    def zset(self, V:)
        print("z has been set!")
        self._z = v

    def zdel(self):
        print("z has been deleted!")
        del self._z

    z=property(zget, zset, zdel)

s = Simple()
s.print()
s.z = "hello"
s.print()
print(s.z)
del s.z
# s.print() >> will getan error if ru it as z has been deleted