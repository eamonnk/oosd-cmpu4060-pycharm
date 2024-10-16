import random
# for number in range(0, 11):
#    print(random.randint(1,11))
output = ""
for i in range(2,101, 2):
   output += " "
   output += str(i)
print(output.strip())