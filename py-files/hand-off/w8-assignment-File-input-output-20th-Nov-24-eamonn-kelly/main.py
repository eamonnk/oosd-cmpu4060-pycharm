from zoo import Zoo
from animal import Animal
import csv


#*****************************
# You can just click run on t he main.py file. 
# It will rn and provide output in the terminal window
# explanatory text is included in the output in print statements
# If there are any run time issues it may be related to the path to the files
# ensure they are all int hge same folder, check the PYTHONPATH value and ensure files are present
#******************************


# adata_list and adata definitions below are just placeholder definitions we will use
adata_list= [
    ['panda','Alford',8,646.48],
    ['zebra','Marlow',3,373.15],
    ['monkey','Filippa',4,250.85],
]
adata= []

# ********************* STEP 1 - Mockaroo data *******************************
print("----------------------------------------------------------------------------------------------------------------------")
print("----------------------------------START  STEP 1 - Mockaroo data-------------------------------------------------------")
print("----------------------------------------------------------------------------------------------------------------------")
print("a file 'animals.csv' was included in the hand off")
print("This file was created on mockaroo.com")
print("-----------------------------------------End STEP 1-------------------------------------------------------------------")
print("----------------------------------------------------------------------------------------------------------------------")

#**************** STEP 2 - Animal Class Definition and Zoo class objects  list creation**********
print("----------------------------------------------------------------------------------------------------------------------")
print("--------START  STEP 2 - Animal Class Definition and Zoo class objects list creation*----------------------------------")
print("----------------------------------------------------------------------------------------------------------------------")
print("This just demonstrates creation of animal object with attributes as per spec and ability to populate a zoo list with those objects \n we print out the result just as a demonstration it works successfully")
myanimals=Zoo(adata_list)
myanimals.print_animal_list()
print("----------------------------------------------------------------------------------------------------------------------")
print("-----------------------------------------End STEP 2-------------------------------------------------------------------")
print("----------------------------------------------------------------------------------------------------------------------")

#**************** STEP 3 - csv list to animals list *************
print("----------------------------------------------------------------------------------------------------------------------")
print("--------START  STEP 3 - CSV list to animals list----------------------------------")
print("----------------------------------------------------------------------------------------------------------------------")
print("There are 200 animals in animals.csv. Here we create the zoo instance, then call the method 'add_csv_to_list()', specifying a file name. This creates a new list containing animal objects")
print("We print out the full list of 200 animal objects to prove it was successful")
print(">> If a '...filename is not recognised..', or '..no such filename..', error appears ensure you have the animals.csv in the PYTHONPATH, i.e. the folder path where you run the files in the terminal window. All files in the same place. Failing that you can uncomment the line below contain the file path and explicitly point to the animal.csv location in your environment.")
myzoo = Zoo(adata)
myzoo.add_csv_to_list('G:\\GG\\oosd-cmpu4060-pycharm\\py-files\\week 9\\assignment\\animals.csv')
# myzoo.add_csv_to_list("animals.csv")
myzoo.print_animal_list()

print("----------------------------------------------------------------------------------------------------------------------")
print("-----------------------------------------End STEP 3-------------------------------------------------------------------")
print("----------------------------------------------------------------------------------------------------------------------")
# ************step 4 - create animal transfer  list *****************
print("----------------------------------------------------------------------------------------------------------------------")
print("-------------------START  STEP 4 - Compile Transfer List --------------------------------------------------------")
print("----------------------------------------------------------------------------------------------------------------------")
print("We have created a transfer list that contains 10 randomly selected animals form the main animal ist. The transfer list will be printed here.")
print("Also created is a 'transfer.csv' file containing the 10 randomly selected animals form the main animal ist. It is located in the current working directory if you cannot see it. ") 
myzoo = Zoo(adata)
myzoo.compile_transfer_list('G:\\GG\\oosd-cmpu4060-pycharm\\py-files\\week 9\\assignment\\animals.csv')
#myzoo.compile_transfer_list('animals.csv')
print("----------------------------------------------------------------------------------------------------------------------")
print("-----------------------------------------End STEP 4-------------------------------------------------------------------")
print("----------------------------------------------------------------------------------------------------------------------")

# ************** Step 5 - Try / EXcept added *******************
print("----------------------------------------------------------------------------------------------------------------------")
print("-------------------START  STEP 5 - Try / Except --------------------------------------------------------")
print("----------------------------------------------------------------------------------------------------------------------")
print("")
print("we have added try /except constructs to he code as part of our error handling")
print("")

print("----------------------------------------------------------------------------------------------------------------------")
print("-----------------------------------------End STEP 5-------------------------------------------------------------------")
print("----------------------------------------------------------------------------------------------------------------------")
# ************* Step 6 - pounds to Kgs ******************
print("----------------------------------------------------------------------------------------------------------------------")
print("-------------------START  STEP 6 - Weight to Pounds(lbs) or Kgs--------------------------------------------------------")
print("----------------------------------------------------------------------------------------------------------------------")
print("Method which requires a parameter to say whether the data returned for weight should be in lbs or kgs")
print("lbs=True => data is returned in Pounds(lbs)")
print("lbs=False => data is returned in Kgs (this is the default)")
print("We will print a subset of the 'last 10 items' in the list, just to demonstrate the conversion. Full list is too many items and clutters the screen")
print(" You can change the input value to 'True' from 'False' here if you wish, re-run it and view the output in lbs")
myzoo = Zoo(adata)
myzoo.add_csv_to_list('G:\\GG\\oosd-cmpu4060-pycharm\\py-files\\week 9\\assignment\\animals.csv')
#myzoo.add_csv_to_list('animals.csv')
myzoo.print_with_weight_in_lbs(False)

print("----------------------------------------------------------------------------------------------------------------------")
print("-----------------------------------------End STEP 6-------------------------------------------------------------------")
print("----------------------------------------------------------------------------------------------------------------------")

# ************* Step 7 - Mean weight  - pounds or Kgs ******************

print("----------------------------------------------------------------------------------------------------------------------")
print("-------------------START  STEP 7 - Mean weight - in Pounds(lbs) or Kgs--------------------------------------------------------")
print("----------------------------------------------------------------------------------------------------------------------")
print("Method which requires a parameter to say whether the data returned for mean weight should be in lbs or kgs")
print("lbs=True => data is returned in Pounds(lbs)")
print("lbs=False => data is returned in Kgs (this is the default)")
print("You can change the input value to 'True' from 'False' here if you wish, re-run it and view the output in lbs")
myzoo = Zoo(adata)
myzoo.add_csv_to_list('G:\\GG\\oosd-cmpu4060-pycharm\\py-files\\week 9\\assignment\\animals.csv')
# myzoo.add_csv_to_list('animals.csv')
myzoo.mean_weight(False)

print("----------------------------------------------------------------------------------------------------------------------")
print("-----------------------------------------End STEP 7-------------------------------------------------------------------")
print("----------------------------------------------------------------------------------------------------------------------")
