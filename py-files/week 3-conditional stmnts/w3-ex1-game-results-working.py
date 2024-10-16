names = []
current_player_name = input("Please enter players names, when finished enter a full stop: ")
names.append(current_player_name)

while names[-1] != ".":
    current_player_name = input("Please enter players name, when finished enter a full stop: ")
    if current_player_name == ".":
        break
    names.append(current_player_name)
print(names)

scores_str_list = []
current_player_score = input("Please enter their score, when finished please enter a full stop: ")
scores_str_list.append(current_player_score)

while scores_str_list[-1] != ".":
    current_player_score = input("Please enter their score, when finished please enter a full stop: ")
    if current_player_score == ".":
      break
    scores_str_list.append(current_player_score)

# print the lowest score
print("the lowest score was" + " " + str(min(scores_str_list)))

# print the highest score
print("the lowest score was" + " " + str(max(scores_str_list)))

# print the average score. Must first convert list of strings to ints so can add them
scores_int_list=[]
for num_in_scores_str_list in scores_str_list:
    scores_int_list.append(int(num_in_scores_str_list))

avg_acore=()
print("the average score was" + " " + str((sum(scores_int_list))/len(scores_int_list)))

highest_score_index = enumerate(scores_int_list)
print(highest_score_index)

