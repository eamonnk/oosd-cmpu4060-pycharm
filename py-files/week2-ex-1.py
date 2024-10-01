# Week 2 - Ex 1 - cutting the grass

# Calculate total garden area with input from user for garden length and width,
# we will use float type for inputted values to allow for non whole numbers entered

# Prompt user to input the length and width of the garden
garden_length=float(input("Please enter the length of the garden in metres: "))
garden_width=float(input("Please enter the width of the garden in metres: "))

# total garden area is the garden length multiplied by the garden width
# we round to 1 decimal place to keep the display value manageable
garden_area=round((garden_length*garden_width), 1)

# display the total calculated garden area to the user.
print("Garden area" + " = " + str(garden_area) + " " +  "mtrs squared" + "\n")

# Prompt user to input the length and width of the house
house_length=float(input("Please enter the length of the house in metres: "))
house_width=float(input("Please enter the width of the house in metres: "))

# total house area is the house length multiplied by the house width
# we round to 1 decimal place to keep the display value manageable
house_area=round((house_length*house_width), 1)

print("House area" + " = " + str(house_area) + " " + "mtrs squared" "\n")

# Cuttable grass area is calculated by the formula garden area minus house area
cuttable_area=round((garden_area-house_area), 1)
print("Area of grass which needs to be cut" + " " + "= "  + str(cuttable_area) + "mtrs squared" + "\n" )

# rate of cutting is 0.5 mtrs per second
cutting_rate=0.5

# time to cut grass is cuttable area divided by cutting rate divided by 60 to get value in mins
time_to_cut_grass=round(((cuttable_area/cutting_rate)/60))

# Display resultant time to cut the grass
print("Assuming a cutting rate of 0.5 mtrs/sec, the time to cut the grass will will be " + " " + str(time_to_cut_grass) + " " + "mins" + "\n \n " + "Thank You")


