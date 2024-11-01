import random

groceries = [
    ["bread", "A delicious 500g brown loaf.", 1.0, 10],
    ["milk", "A litre carton of low fat milk.", 1.5, 10],
    ["eggs", "10 free range eggs in a cardboard box.", 2.3, 10],
    ["oats", "500g of porridge oats in paper packaging.", 2.2, 10],
    ["nuts", "100g packet of walnuts.", 3.0,8]
]

# items in stock text
divider_line="----------------------------------------"
website_header="Groceries at your Fingertips"
stock_column_headers = ['ID', 'Name', 'Description', 'Price', 'Amount in Stock']
out_of_stock="Out of Stock"
stock_mgmt_option_menu="Stock Management Options"#
items_in_stock="Items in Stock"

# stock mgmt operation index ints and display text strings
add_item_index=1
remove_item_index=2
update_item_index=3
update_stock_index=4
exit_item_index=5
add_item_txt="Add item"
remove_item_txt="Remove item"
update_item_txt="Update item"
update_stock_txt="Update Stock"
exit_item_txt="Exit"
choice_prompt_text="Please choose an option (1, 2, 3, 4 or 5): "

# function to print the website header
def print_header():
    print('{:<40}'.format(divider_line) + '\n'
            + '{:^40}'.format(website_header)  + '\n'
                + '{:<40}'.format(divider_line) + '\n')


# function to print the column headers used in the Items in stock Display
def print_items_in_stock_column_headers():
    print(items_in_stock + '\n' + '{:<40}'.format(divider_line) + '\n')
    print('{:<5}'.format(stock_column_headers[0])
            + '{:<10}'.format(stock_column_headers[1])
                + '{:<50}'.format(stock_column_headers[2])
                    + '{:<10}'.format(stock_column_headers[3])
                        + '{:<10}'.format(stock_column_headers[4]))

# function to print out the stock items and align with headers
# create new global variable which will be the groceries list with an index added.
# It is global variable to make it available elsewhere
# Loop through each groceries sublist in the nested list and add an index
# taken some elements from here https://docs.python.org/3/library/functions.html#enumerate
def print_items_in_stock_menu():
    #create the indexed list based off
    #reset list to null as appending to it, and don't want to append to existing items
    global indexed_groc_list
    indexed_groc_list=[]
    for index, items in list(enumerate(groceries, start=1)):
        indexed_groc_list.append([index] + items)
    # iterate in the item list then to print the items out with index
    for groc_item in indexed_groc_list:
        # Print each element from the sublist
        print('{:<4}'.format(str(groc_item[0])),
                '{:<9}'.format(str(groc_item[1])),
                    '{:<49}'.format(str(groc_item[2])),
                        '{:<9}'.format(str(groc_item[3])),
                            '{:<10}'.format(str(groc_item[4])))

#function to print stock mgmt options menu
def print_stock_mgmt_options_menu():
    print('\n' + '{:<5}'.format(str(stock_mgmt_option_menu)) + '\n' + '{:<40}'.format(divider_line) + '\n')
    print('({:<1}'.format(str(add_item_index))+')' + "     " + '{:<15}'.format(str(add_item_txt)) + '\n'
            + '({:<1}'.format(str(remove_item_index))+')' + "     " + '{:<15}'.format(str(remove_item_txt)) + '\n'
                + '({:<1}'.format(str(update_item_index))+')' + "     " + '{:<15}'.format(str(update_item_txt)) + '\n'
                    + '({:<1}'.format(str(update_stock_index))+')' + "     " + '{:<15}'.format(str(update_stock_txt)) + '\n'
                        + '({:<1}'.format(str(exit_item_index))+')' + "     " + '{:<15}'.format(str(exit_item_txt)) + '\n')


# function to combine all print options into single function to optimize code
def print_all():
    print_header()
    print_items_in_stock_column_headers()
    print_items_in_stock_menu()
    print_stock_mgmt_options_menu()

