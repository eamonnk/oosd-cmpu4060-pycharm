# some names
DATA = [
    ["bed", 3, 5],
    ["milk", 3, 10, 2024, 11, 7],
    ["bread", 3, 4, 2024, 11, 4],
    ["tea", 3, 12, 2024, 11, 7],
]

# Use map with a lambda function to add each sublist as is
new_list = list(map(lambda sublist: sublist, DATA))

print(new_list)
