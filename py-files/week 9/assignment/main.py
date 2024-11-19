from zoo import Zoo
from animal import Animal
import csv

myanimal = Animal('cat', 'fred', 9, 10)
myanimal.print()


adata= [
    ['panda','Alford',8,646.48],
    ['zebra','Marlow',3,373.15],
    ['monkey','Filippa',4,250.85],
]


myanimals=Zoo(adata)
# Create an Instance of Zoo called my zoo, then call the add_csv_to_list method within that instance

# myzoo = Zoo()
# myzoo.add_csv_to_list('G:\\GG\\oosd-cmpu4060-pycharm\\py-files\\week 9\\assignment\\animals.csv')
# #myzoo.add_csv_to_list("animals.csv")
# myzoo.print_animals()

#
# import numpy as np

# lst = [ 1, 2, 3, 4, 5]
# arr = np.array(lst)
# # with numpy can do stats work
# print(lst)
# print(arr + 3)
# print(arr.mean())
# print(arr.std())
# print(arr.sum())