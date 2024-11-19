with open("people.txt", "r") as file:
    list_of_lists = []

    for line in file:
        list_of_lists.append(list(map(lambda s: s.strip('"\n'), line.split(","))))

print(list_of_lists)