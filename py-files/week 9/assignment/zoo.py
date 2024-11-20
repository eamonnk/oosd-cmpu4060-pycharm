from animal import Animal
import csv
import random

class AnimalnotinList(Exception):
    pass

class ValidFileLine(Exception):
    pass

class Zoo:
    
    # objects from animal class
    # assignment spec asks for constructor in zoo class to hold a list of animal objects
    # we define initial animal list init_animal_list here just to craete the objectand allow us print this short a short list to demo functionality
    def __init__(self, adata):
        self.animaldata=adata
        self.animal_list=[]
        self.animal_list= list(map(lambda data: Animal(data[0], data[1], data[2], data[3]), adata))



# print method - uses init_list created earlier in constructor and iterates over the list using enumerate to put an index number over the animal number in our print output 
    def print_animal_list(self):
        # for i, animal in enumerate((self.animal_list), start=1):   
        #     print("----- Animal Number -- {}  -- :  ".format(i))
        #     print(" Species :  {} ".format(animal.species))
        #     print(" Name  :  {} ".format(animal.name))
        #     print(" Age :  {}".format(animal.age))
        #     print(" Weight (Kgs) {} : ".format(animal.weight))
        print("********Animal Objects contained in  >> '[animal_list]'************")
        try:
            for i, animal in enumerate(self.animal_list, 1):
                print("----animal {} --- details >> {}".format(i, (animal.species, animal.name, animal.age, animal.weight)))
        except AnimalnotinList as ae1:
            print("-->> AnimalnotinList exception catch - Animal object not readable or valid - ae1")

