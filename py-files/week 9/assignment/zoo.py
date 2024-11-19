from animal import Animal
import csv
import random

class Zoo:
    
    # empty constructor, the definitions are all in animal class and the zoo class has methods to manipulate and interact with 
    # objects from animal class

    def __init__(self, adata):
        self.animal_list=[]
        self.animal_list= list(map(lambda data: Animal(data[0], data[1], data[2], data[3], adata)))
        print("You have successfully added data to the animal list")

        # animal_list=[]
        # animal_list = list(map(lambda a: a ()))

    def add_csv_to_list(self, fn):
        self.filename=fn
        animal_list=[]
        with open(self.filename, 'r') as file:
            for line in file:
                animal_list.append(list(map(lambda s: s.strip('"\n'), line.split(","))))
    
        print(animal_list)

    def compile_transfer_list(self, fn):
        self.filename=fn
        
        # generate 10 random numbers between 0 and 200 and put in list. 
        # We will use these 10random numbers to select animals from animals.csv source to tranfers
        random_list_num= []
        for i in range (0, 10):
            x=random.randint(0, 200)
            random_list_num.append(x)
            print(x)
        print(random_list_num)
        print(type(andom_list_num[1]))
       
        # use with statement to open and read csv and put all 200 animals in a nested list.
        interim_transfer_list= []
        with open(self.filename, 'r') as file:
            for line in file:
                transfer_list.append(list(map(lambda s: s.strip('"\n'), line.split(","))))
            print(interim_transfer_list)
            
        # # use num in random num list to select items froim nested list and put in a new list, a final _trasnfer list
        # final_transfer_list=[]
        #     for num in random_list_num:
            
        
        
                
                
        
        


    def print_animals(self):
        print()


# csvReader = csv.reader(personFile, delimiter=",")
# for row in csvReader:
#     print(row)
        # personFile = open("animal.csv")
        # csvReader = csv.reader(personFile, delimiter=",")
        # for row in csvReader:
        #     print(row)