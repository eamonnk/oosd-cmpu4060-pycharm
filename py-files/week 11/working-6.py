import tkinter as tk

# Create the main window
root = tk.Tk()

# Create a parent frame
parent_frame = tk.Frame(root)
parent_frame.pack()

# Create a child widget (button) inside the parent frame
child_button = tk.Button(parent_frame, text="Click Me")
child_button.pack()

# Check the parent of the child_button
parent_name = child_button.winfo_parent()
print(f"The parent of the child_button is: {parent_name}")

# To get the actual parent widget, you can use nametowidget
parent_widget = child_button.nametowidget(parent_name)
print(f"The parent widget is: {parent_widget}")

# Start the Tkinter event loop
root.mainloop()
