from animal import Animal
import csv
import random

class Zoo:
    
    # empty constructor, the definitions are all in animal class and the zoo class has methods to manipulate and interact with 
    # objects from animal class

    def __init__(self, adata):
        self.animaldata=adata
        self.animal_list=[]
        self.animal_list= list(map(lambda data: Animal(data[0], data[1], data[2], data[3]), adata))
        print("You have successfully added data to the animal list")
        print(self.animal_list)


        # animal_list=[]
        # animal_list = list(map(lambda a: a ()))

    # def display_info(self):
    #     return f"Name: {self.name}, Species: {self.species}, Age: {self.age}, Habitat: {self.weight}"

    def print_animal_list(self):
        for animal in self.animal_list:
            #print(animal.display_info())
            #print(" Here are the animals {} , {} ,  {} ,  {} ".format(self.species, self.name, self.age, self.weight))
            print(" Here are the animals {} , {} ,  {} ,  {} ".format(animal.species, animal.name, animal.age, animal.weight))

# requires input argument "filename" (fn). we create an empty list in which we will store the animal data
# then use the 'with' statement to open the read the csv file. we use this as ir does tno need close the file after 
# we are finished with it, so is more efficient.
# we use a lambda fn to strip() (remove double quote and new line characters
# and split each str whenever there is a comma rem
    def add_csv_to_list(self, fn):
        self.filename=fn
        animal_list=[]
        with open(self.filename, 'r') as file:
            for line in file:
                animal_list.append(list(map(lambda s: s.strip('"\n'), line.split(","))))
                
        # we print out the list entries here, just to demonstrate it exists and contains entries
        print("********Entries contained in newly created list  >> '[animal_list]'************")
        for i, animal in enumerate(animal_list, 1):
            print("----animal {} --- details >> {}".format(i, animal))
  

        
        
        # for animal in animal_list:
        #     print("----animal {}".format(range(1, 200, 1)))
        #     print(animal)
        

# compile tranfser list 
    def compile_transfer_list(self, fn):
        self.filename=fn
        
        # generate 10 random numbers between 0 and 200 and put in list. 
        # We will use these 10 random numbers to select animals from animals list to place on transfer list
        random_list_num= []
        for i in range (0, 10):
            x=random.randint(0, 200)
            random_list_num.append(x)
            print(x)
        print(random_list_num)
        print(type(random_list_num[1]))
       
        # use 'with' statement to open and read csv and put all 200 animals in a nested list.
        # we could use earlier method, but will leave this here so we can complete all in one method call
        interim_animal_list= []
        with open(self.filename, 'r') as file:
            for line in file:
                interim_animal_list.append(list(map(lambda s: s.strip('"\n'), line.split(","))))
        
        print("********Entries contained in newly created list  >> '[animal_list]'************")
        for i, animal in enumerate(interim_animal_list, 1):
            print("----animal {} --- details >> {}".format(i, animal))
        
        # create the transfer list and populate it with animals that correspond to the random numbers in the
        # append each item to the transfer list in for loop, and subtract -1 as animal list index starts at 0.
        transfer_list=[]
        for num in random_list_num:
            transfer_list.append(interim_animal_list[num -1])
        
        print("******** Step 3 -- transfer list'************")
        for i, animal in enumerate(transfer_list, 1):
            print("----animal {} --- details >> {}".format(i, animal))
            
        # copy that list into a transfer.csv
        
        
        # with open("transfer.csv", "w") as csvfile:
        #         csv.writer = csv.writer(transfer.csv, delimiter=',')
        #         for item in transfer_list:
        #             csv.writer.writerows(item)

                 

           
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