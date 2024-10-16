# bread item defintion
item_bread="bread"
item_desc_bread="A delicious 500g brown loaf."
item_price_bread=1.0
stock_bread=0

# milk item defintion
item_milk="milk"
item_desc_milk="A litre carton of low fat milk."
item_price_milk="1.5"
stock_milk=0

bread_def = [(item_bread), (item_desc_bread), (item_price_bread), (stock_bread)]
milk_def = [(item_milk), (item_desc_milk), (item_price_milk), (stock_milk)]


out_of_stock="Out of Stock"
print("test1")
print(bread_def[3])
print(milk_def[3])
print("test2")
# print(groceries)
# for i in groceries
#    print(groceries.[0:2])


def print_header():
    print("-------------------------------------" + '\n'
        + "Groceries at your Fingertips" + '\n'
            + "----------------------------------" + '\n')

def print_items_in_stock_column_headers():
    print("Items in stock" + '\n' + "----------------------------------" + '\n')
    print('ID Code   ' + '      Name'     + '   Price    ' + '   Number in Stock    ')


def print_items_in_stock_menu(stock=False):
    # item_bread=bread_def[index]
    # item_milk=milk_def[index]
    bread_text = "  "
    milk_text = " "
    if bread_def[3] == 0:
        print("{:<10}".format(str(bread_def[0])), str(bread_def[1]), str(bread_def[2]) + "{:>}".format(str(out_of_stock)))
    if milk_def[3] == 0:
       print(str(milk_def[0]), str(milk_def[1]), str(milk_def[2]) + " Out of Stock")




    #        text += "{0}: ".format(index + 1) if groceries[index][3] > 0 else "   "
    #        text += "{0: <10} {1: <45} €{2: <7}".format(item[0], item[1], item[2])
#    if stock:
 #           text += "[{0: <}]".format(groceries[index][3]) if groceries[index][3] > 0 else "[OUT OF STOCK]"
#      if quantity:
#           text += "{0: <}".format(order[index])
    print(bread_text)

print_header()

print_items_in_stock_column_headers()

print_items_in_stock_menu()

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