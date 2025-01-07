# Example: Matrix for Activities Calculations
activities = [5, 12, 24, 80, 800, 28000, 299792]

# Create a matrix for activities
activity_matrix = [[activities[i] * activities[j] for j in range(len(activities))] for i in range(len(activities))]

print(activity_matrix)
# Access a value from the matrix (e.g., value for Activity 1 * Activity 3)
print(activity_matrix[0][2])  # Activity 1 * Activity 3

# Example: Matrix for Planet Distances Calculations
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

# Create a matrix for planet distances
planet_matrix = [[planet_distances[i][1] * planet_distances[j][1] for j in range(len(planet_distances))] for i in range(len(planet_distances))]

# Access a value from the matrix (e.g., value for Mercury * Jupiter)
print(planet_matrix[0][3])  # Mercury * Jupiter