# function to add an item as per assignment spec
# creates empty list to use to store new item details
# prompt for item name, makes sure new item name is lower case and checks if name already exists in groceries list
# if so displays msg telling user and ends. If not continue and prompts for other item details , adds new details to
# new item list and appends those details to groceries list
def add_item():
    print("please enter the details of the item wish to add")
    add_item_list=[]
    item_found=False
    # if choice == 1:
    add_name=str(input("Name: "))
    for items in groceries:
        if items[0] == add_name.lower():
            print("This item already exists, please use the update item option to modify an existing item:")
            exit()
        else:
            continue
    add_desc=str(input("Description: "))
    add_price = float(input("Price: "))
    add_quantity=int(input("Amount in Stock: "))
    add_item_list = [add_name, add_desc, add_price, add_quantity]
    groceries.append(add_item_list)

# function to remove an item as per assignment spec
# uses index global variable and empties it then iterates thru current groceries items to create a current indexed list.
# prompt users to select item to remove by index and modify the index by -1 to match list number
# confirm the action to delete then remove item from groceries list and re-display gui or take no action and re-display gui
def remove_item():
    indexed_groc_list = []
    for index, items in list(enumerate(groceries, start=1)):
        indexed_groc_list.append([index] + items)
    remove_item_ID=int(input("Please enter the ID of the item you wish to remove: "))
    remove_item_ID -=1
    print("Are you sure you wish to remove the item following item?" + '\n' + '{}'.format(indexed_groc_list[remove_item_ID]))
    confirm_removal=input("Please press \'y\' to confirm or \'n\' to cancel: ")
    if confirm_removal == 'y':
        groceries.remove(groceries[remove_item_ID])
        #print_all()
    else:
        pass
        #print_all()

# function to update an item as per assignment spec
# uses index global variable and empties it then iterates thru current groceries items to create a current indexed list.
# prompts user to select an item based on Index and then enter updates for each item element and updates the element with them.
# runs print all function to re-display the gui
def update_item():
    indexed_groc_list = []
    for index, items in list(enumerate(groceries, start=1)):
        indexed_groc_list.append([index] + items)
    update_item_ID = int(input("Please enter the ID of the item you wish to update: "))
    update_item_ID -= 1
    groceries[update_item_ID][0]= str(input("Please enter updated text for Name: "))
    groceries[update_item_ID][1]= str(input("Please enter updated text for Description: "))
    groceries[update_item_ID][2]= float(input("Please enter updated Price: "))
    groceries[update_item_ID][3]= int(input("Please enter updated amount in Stock: "))
    #print_all()

# function to update stock as per assignment spec
# generates random # in range of zero and current stock number per item
# reduces existing stock count by that random number
# finds items with stock values less than 2 and adds them to a list
# displays items with low stock i.e. < 2 if they exist otherwise displays no low stock message
# prints full menu with updated stock values after user presses key
def update_stock():
    item_stck_reduction_nums=[]
    groc_stock=[]
    for items in range(len(groceries)):
        new_rand_num=random.randint(0, groceries[items][3])
        item_stck_reduction_nums.append(new_rand_num)
    for items in range(len(groceries)):
        groceries[items][-1] -= (item_stck_reduction_nums[items])
    for items in range(len(groceries)):
        if groceries[items][-1] <=2:
            groc_stock.append(groceries[items])
        else:
            pass
    if groc_stock:
        print("The following items have low stock i.e. items with less than 2 in stock. ")
        for items in range(len(groc_stock)):
            print("***  "+ str(groc_stock[items][0])+"  ***")
    else:
        print("There are no items with low stock, i.e. items less than 2 in stock")
    input("Press Enter key to continue and display latest stock information: ")
    print_all()


# logic section where program sequence runs, start by printing gui elements
print_all()
# define and set choice value
choice='0'
# binary state to run while loop or not 1= True/0=False
prog_finished=0
while prog_finished != 1:
    choice=int(input('{:<5}'.format(choice_prompt_text)))
    if choice == 1:
        add_item()
        print_all()
    if  choice == 2:
        remove_item()
        print_all()
    if  choice == 3:
        update_item()
        print_all()
    if  choice == 4:
        update_stock()
    if choice == 5:
        prog_finished = 1
        print("Thank You, Good Bye...")
exit()
