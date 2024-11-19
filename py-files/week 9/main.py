numList = []
f = open("people.txt", 'r')  # opens file data.txt for reading
l = f.readline()           # reads a line from the file
isNum = ''.join(l.strip("").split(',', 1))
while isNum:
   numList += [ (l) ]
   l = f.readline()
   isNum = ''.join(l.strip().split('.', 1)).isnumeric()

f.close()                  # closes the file

print(numList)
