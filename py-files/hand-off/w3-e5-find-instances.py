'''
Week 3- EX 3 - Find Instances
'''
s1=input("Please enter a string: ")
s2=input("Please enter an substring to search for: ")

# find first index value of string occurrence
search_result_index=int(s1.find(s2))

# put first index value into a list in which we will
# store all occurrences so we can print from it later
search_result_index_list=[search_result_index]

# if string value not found i.e. find returned a -1, then exit the program
# and print the statement that the string was nto found
# else if string found repeat the search for the next occurrence
if search_result_index == -1:
    print("The search string does not appear in the string")
    exit()

else:
    while search_result_index != -1:
        search_result_index = (s1.find((s2), search_result_index+1 ))
        search_result_index_list.append(search_result_index)

# if the list is not empty i.e. sub string items have been found
# delete the last item from the list, which will eb -1, as eventually find must return a -1 when
# it can find no more instances of the search string
# Also, assign last index entry to a variable so can print it out
# separately with an 'and' text as per requirement for print out
# then remove last element from the index list so it doesn't appear twice in print out
if search_result_index_list:
    del search_result_index_list[-1:]
    search_last_entry=[search_result_index_list[-1]]
    del search_result_index_list[-1:]

# print appending of ints to string taken from stack overflow
## https://stackoverflow.com/questions/37625208/printing-an-int-list-in-a-single-line-python3
if search_result_index_list:
    print("The substring appears at positions "
          + " ".join(map(str, search_result_index_list))
            + " and "
                + "{}".format(str(search_last_entry[0])
                    + " in the string"))

