'''
Week 3- EX 4 - Home insulation grant
'''
# take user input for floor size and house type
floor_area=int(input("Please enter your house floor area in sq mtrs: "))
user_hse_type=input("Please enter your house type i.e. 'detached', 'semi' or 'terraced' : ")

# control strings to match in if statement later
hse_type_1="detached"
hse_type_2="semi"
hse_type_3="terraced"

# define cap size for floor area
cap_size=150

# Grant multiplier values
det_grant_multiplier=2.5
semi_grant_multiplier=1.5
terraced_grant_multiplier=1

# Conditional statements for floor size cap and house type
if floor_area > cap_size and user_hse_type==hse_type_1:
    det_grant_amount = cap_size * det_grant_multiplier
    print("You are entitled to a grant of " + "€" + str(det_grant_amount) + " for external insulation")

elif floor_area > cap_size and user_hse_type==hse_type_2:
    semi_grant_amount = cap_size * semi_grant_multiplier
    print("You are entitled to a grant of " + "€" + str(semi_grant_amount) + " for external insulation")

elif floor_area > cap_size and user_hse_type==hse_type_3:
    terraced_grant_amount = cap_size * terraced_grant_multiplier
    print("You are entitled to a grant of " + "€" + str(terraced_grant_amount) + " for external insulation")

elif floor_area < cap_size and user_hse_type==hse_type_1:
    det_grant_amount = floor_area * det_grant_multiplier
    print("You are entitled to a grant of " + "€" + str(det_grant_amount) + " for external insulation")

elif floor_area < cap_size and user_hse_type==hse_type_2:
    semi_grant_amount = floor_area * semi_grant_multiplier
    print("You are entitled to a grant of " + "€" + str(semi_grant_amount)  + " for external insulation")

elif floor_area < cap_size and user_hse_type==hse_type_3:
    terraced_grant_amount = floor_area * terraced_grant_multiplier
    print("You are entitled to a grant of " + "€" + str(terraced_grant_amount) + " for external insulation")
