import csv

# Define your lists
activities = [5, 12, 24, 80, 800, 28000, 299792]
planet_distances = [
    ("Mercury", 77300000),
    ("Venus", 38200000),
    ("Mars", 55700000),
    ("Jupiter", 629000000),
    ("Saturn", 1270000000),
    ("Uranus", 2720000000),
    ("Neptune", 4350000000),
    ("Earth (to the Sun)", 147100000),
    ("Pluto", 4280000000)
]

# Function to multiply elements and create CSV for activities
def multiply_activities(activities):
    result = []
    for i in range(len(activities)):
        row = []
        for j in range(len(activities)):
            row.append(activities[i] * activities[j])
        result.append(row)

    # Save the results to a CSV
    with open('activities_results.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([f"Activity {i+1}" for i in range(len(activities))])  # Header
        writer.writerows(result)

# Function to multiply elements and create CSV for planet distances
def multiply_planet_distances(planet_distances):
    result = []
    for i in range(len(planet_distances)):
        row = []
        for j in range(len(planet_distances)):
            row.append(planet_distances[i][1] * planet_distances[j][1])
        result.append(row)

    # Save the results to a CSV
    with open('planet_distances_results.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([planet[0] for planet in planet_distances])  # Header
        writer.writerows(result)

# Call the functions
multiply_activities(activities)
multiply_planet_distances(planet_distances)

