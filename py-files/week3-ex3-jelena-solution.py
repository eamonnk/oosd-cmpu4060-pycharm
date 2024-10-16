# jelena solution to Week 3 - Ex 3

#split it in the line rather than do separate line
itemArr =input("Please enter a list of 5 items to be rated, separated by spaces: ").split()
print("-----------------------")
print("item ids:")
print(1, itemArr[0])
print(2, itemArr[1])
print(3, itemArr[2])
print(4, itemArr[3])
print(5, itemArr[4])
print("-----------------------")

#split in place
myPrefArr=input("Please enter the item ids in order of your preference for the items, separated by spaces: ").split(" ")
friendPrefArr=input("Please enter the item ids in order of your preference for the items, separated by spaces: ").split(" ")
print(myPrefArr, friendPrefArr)

# lambda function as done by jelena for ex 3
myPrefItems = list(map(lambda pref: itemArr[int(pref) - 1], myPrefArr))
print("The items ordered by your preference : " + ' '.join(myPrefItems))
print(map(lambda pref: itemArr[int(pref) - 1], myPrefArr))