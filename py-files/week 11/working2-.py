# Define the speed of each mode of travel (in km/h)
speeds = {
    "walk": 5,
    "run": 12,
    "cycle": 24,
    "drive": 80,
    "airplane": 800,
    "rocket": 28000,
    "speed_of_light": 299792
}

# Define the distances from Earth to the planets (in km)
distances = {
    "Mercury": 77300000,
    "Venus": 38200000,
    "Mars": 55700000,
    "Jupiter": 629000000,
    "Saturn": 1270000000,
    "Uranus": 2720000000,
    "Neptune": 4350000000,
    "Earth (to the Sun)": 147100000,
    "Pluto": 4280000000
}

# Create a dictionary to store the time (T = D / S) for each combination of speed and planet distance
time_results = {}

# Calculate time for each mode of travel and planet distance
for mode, speed in speeds.items():
    time_results[mode] = {}
    for planet, distance in distances.items():
        time_results[mode][planet] = distance / speed

# Print the time results (time in hours)
for mode, times in time_results.items():
    print(f"Mode of travel: {mode}")
    for planet, time in times.items():
        print(f"  Time to {planet}: {time} hours")
