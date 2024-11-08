l=['apples', 'banana', 'cherry', 'orange', 'peach', 'apricot', 'raspberry']
print("list:", l)
while True:
    try:
        index, value = input("Please enter an index and the new fruit, e.g. '7 blackberry': ").split(sep=" ")
    except Exception as e:
        print(" You did not enter two avleus separated by a space")
    try:
        l[int(index)] = value
    except Exception as e:
            print("Invalid index")
    print("Current list:", l)