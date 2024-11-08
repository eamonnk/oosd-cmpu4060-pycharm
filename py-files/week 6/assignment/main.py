from product import Product


divider_line="----------------------------------------"
website_header="Groceries at your Fingertips"
stock_column_headers = ['ID', 'Name', 'Description', 'Price', 'Amount in Stock']
out_of_stock="Out of Stock"
stock_mgmt_option_menu="Stock Management Options"#
items_in_stock="Items in Stock"


DATA = [
    ["milk", 3, 10],
    ["bread", 3, 4],
    ["tea", 3, 1],
    ["eggs", 3, 33],
    ["ice cream",3, 2]
]


p1=Product("milk", 3, 10)
p1.print_single()