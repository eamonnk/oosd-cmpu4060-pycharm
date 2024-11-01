class Car:

    classic = False

    def __init(self, make, model, colour, maxAcc, name=""):
        self.make=make
        self.model=model
        self.colour=colour
        self.maxxAcc=maxAcc
        self.name=name

    def start(self):
        print("vroom vroom")

    def gas(self):
        print("acclerating at " + str(self.maxAcc) + "km/hr/sec")

    def change_gear(self):
        pass
    def stop(self):
        pass

amysCar=Car("toyota", "corolla", "red", 7, "mr cool")
bensCar=Car("hyundai", "accent", "red", 7, "mr cool")
bensCar.classic = True

# selfs is the object that was create, all thes einstances are runnginon an object
# that means they need ot acces the data on  that object

print("amy")
amysCar.start()
anysCar.gas
print(amysCar.classic)

print("ben")
bensCar.start()
bensCar.gas()