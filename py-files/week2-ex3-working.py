names = ['Alice', 'Bob', 'Charlie', 'David']
numbers_list = []

# Iterate over the names and ask the user for a number corresponding to each name
for name in names:
    number = int(input(f"Enter a number for {name}: "))
    numbers_list.append(number)

# Print the resulting list of numbers
print("List of numbers corresponding to the names:", numbers_list)