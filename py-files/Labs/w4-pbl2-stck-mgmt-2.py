# bread item defintion
item_bread="Bread"
item_desc_bread="A delicious 500g brown loaf."
item_price_bread=1.0
stock_bread=0
bread_index=1

# milk item defintion
item_milk="Milk"
item_desc_milk="A litre carton of low fat milk."
item_price_milk="1.5"
stock_milk=0
milk_index=2

bread_def = [(item_bread), (item_desc_bread), (item_price_bread), (stock_bread)]
milk_def = [(item_milk), (item_desc_milk), (item_price_milk), (stock_milk)]

stock_column_headers = ['ID', 'Name', 'Description', 'Price', 'In Stock']

out_of_stock="Out of Stock"


def print_header():
    print("-------------------------------------" + '\n'
        + "Groceries at your Fingertips" + '\n'
            + "----------------------------------" + '\n')

def print_items_in_stock_column_headers():
    print("Items in stock" + '\n' + "----------------------------------" + '\n')
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

#print("{:<10} {:<15} {:<30} €{:<10}".format(str(bread_def[0])),
            #str(bread_def[1]),
             #   str(bread_def[2]))
     #               #+ "{:>}".format(str(out_of_stock)))
    #if bread_def[3] == 0:
     #   print("test1")
    #  bread_text.append("{:<10} {:<15} {:<30} €{:<10} {:>10}".format(str(bread_def[0])),
     #         str(bread_def[1]),
    #          str(bread_def[2]))
     #               #+ "{:>}".format(str(out_of_stock)))
      #  print("test2")
    # if bread_def[3] != 0:
     #    print("test3")
      #   print("{:<10} {:<15} {:<30} €{:<10}{:>10}".format(str(bread_def[0]), str(bread_def[1]), str(bread_def[2]), str(bread_def[3])))
       # print("test4")
    #        text += "{0}: ".format(index + 1) if groceries[index][3] > 0 else "   "
    #        text += "{0: <10} {1: <45} €{2: <7}".format(item[0], item[1], item[2])
#    if stock:
 #           text += "[{0: <}]".format(groceries[index][3]) if groceries[index][3] > 0 else "[OUT OF STOCK]"
#      if quantity:
#           text += "{0: <}".format(order[index])


print_header()

print_items_in_stock_column_headers()

print_bread_items_in_stock_menu()
print_milk_items_in_stock_menu()

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