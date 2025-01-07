import tkinter as tk
from tkinter import ttk
import csv

# Create the main window
root = tk.Tk()
root.title("Football Match Entry")

# Create a label to display the selected date
label = tk.Label(root, text="Enter match date:", font=("Helvetica", 12))
label.grid(row=0, column=0, columnspan=2, pady=10)

# Create Entry widgets for day, month, and year
day_entry = tk.Entry(root, font=("Helvetica", 12), width=5)
day_entry.grid(row=1, column=0, padx=5, pady=10)

month_entry = tk.Entry(root, font=("Helvetica", 12), width=5)
month_entry.grid(row=1, column=1, padx=5, pady=10)

year_entry = tk.Entry(root, font=("Helvetica", 12), width=6)
year_entry.grid(row=1, column=2, padx=5, pady=10)

# Label for the football teams entry section
team_label = tk.Label(root, text="Enter football teams:", font=("Helvetica", 12))
team_label.grid(row=2, column=0, columnspan=2, pady=10)

# Create Entry widgets for home team and away team
home_team_label = tk.Label(root, text="Home Team:", font=("Helvetica", 12))
home_team_label.grid(row=3, column=0, padx=5, pady=10, sticky="w")

home_team_entry = tk.Entry(root, font=("Helvetica", 12))
home_team_entry.grid(row=3, column=1, padx=5, pady=10)

away_team_label = tk.Label(root, text="Away Team:", font=("Helvetica", 12))
away_team_label.grid(row=4, column=0, padx=5, pady=10, sticky="w")

away_team_entry = tk.Entry(root, font=("Helvetica", 12))
away_team_entry.grid(row=4, column=1, padx=5, pady=10)


# Function to submit match data and write to a CSV file
def submit_match():
    # Get date from entries
    day = day_entry.get()
    month = month_entry.get()
    year = year_entry.get()

    # Get team names
    home_team = home_team_entry.get()
    away_team = away_team_entry.get()

    # Validate date input (ensure it is numeric and within valid ranges)
    try:
        day = int(day)
        month = int(month)
        year = int(year)
        if not (1 <= day <= 31) or not (1 <= month <= 12) or not (2024 <= year <= 2027):
            raise ValueError("Invalid date")
    except ValueError:
        label.config(text="Invalid date. Please check your entries.")
        return

    # Validate team names (allow spaces in team names)
    if not home_team.strip() or not away_team.strip():
        label.config(text="Please enter both team names.")
        return

    # Open the CSV file and write the match data
    with open("matches.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([f"{day}/{month}/{year}", home_team, away_team])  # Write the match data

    # Clear entry fields after submission
    day_entry.delete(0, tk.END)
    month_entry.delete(0, tk.END)
    year_entry.delete(0, tk.END)
    home_team_entry.delete(0, tk.END)
    away_team_entry.delete(0, tk.END)

    label.config(text="Match data submitted successfully!")


# Create a submit button to write the match data to the CSV file
submit_button = tk.Button(root, text="Submit Match", command=submit_match)
submit_button.grid(row=5, column=0, columnspan=3, pady=10)

# Start the Tkinter event loop
root.mainloop()
