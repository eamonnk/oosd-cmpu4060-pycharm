from zoo import Zoo
from animal import Animal
import csv

# myanimal = Animal('cat', 'fred', 9, 10)
# myanimal.print()


# adata= [
#     ['panda','Alford',8,646.48],
#     ['zebra','Marlow',3,373.15],
#     ['monkey','Filippa',4,250.85],
# ]
adata= []

#****************step 2**********
# myanimals=Zoo(adata)
# #myanimals.display_info()
# myanimals.print_animal_list()
# Create an Instance of Zoo called my zoo, then call the add_csv_to_list method within that instance

#**************** step 3*************
myzoo = Zoo(adata)
#myzoo.add_csv_to_list('G:\\GG\\oosd-cmpu4060-pycharm\\py-files\\week 9\\assignment\\animals.csv')
# #myzoo.add_csv_to_list("animals.csv")
# myzoo.print_animals()

# ************step 4 *****************
# import numpy as np


myzoo.compile_transfer_list('G:\\GG\\oosd-cmpu4060-pycharm\\py-files\\week 9\\assignment\\animals.csv')

# lst = [ 1, 2, 3, 4, 5]
# arr = np.array(lst)
# # with numpy can do stats work
# print(lst)
# print(arr + 3)
# print(arr.mean())
# print(arr.std())
# print(arr.sum())