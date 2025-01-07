from match_analysis import MatchAnalysis # match_analysis.py file
from planet_travel_time import PlanetTravelTime # planet_travel_time.py file
from gravity import Gravity # gravity.py file
import tkinter as tk # used for tk work
from tkinter import ttk # some ttk widgets used for attributes they contain
import os # used for file and path work



# create functions that we will call as commands on button clicks in our main app window
# create an instance of the class then call the start app function on that instance
def ma_utility_button_click():
    ma_utility=MatchAnalysis()
    ma_utility.start_match_analysis_app()

def ptt_utility_button_click():
    ptt_utility=PlanetTravelTime()
    ptt_utility.start_planet_travel_time_app()
    
def g_utility_button_click():
    g_utility=Gravity()
    g_utility.start_gravity_app()

def help_button_click():
        
    user_guide_file_path=os.path.dirname(os.path.realpath(__file__))
    # define csv file name to store data. could prompt user for its name and define outside of function but it is not used, seen or interacted with user in the app so just lf it hard coded here 
    user_guide_file_name="user_guide_app.txt"
    user_guide_file_name_and_path=os.path.join(user_guide_file_path, user_guide_file_name)
    
    print(user_guide_file_name_and_path)
    # create new window, which is still a child of 'root', a new separate window
    user_guide_window=tk.Toplevel(root)
    user_guide_window.title("User Guide")
    user_guide_window.geometry('700x400')
    
    # open the user_guise.txt, read contents and assign to a variable
    with open(user_guide_file_name_and_path, 'r') as file:
        user_guide_text_content=file.read()
        
    user_guide_text_obj=tk.Text(user_guide_window, wrap="word")
    user_guide_text_obj.insert('1.0', user_guide_text_content)
    user_guide_text_obj.configure(state='disabled')
    user_guide_text_obj.pack(fill='both', expand=True)

def close_button_click():
    # this stops the event loop
    root.quit()
    # this destroys the root window gui
    root.destroy()


# create main app root window
root = tk.Tk()
root.title("Mini project - 3 Utilities application - Jan 2025")

# create main app windows frame and place it using grid()
app_frame = tk.Frame(root, borderwidth=2, relief="groove", padx=5, pady=10)
app_frame.grid(row=0, column=0, padx=10, pady=10, sticky=('N', 'W', 'E', 'S'))

# Create header text and description text for frame and place them using grid()
app_frame_header = ttk.Label(app_frame, text="Mini Project - 3 Utilities", font=("Helvetica", 10, "bold"))
app_frame_header.grid(row=0, column=0, columnspan=3)
app_frame_desc = ttk.Label(app_frame, text="This application contains 3 separate utilities. Click any of the 3 buttons below to launch that specific utility.", font=("Helvetica", 11, "normal"))
app_frame_desc.grid(row=1, column=0, columnspan=3, padx=20, pady=10, sticky='w, n, e, s')

# craete utility and Help buttons
match_analysis_button=tk.Button(app_frame, text="Match Analysis", padx=5, pady=5, underline=True, background='white', command=ma_utility_button_click)
match_analysis_button.grid(row=2, column=0, columnspan=3, padx=10, pady=5, sticky='w, n, e, s')

planet_travel_time_button=tk.Button(app_frame, text="Planet Travel Time", padx=5, pady=5, underline=True, background='white', command=ptt_utility_button_click)
planet_travel_time_button.grid(row=3, column=0, columnspan=3, padx=10, pady=5, sticky='w, n, e, s')

gravity_button=tk.Button(app_frame, text="Gravity", padx=5, pady=5, underline=True, background='white', command=g_utility_button_click)
gravity_button.grid(row=4, column=0, columnspan=3, padx=10, pady=5, sticky='w, n, e, s')

help_button=tk.Button(app_frame, text="Help", padx=5, pady=5, underline=True, background='white', command=help_button_click)
help_button.grid(row=5, column=0, padx=10, pady=10, sticky='w')

# create a Close button and place it using grid()
app_close_button=tk.Button(app_frame, text="Close", padx=5, pady=5, underline=True, background='white', command=close_button_click)
app_close_button.grid(row=5, column=2, padx=10, pady=10, sticky='e')


# re-sizing
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
app_frame.columnconfigure(0, weight=3)
app_frame.columnconfigure(1, weight=3)
app_frame.columnconfigure(2, weight=3)
app_frame.columnconfigure(3, weight=3)
app_frame.rowconfigure(0, weight=3)
app_frame.rowconfigure(1, weight=3)
app_frame.rowconfigure(2, weight=3)
app_frame.rowconfigure(3, weight=3)
app_frame.rowconfigure(4, weight=3)
app_frame.rowconfigure(5, weight=3)
app_frame.rowconfigure(6, weight=3)



# def close_button_click(self):
#     # this stops the event loop
#     self.root.quit()
#     # this destroys the root window gui
#     self.root.destroy()

root.mainloop()