from colorsys import yiq_to_rgb

groceries = [
    ["bread", "A delicious 500g brown loaf.", 1.0, 10],
    ["milk", "A litre carton of low fat milk.", 1.5, 10],
    ["eggs", "10 free range eggs in a cardboard box.", 2.3, 10],
    ["oats", "500g of porridge oats in paper packaging.", 2.2, 10],
    ["nuts", "100g packet of walnuts.", 3.0,8]
]

indexed_groc_list = []

# items in stock text
divider_line="----------------------------------------"
website_header="Groceries at your Fingertips"
stock_column_headers = ['ID', 'Name', 'Description', 'Price', 'In Stock']
out_of_stock="Out of Stock"
stock_mgmt_option_menu="Stock Management Options"

# stock mgmt operation index ints and display text strings
add_item_index=1
remove_item_index=2
update_item_index=3
update_stock_index=4
exit_item_index=5
add_item_txt=("Add item")
remove_item_txt=("Remove item")
update_item_txt=("Update item")
update_stock_txt=("Update Stock")
exit_item_txt=("Exit")
choice_prompt_text="Please choose an option (1, 2, 3, 4 or 5): "

def print_header():
    print('{:<40}'.format(divider_line) + '\n'
            + '{:^40}'.format(website_header)  + '\n'
                + '{:<40}'.format(divider_line) + '\n')


def print_items_in_stock_column_headers():
    print("Items in stock" + '\n' + '{:<40}'.format(divider_line) + '\n')
    print('{:<5}'.format(stock_column_headers[0])
            + '{:<10}'.format(stock_column_headers[1])
                + '{:<50}'.format(stock_column_headers[2])
                    + '{:<10}'.format(stock_column_headers[3])
                        + '{:<10}'.format(stock_column_headers[4]))

# add an index item at star as missing from item definitions
# Loop through each sublist in the nested list and add an index
# taken from here https://docs.python.org/3/library/functions.html#enumerate
# def generate_index_groc_list():
#     indexed_groc_list=[]
#     for index, items in list(enumerate(groceries, start=1)):
#         indexed_groc_list.append([index] + items)

def print_items_in_stock_menu():
    text=' '
    #create the indexed list?
    #reset list to null as am appending to it, and don't want to append to existing items
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

def print_stock_mgmt_options_menu():
    print('\n' + '{:<5}'.format(str(stock_mgmt_option_menu)) + '\n' + '{:<40}'.format(divider_line) + '\n')
    print('({:<1}'.format(str(add_item_index))+')' + "     " + '{:<15}'.format(str(add_item_txt)) + '\n'
            + '({:<1}'.format(str(remove_item_index))+')' + "     " + '{:<15}'.format(str(remove_item_txt)) + '\n'
                + '({:<1}'.format(str(update_item_index))+')' + "     " + '{:<15}'.format(str(update_item_txt)) + '\n'
                    + '({:<1}'.format(str(update_stock_index))+')' + "     " + '{:<15}'.format(str(update_stock_txt)) + '\n'
                        + '({:<1}'.format(str(exit_item_index))+')' + "     " + '{:<15}'.format(str(exit_item_txt)) + '\n')
    #print(input('{:<5}'.format(choice_prompt_text)))
    #print(sm_choice)
    #print(type(sm_choice))

# function to combine all print options to make it easier to call
def print_all():
    print_header()
    print_items_in_stock_column_headers()
    print_items_in_stock_menu()
    print_stock_mgmt_options_menu()

def add_item():
    print("please enter the details of the item wish to add")
    add_item_list=[]
    item_found=False
    if choice == 1:
        add_name=str(input("Name: "))
        for items in groceries:
            if items[0] == add_name.lower():
                print("This item already exists, please use the update item option to modify an existing item:")
                exit()
            else:
                continue
        add_desc=str(input("Description: "))
        add_price = input("Price: ")
        add_quantity=input("Number in Stock: ")
        add_item_list = [add_name, add_desc, add_price, add_quantity]
        groceries.append(add_item_list)



def remove_item(indexed_groc_list=None):
    indexed_groc_list = []
    for index, items in list(enumerate(groceries, start=1)):
        indexed_groc_list.append([index] + items)
    remove_item_ID=int(input("Please enter the ID of the item you wish to remove: "))
    remove_item_ID -=1
    print("Are you sure you wish to remove the item following item?" + '\n' + '{}'.format(indexed_groc_list[remove_item_ID]))
    confirm_removal=input("please press \'y\' to confirm or \'n\' to cancel: ")
    if confirm_removal == 'y':
        groceries.remove(groceries[remove_item_ID])
        print_all()
    else:
        print_all()

update_item()

# logic

print_all()
choice='0'
# binary state to run while loop or not 1= True/0=False
prog_finished=0
print(prog_finished)
while prog_finished != 1:
    choice=int(input('{:<5}'.format(choice_prompt_text)))
    if choice == 1:
        add_item()
        print_all()
    if  choice == 2:
        remove_item()
    choice = int(input('{:<5}'.format(choice_prompt_text)))
    if  choice == 23:
        update_item()
    print(choice)
    print(type(choice))
    print('test1')
    prog_finished==1
    print('test2')
