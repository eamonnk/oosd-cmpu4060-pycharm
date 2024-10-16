# Input strings
main_string = input("Please enter a string: ")
substring = input("Please enter an substring to search for: ")


# Initialize the starting point of the search
index = main_string.find(substring)

# Check if the substring was found
if index == -1:
    print(f"'{substring}' not found in the main string.")
else:
    # Loop to find all occurrences
    while index != -1:
        print(f"'{substring}' found at index {index}")
        # Continue searching from the next character after the current found index
        index = main_string.find(substring, index + 1)
