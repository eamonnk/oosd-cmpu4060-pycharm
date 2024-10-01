# Week 2 - Ex 3 - item reordering

# Prompt user to input their full name with space between them
user_items_str=input("Please enter a list of 5 items to be rated, separated by spaces: ")

print(user_items_str)
type(user_items_str)
user_items_list=user_items_str.split()
print(user_items_list)
type(user_items_list)
item_display=("1 "+ user_items_list[0] + "\n" +
                "2 " + user_items_list[1] + "\n" +
                    "3 " + user_items_list[2] + "\n"
                        +"4 " + user_items_list[3] + "\n"
                            +"5 " + user_items_list[4] + "\n")
print(item_display)
user_pref_str=input("Please enter the item ids in order of your preference for the items, separated by spaces: ")

print(user_pref_str)
type(user_pref_str)

user_pref_list=user_pref_str.split()
print(user_pref_list)
type(user_pref_list)

order_1=("1" in user_pref_list_1)
print(order_1)
sorted(user_pref_list_1, key=lambda ord_num: user_pref_list_1.index(ord_num)

my_pref = [user_items_list[i] for i in user_pref_list]
print(my_pref)

sorted_data = sorted(data, user_pref_list=lambda x: x[1])

mylist = ['apple', 'ball', 'cup', 'donkey', 'egg']
myorder = [3, 2, 0, 1, 4]
mylist = [mylist[i] for i in myorder]

print(mylist) # prints: ['d', 'c', 'a', 'b', 'e']

names = ['jim', 'john', 'jane', 'jen']
print(names)
type(names)
list(map(len, names))
list(map(lambda s : s.upper(), names))


names = ["ben", "con", "ann", "dan"]
# define a lambda expression that returns the
# index in the list 'names' for the given string value
get_index_for_name = lambda nm : names.index(nm)
# use it
get_index_for_name('ann')
get_index_for_name('ben')

user_pref_list_1

first_pref_str=user_pref_list[0]
second_pref_str=user_pref_list[1]
third_pref_str=user_pref_list[2]
fourth_pref_str=user_pref_list[3]
fifth_pref_str=user_pref_list[4]

type(first_pref_str)
print(first_pref_str)
first_pref_int=int(first_pref_str)
second_pref_int=int(second_pref_str)
third_pref_int=int(third_pref_str)
fourth_pref_int=int(fourth_pref_str)
fifth_pref_int=int(fifth_pref_str)

type(first_pref_int)
print("Your preferences were " + "\n"
        + "1st" + " " + user_items_list[(first_pref_int)-1] + "\n"
            +  "2nd" + " " + user_items_list[(second_pref_int)-1] + "\n"
                + "3rd" + " " + user_items_list[(third_pref_int)-1] + "\n"
                    +  "4th" + " " + user_items_list[(fourth_pref_int)-1] + "\n"
                        + "5th" + " " + user_items_list[(fifth_pref_int)-1] + "\n")


get_index_for_order = lambda pref : user_pref_list.index(pref)
first_pref=get_index_for_order('1')
second_pref=get_index_for_order('2')
third_pref=get_index_for_order('3')
fourth_pref=get_index_for_order('4')
fifth_pref=get_index_for_order('5')

print(first_pref)
# jelena solution to Week 3 - Ex 3

#split it in the line rather than do separate line
itemArr =input("Please enter a list of 5 items to be rated, separated by spaces: ").split()
Print("-----------------------")
print("item ids:")
print(1, itemArr[0])
print(2, itemArr[1])
print(3, itemArr[2])
print(4, itemArr[3])
print(5, itemArr[4])
Print("-----------------------")

#split in place
myPrefArr=input("Please enter the item ids in order of your preference for the items, separated by spaces: ").split(" ")
friendPrefArr=input("Please enter the item ids in order of your preference for the items, separated by spaces: ").split(" ")
print(myPrefArr, friendPrefArr)

# lambda function as done by jelena for ex 3
myprefitems = list(map(lambda pref: itemarr[int(pref) - 1, myPrefArr]))