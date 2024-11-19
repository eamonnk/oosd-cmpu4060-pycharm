import random
# n = random.randint(0, 5)
# while n != 0:
#     for i in range(1, n + 1):
#         print(str(i) + " ", end="")
#     print("")
#     n = random.randint(0, 5)

random_list_num= []
for i in range (0, 10):
    x=random.randint(0, 200)
    random_list_num.append(x)
    print(x)
print(random_list_num)