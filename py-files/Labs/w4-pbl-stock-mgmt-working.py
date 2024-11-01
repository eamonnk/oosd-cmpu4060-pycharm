# Initial nested list
nested_list = [["John", "Doe", 3.14, 42], ["Jane", "Smith", 2.71, 30], ["Alice", "Wonderland", 4.56, 24]]

# Loop through each sublist in the nested list
for i in nested_list:
    # Print each element from the sublist
    print('{:<5}'.format(i[0]), '{:<10}'.format(i[1]), '{:<5}'.format(i[2]), '{:<5}'.format(i[3]))
