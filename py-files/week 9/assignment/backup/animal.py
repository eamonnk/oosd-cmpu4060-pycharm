class Animal:

    def __init__(self, s, n, a, w):
        self.species=s
        self.name=n
        self.age=a
        self.weight=w

# created a print method #to use during testing.
    def print(self):
        print("The animal is a {} , its name is {} , they are  {} yrs old , and weigh {} kg. ".format(self.species.upper(), self.name.upper(), self.age, self.weight))
        