class Car:

    def __init__(self, mk, md, c, ma, o, n=""):
        self.make=mk
        self.model=md
        self.colour=c
        self.maxAcc=ma
        self.owner=o # needs to be of type Person
        self.name=n

    def start(self):
        print("vroom vroom")

    def gas(self):
        print("accelerating at " + self.owner.getName() + "km/hr/sec")

    def change_gear(self):
        print("accelerating at " + str(self.maxAcc) + "km/he/s")

    def stop(self):
        pass

