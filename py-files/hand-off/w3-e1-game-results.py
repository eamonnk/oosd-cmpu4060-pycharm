'''
Week 3- EX 1 - Game Results
'''

# create an empty list to use top store names,
# get names input from user and append them to the names list
names = [] # listr to store names
scores = [] # list to store scores

current_player_name = input("Please enter a players names: ")
names.append(current_player_name)

current_player_score = int(input("Please enter" + " " + names[0] + "'s score: " ))
scores.append(current_player_score)

#set the index valeu for the loop
loop_index=0

# while last value entered does not equal a full stop proceed into loop
while names[-1] != ".":
    loop_index +=1
    current_player_name = input("Please enter another players name, if you are finished entering player names, please enter a full stop: ")
    if current_player_name == ".":
        break
    names.append(current_player_name)
    current_player_score = int(input("Please enter" + " " + names[(loop_index)] +"'s score: "))
    scores.append(current_player_score)

# print the lowest score
print("The lowest score was" + " " + str(min(scores)))

# print the highest score
print("the highest score was" + " " + str(max(scores)))

# print the average score
avg_acore=()
print("the average score was" + " " + str(round(sum(scores)/len(scores))))

# create a tuple of both lists
lists_combined=tuple((zip(names, scores)))
# sort the tuple by the score values, which is the second element inthe tuple
sorted_tuple=sorted(lists_combined, key=lambda s : s[1])

# crate a list of the names from the sorted tuple which will be highest to lowest score names
#  the * prints the values as litterals
sorted_names=list(map(lambda n: n[0], sorted_tuple))
print("The names from lowest to highest scores was: ", end=" ")
print(*sorted_names)
