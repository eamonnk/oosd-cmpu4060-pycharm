# # names = ['jim', 'john', 'jane', 'jen']
# #
# # # create an enumerated list
# # indexed_list=list(enumerate(names))
# # print(indexed_list)
# #
# # [ str(x[0] + 1) + " " + x[1] for x in enumerate(names) ]
# # # or
# # list(str(x[0] + 1) + " " + x[1] for x in enumerate(names))
#
# #Initial nested list
# nested_list = [["John", "Doe", 3.14, 42], ["Jane", "Smith", 2.71, 30], ["Alice", "Wonderland", 4.56, 24]]
#
# # Loop through each sublist in the nested list and add an index
# # taken from here https://docs.python.org/3/library/functions.html#enumerate
# i_list=[]
# for index, sublist in enumerate(nested_list, start=2):
#     i_list += ([index] + sublist)
#     print(i_list)
#     # Print the index and each element from the sublist
#     #print([index] + sublist)
#
# # languages = ['Python', 'C', 'Java', 'JavaScript']
# #
# # for index, value in enumerate(languages, start=1):
# #     print(index, value)
#
# # Initial nested list
# nested_list = [["John", "Doe", 3.14, 42], ["Jane", "Smith", 2.71, 30], ["Alice", "Wonderland", 4.56, 24]]
#
# # Get the new string input from the user
# new_string = input("Enter a string to check: ").lower()  # Convert input to lowercase
#
# # Flag to track if the string was found
# string_found = False
#
# # Check if the new string exists in any sublist (case-insensitive)
# for sublist in nested_list:
#     for item in sublist:
#         # Perform case-insensitive comparison only for string values
#         if type(item) == str and item.lower() == new_string:
#             string_found = True
#             break
#     if string_found:
#         break  # Exit the outer loop as well
#
# # Print appropriate message
# if string_found:
#     print(f'The string "{new_string}" already exists in the nested list (case-insensitive).')
# else:
#     print(f'The string "{new_string}" does not exist in the nested list.')

# Initial nested list
nested_list = [["John", "Doe", 3.14, 42], ["Jane", "Smith", 2.71, 30], ["Alice", "Wonderland", 4.56, 24]]

# Get the new string input from the user
new_string = input("Enter a string to check: ").lower()  # Convert input to lowercase

# Flag to track if the string was found
string_found = False

# Check only the first element of each sublist (case-insensitive)
for sublist in nested_list:
    # Compare the first element, convert it to lowercase
    if sublist[0].lower() == new_string:
        string_found = True
        break  # Exit the loop as soon as the string is found

# Print appropriate message
if string_found:
    print(f'The string "{new_string}" already exists in the first element of a nested list (case-insensitive).')
else:
    print(f'The string "{new_string}" does not exist in the first element of any nested list.')


