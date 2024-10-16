# using the statistics mean method to calculate mean
# details obatined from w3schools and url included below for referemce
import statistics

# create empty list, prompt users for input and ad values to new list
nums_list=[]
user_num=(input("Please enter a number (or non-numeric value if finished): "))
nums_list.append(user_num)

# while user value is is not alphabetical i.e is numerical execute the while loop
# get user input value
# if users enters numerical character append it to the list
while not user_num.isalpha():
    user_num=input("Please enter another number (or non-numeric value if finished): ")
    if not user_num.isalpha():
        nums_list.append(user_num)

# if user enters alphabetical character, do not add it ot the list an
if user_num.isalpha:
    print("You have entered an non numeric value and as such this program will terminate: ")

# calc and print the length of the list, i,e, the number of elements
print("You have entered " + "{}".format(str(len(nums_list)) + " numbers. "))

# calc and print the smallest number
print("The smallest number is " + "{}".format(str(min(nums_list)) + ". "))

# calc and print the biggest number
print("The biggest number is " + "{}".format(str(max(nums_list)) + ". "))

# the mean of the numbers entered and statistics module to import was
# found on stackoverflow at the below url
# https://www.w3schools.com/python/ref_stat_mean.asp
# convert list of strings to list of integers using map
# then run statistics.mean method on it, round to 2 decimals
# print result
nums_list_int=list(map(int, nums_list))
mean=round(statistics.mean(nums_list_int), 2)
print("The mean of your numbers is " + "{}".format(mean) + ". ")