# requires input argument "filename" (fn), as per spec. We create an empty list in which we will store the animal data
# then use the 'with' statement to open and read the csv file. we use this as it does tno need close the file after 
# we are finished with it, so is more efficient.
# we use a lambda fn to strip() (remove double quote and new line characters)
# and split() each str whenever there is a comma rem
# animal List here is defined as instance attribute using 'self'. so every other method in zoo class can use it
    def add_csv_to_list(self, fn):
        self.filename=fn
        self.animal_list=[]
        with open(self.filename, 'r') as file:
            next(file)
            try:
                for line in file:
                    species, name, age, weight = map(lambda s: s.strip('"\n'), line.split(","))
                    self.animal_list.append(Animal(species, name, int(age), float(weight)))
            except ValidFileLine as fle1:
                print("-->> ValidFileLine exception catch- File line not readable or valid - fle1")
        # # we print out the list entries here, just to demonstrate it exists and contains entries
        # print("********Entries contained in newly created list  >> '[animal_list]'************")
        # for i, animal in enumerate(self.animal_list, 1):
        #     print("----animal {} --- details >> {}".format(i, (animal.species, animal.name, animal.age, animal.weight)))

        

    # compile tranfser list 
    def compile_transfer_list(self, fn):
        self.filename=fn
        
        # generate 10 random numbers between 0 and 200 and put in list. 
        # We will use these 10 random numbers to select animals from animals list to place on transfer list
        random_list_num= []
        for i in range (0, 10):
            x=random.randint(0, 200)
            random_list_num.append(x)

        # use 'with' statement to open and read csv and put all 200 animals in a nested list.
        # we could use earlier method, but will leave this here so we can complete all in one method call
        interim_animal_list= []
        with open(self.filename, 'r') as file:
            try:
                for line in file:
                    interim_animal_list.append(list(map(lambda s: s.strip('"\n'), line.split(","))))
        
            except ValidFileLine as fle2:
                print("-->> ValidFileLine exception catch- File line not readable or valid - fle2")
        
        # print("********Entries contained in newly created list  >> '[animal_list]'************")
        # for i, animal in enumerate(interim_animal_list, 1):
        #     print("----animal {} --- details >> {}".format(i, animal))
        
        # create the transfer list and populate it with animals that correspond to the random numbers in the
        # append each item to the transfer list in for loop, and subtract -1 as animal list index starts at 0.
        transfer_list=[]
        for num in random_list_num:
            transfer_list.append(interim_animal_list[num -1])
        
        print("******** Step 4 -- Transfer list of 10 randomly selected Animals'************")
        for i, animal in enumerate(transfer_list, 1):
            print("----animal {} --- details >> {}".format(i, animal))
            
        # copy that list into a transfer.csv
        # use 'with' open statement  again to with 'w' tio write to the file. 
        # pass the file obj to csv,writer and write the transfer_list to the transfer.csv file 
        # the 'transfer.csv' is located in the current working directory if you cannot see it.  
        # i.e. the folder listed in the terminal window.
        with open("transfer.csv", "w", newline='') as csvfile:
            csv.writer = csv.writer(csvfile, delimiter=',')
            csv.writer.writerows(transfer_list)
            
        print("")
        print("The 'transfer.csv' file has been created and is available in your current working directory.")
        print("")
        

    # method which requires a parameter to say whether the data returned for weight should be in lbs or kgs
    # lbs=True => data is returned in Pounds(lbs)
    # lbs=False => data is returned in Kgs (this is the default)
    def print_with_weight_in_lbs(self, lbs=False):
        self.pounds=lbs
        # create lists to store lbs and kg data, we will store them as lists
        self.animal_list_weight_kgs=[]
        self.animal_list_weight_lbs=[]
        self.animal_list_weight_kgs_print=[]
        self.animal_list_weight_lbs_print=[]
        
      
        # Print statement for KGs - if pounds is False print animal data by row with weight in KGs
        # Create list of animals objects with weight in KG for any future use requirements
        # print sublist of objects just to demonstrate functionality and success for grading
        # weight is already in Kgs in csv so don't have to do anything to it.
        if not self.pounds:
            self.animal_list_weight_kgs=self.animal_list
            print("")
            print("lbs parameter is False. Printing weight in KGs")
            print("")

            # slicing the last 109 elements off the main list to create a sub list from which we'll print
            self.animal_list_weight_kgs_print=self.animal_list_weight_kgs[-10:]
            #for animal in self.animal_list_weight_kgs_print:
            
            # printing output of last10 animals in list in KGs 
            # printing sublist so gui is not cluttered
            try: 
                for i, animal in enumerate(self.animal_list_weight_kgs_print, start=190):   
                    print("----- Animal Number -- {}  -- weight in Kgs:  ".format(i))
                    print(" Species :  {} ".format(animal.species))
                    print(" Name  :  {} ".format(animal.name))
                    print(" Age :  {}".format(animal.age))
                    print(" Weight (Kgs) {} : ".format(animal.weight))
        
            except AnimalnotinList as ae2:
                print("-->> AnimalnotinList exception catch - Animal object not readable or valid - ae2")
        
        
        # Print statement for LBS - if pounds is True print animal data by row with weight in lbs
        # Create list of animals objects with weight in LBS for any future use requirements
        # print sublist of objects just to demonstrate functionality and success for grading
        # weight is already in Kgs in csv so don't have to do anything to it.
        else:
            try:
                for animal in self.animal_list:
                    weight_lbs = round(animal.weight *2.2, 2)
                    animal_obj_lbs=Animal(animal.species, animal.name, animal.age, weight_lbs)
                    self.animal_list_weight_lbs.append(animal_obj_lbs)
        
            except AnimalnotinList as ae3:
                print("-->> AnimalnotinList exception catch - Animal object not readable or valid - ae3")

            print("")
            print("lbs parameter is True. Printing weight in lbs")
            print("")
            # use slicing to print only last 10 elements of list [-10] as 200 objects clutters the screen
            self.animal_list_weight_lbs_print=self.animal_list_weight_lbs[-10:]
            try:
                for i, animal in enumerate(self.animal_list_weight_lbs_print, start=190):
                    print("----- Animal Number -- {} -- weight in lbs:  ".format(i))
                    print(" Species :  {} ".format(animal.species))
                    print(" Name  :  {} ".format(animal.name))
                    print(" Age :  {}".format(animal.age))
                    print(" Weight (Lbs) :  {} ".format(animal.weight))

            except AnimalnotinList as ae4:
                print("-->> AnimalnotinList exception catch - Animal object not readable or valid - ae4")

    # Mean Weight in Lbs or Kgs
    # we will use an input value to determine if mean weight should be in lbs or kgs
    # lbs=True => data is returned in Pounds(lbs)
    # lbs=False => data is returned in Kgs (this is the default)
    def mean_weight(self, lbs=False):  
        self.mean_pounds=lbs
         
        # define empty lists for just KG weight and just lbs weight
        self.animal_list_weight_only_kgs=[]
        self.animal_list_weight_only_lbs=[]
        
        
         
        # lbs input = False >> ---- mean weight will be calculated in KGs-----
        # mean weight KGs
        # create list of weight value  - floats.
        # as all values are already in KGs we do nto need to convert kgs to anything else. already in Kgs
        mean_weight_kgs=0.0
        mean_weight_lbs=0.0
        # create a list which just contains all the weight values. 'mean_pounds' value is trigger and if False this loop enters and returns Kgs
        if not self.mean_pounds:
            try:
                for animal in self.animal_list:
                    self.animal_list_weight_only_kgs.append(animal.weight)
            # formula to calculate mean weight - use sum() method to total floatvalues in list, then divide by number of items in the list i.e. the length of the list
                mean_weight_kgs = round(sum(self.animal_list_weight_only_kgs) / len(self.animal_list_weight_only_kgs), 2)
            except AnimalnotinList as ae5:
                print("-- Animal not in list exception catch - ae5")
            
            # print statement to print the calculated value
            ("")
            print("")
            print(" The average weight in Kgs for all 200 animals   =  {} Kgs ".format(mean_weight_kgs))
            print("")
            print("")
    
        # lbs input = True >> ---- mean weight will be calculated in LBS-----
        # mean weight LBS
        # 1 pound = 1 KG x 2.2
            if self.mean_pounds:
                try:
                    for animal in self.animal_list:
                        self.animal_list_weight_only_lbs.append(round((animal.weight)* 2.2, 2))
                
                except AnimalnotinList as ae6:
                    print("-- Animal not in list exception catch - ae6")
            # formula to calculate mean weight - use sum() method to total floatvalues in list, then divide by number of items in the list i.e. the length of the list
                mean_weight_lbs = round(sum(self.animal_list_weight_only_lbs) / len(self.animal_list_weight_only_lbs), 2)
            
             # print statement to print the calculated value
                print("")
                print("")
                print(" The average weight in Pounds (lbs) for all 200 animals   =  {} lbs ".format(mean_weight_lbs))
                print("")
                print("")
        
        
        
                
                
        
        


