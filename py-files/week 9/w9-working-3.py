# import csv

# personFile = open("G:\\GG\\oosd-cmpu4060-pycharm\\py-files\\week 9\\people1.csv")
# csvReader = csv.reader(personFile, delimiter=",")
# for row in csvReader:
#     print(row)
# personFile.close()

with open("G:\\GG\\oosd-cmpu4060-pycharm\\py-files\\week 9\\people2.txt", "r") as file:
    list_of_lists = []

    for line in file:
        list_of_lists.append(list(map(lambda s: s.strip('"\n'), line.split(","))))

print(list_of_lists)



