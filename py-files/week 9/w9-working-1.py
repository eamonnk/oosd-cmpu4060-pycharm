# # # reading characters
# # file = open("test.txt", "r")
# # print(file.read(1))
# # print(file.read(2))
# # print(file.read(3))
# # file.close()		

# file = open("G:\\GG\\oosd-cmpu4060-pycharm\\py-files\\week 9\\test1.txt", "r")
# final_list=[]

# items=file.readline()
# while items:
#     print(items)
#     for line in file:
#         final_list.append(list(map(lambda parenth: parenth.strip ('"\n'), line.split(","))))
#     items=file.readline()
# file.close()

# print(final_list[1])

file = open("G:\\GG\\oosd-cmpu4060-pycharm\\py-files\\week 9\\test1.txt", "w")
file.append("A new line!")
file.close()



