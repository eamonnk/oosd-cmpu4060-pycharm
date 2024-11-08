inp = input("Input an index to set to zero: ")
nums = [1, 2, 3, 4, 5]
index = 0
try:
    index = int(inp)
except ValueError as ve:
    print("A non-number value was entered!")
    print("Exception message:", ve)
else:
    nums[index] = 0
    print("Here is the new list of numbers: ", nums)
finally:
    print("Complete, but not necessarily successfully :-).")