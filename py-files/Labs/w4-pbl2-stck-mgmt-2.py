# bread item definition
item_bread="Bread"
item_desc_bread="A delicious 500g brown loaf."
item_price_bread=1.0
stock_bread=10
bread_index=1

# milk item definition
item_milk="Milk"
item_desc_milk="A litre carton of low fat milk."
item_price_milk="1.5"
stock_milk=0
milk_index=2

bread_def = [(item_bread), (item_desc_bread), (item_price_bread), (stock_bread)]
milk_def = [(item_milk), (item_desc_milk), (item_price_milk), (stock_milk)]

divider_line="----------------------------------------"
website_header="Groceries at your Fingertips"
stock_column_headers = ['ID', 'Name', 'Description', 'Price', 'In Stock']
out_of_stock="Out of Stock"
stock_mgmt_option_menu="Stock Management Options"

sm_add_item_index="(1)"
sm_remove_item_index="(2)"
sm_update_item_index="(3)"
sm_update_stock_index="(4)"
sm_exit_item_index="(5)"
sm_add_button_txt=("add item")
sm_remove_button_txt=("add item")
sm_update_button_txt=("add item")
sm_update_button_txt=("add item")
sm_choice_prompt_text="Please choose an option (1, 2, 3 4 or 5): "
sm_choice=int(0)
sm_quantity=int(0)






def print_header():
    print('{:<40}'.format(divider_line) + '\n'
            + '{:^40}'.format(website_header)  + '\n'
                + '{:<40}'.format(divider_line) + '\n')

def print_items_in_stock_column_headers():
    print("Items in stock" + '\n' + '{:<40}'.format(divider_line) + '\n')
    print('{:<5}'.format(stock_column_headers[0])
            + '{:<10}'.format(stock_column_headers[1])
                + '{:<40}'.format(stock_column_headers[2])
                    + '{:<10}'.format(stock_column_headers[3])
                        + '{:<10}'.format(stock_column_headers[4]))


def print_bread_items_in_stock_menu():
    bread_text = ""
    bread_def_str = bread_def
    if bread_def[3] == 0:
        bread_text += '{:<5}{:<10}{:<40}{:<10}{:<10}'.format((bread_index),
                                            (bread_def_str[0]),
                                                (bread_def_str[1]),
                                                    (bread_def_str[2]),
                                                        (out_of_stock))
    else:
        bread_text += '{:<5}{:<10}{:<40}{:<10}{:<10}'.format((bread_index),
                                            (bread_def_str[0]),
                                                (bread_def_str[1]),
                                                    (bread_def_str[2]),
                                                        (bread_def_str[3]))
    print(bread_text)

def print_milk_items_in_stock_menu():
    milk_text = ""
    milk_def_str = milk_def
    if milk_def[3] == 0:
        milk_text += '{:<5}{:<10}{:<40}{:<10}{:<10}'.format((milk_index),
                                            (milk_def_str[0]),
                                                (milk_def_str[1]),
                                                    (milk_def_str[2]),
                                                        (out_of_stock))
    else:
        milk_text += '{:<5}{:<10}{:<40}{:<10}{:<10}'.format((bread_index),
                                            (milk_def_str[0]),
                                                (milk_def_str[1]),
                                                    (milk_def_str[2]),
                                                        (milk_def_str[3]))
    print(milk_text)


def print_stock_mgmt_options_menu():
        print('\n' + '{:<5}'.format(str(stock_mgmt_option_menu)) + '\n'
              + '{:<40}'.format(divider_line) + '\n')
        print('{:<5}'.format(str(sm_add_item_index)) + '{:<20}'.format(str(sm_add_button_txt)))
        print(input('{:<5}'.format(sm_choice_prompt_text)))
        print(sm_choice)
        print(type(sm_choice))

def sm_choice():
    return int(input('{:<5}'.format(sm_choice_prompt_text)))
    print(num)


sm_choice()
print(sm_choice)
print(type(sm_choice))






#print_header()
##print_items_in_stock_column_headers()
#print_bread_items_in_stock_menu()
#print_milk_items_in_stock_menu()
#print_stock_mgmt_options_menu()
sm_choice()
print(sm_choice)
print(type(sm_choice))
'''
        item = groceries[index]
        text = ""
        if ids:
            text += "{0}: ".format(index + 1) if groceries[index][3] > 0 else "   "
        text += "{0: <10} {1: <45} €{2: <7}".format(item[0], item[1], item[2])
        if stock:
            text += "[{0: <}]".format(groceries[index][3]) if groceries[index][3] > 0 else "[OUT OF STOCK]"
        if quantity:
            text += "{0: <}".format(order[index])
        print(text)

def print_stock_mgmt_options():
    print("Stock management options" + '\n'
        + "----------------------------------" + '\n')


#print items in stock
# print(groceries.index[1])


# print_header()
# print_items_in_stock_menu()
# print_items_in_stock_headers()
# print_items_in_stock
# print(groceries)
# print_stock_mgmt_options()
'''