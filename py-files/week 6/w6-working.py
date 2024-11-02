class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):  # 'bark' is a method
        return "Woof!"

    def get_age(self):  # 'get_age' is a method
        return f"{self.name} is {self.age} years old."


# Creating an instance of Dog
my_dog = Dog("Buddy", 7)

# Calling methods
print(my_dog.bark())  # Output: Woof!
print(my_dog.get_age())  # Output: Buddy is 5 years old.
