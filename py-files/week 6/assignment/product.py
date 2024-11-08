# '''
# Week 6 - Assignment -
# Class Inheritance - 2 of 3 files

# --products.py--
# -eamonn kelly
# '''

class Product:

# Constructor to define product attributes
    def __init__(self, n:str, l:int, s:int):
        self.name=n
        self.lowstockmark=l
        self.stock=s


# Function to print, print all is default parameter when and
# formatting is handled in the print statements
    def print_single(self):
        print("Product name is: ", self.name)
        print("Product low stock mark is: ", self.lowstockmark)
        print("Stock number is: ", self.stock)
        print("----------")


# function to print the column headers used in the Items in stock Display
    def print_all():
        # print header
        print('{:<40}'.format(divider_line) + '\n'
                + '{:^40}'.format(website_header)  + '\n'
                    + '{:<40}'.format(divider_line) + '\n')


        print(items_in_stock + '\n' + '{:<40}'.format(divider_line) + '\n')
        print('{:<5}'.format(stock_column_headers[0])
                + '{:<10}'.format(stock_column_headers[1])
                    + '{:<50}'.format(stock_column_headers[2])
                        + '{:<10}'.format(stock_column_headers[3])
                            + '{:<10}'.format(stock_column_headers[4]))

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