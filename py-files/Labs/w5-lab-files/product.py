'''
Week 5- Classes - 2 of 3 files

--product.py--
'''

class Product:

    def __init__(self, n:str, d:str, s:int):
        self.name=n
        self.description=d
        self.stock=s

# pa(print all) is default parameter when printing, below, to just print everything
    def print(self):
        print("Product name is: ", self.name)
        print("Product Description is: ", self.description)
        print("Stock number is: ", self.stock)
        print("----------")


