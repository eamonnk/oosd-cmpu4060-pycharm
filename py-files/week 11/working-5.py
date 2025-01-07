import csv

# Save the results to a CSV file
with open('travel_times.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    # Write header row (modes of travel)
    header = ['Planet'] + list(speeds.keys())
    writer.writerow(header)

    # Write each row with the times
    for planet in distances.keys():
        row = [planet] + [time_results[mode].get(planet, 'N/A') for mode in speeds.keys()]
        writer.writerow(row)
