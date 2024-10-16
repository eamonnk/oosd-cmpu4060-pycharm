'''
cellWidth = 6
columnCount = 3
rowCount = 7
for rowNum in range(1, rowCount + 1):
    for colNum in range(1, columnCount + 1):
        print(("r" + str(rowNum) + "c" + str(colNum)).center(cellWidth, " "), end="")
    print("")
'''
def add_number(a, b):
    print(a+b)


def add_number2(a, b):
    return(a+b)

add_number(1, 4)

add_number2(5, 7)