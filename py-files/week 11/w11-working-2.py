from tkinter import *
from tkinter import ttk

root = Tk()

# padding is clockwise from the left

content = ttk.Frame(root, padding=(0,10,20,30))
frame = ttk.Frame(content, borderwidth=5, relief="ridge", width=200, height=100)
namelbl = ttk.Label(content, text="Name")
name = ttk.Entry(content)

onevar = BooleanVar(value=True)
twovar = BooleanVar(value=False)
threevar = BooleanVar(value=True)

one = ttk.Checkbutton(content, text="One", variable=onevar, onvalue=True)
two = ttk.Checkbutton(content, text="Two", variable=twovar, onvalue=True)
three = ttk.Checkbutton(content, text="Three", variable=threevar, onvalue=True)
ok = ttk.Button(content, text="Okay")
cancel = ttk.Button(content, text="Cancel")

# added sticky part to this line below
content.grid(column=0, row=0, sticky=(N, W, E, S))
frame.grid(column=0, row=0, columnspan=3, rowspan=2, sticky=(N, W, E, S))
namelbl.grid(column=3, row=0, columnspan=2)
name.grid(column=3, row=1, columnspan=2)
one.grid(column=0, row=3)
two.grid(column=1, row=3)
three.grid(column=2, row=3)
ok.grid(column=3, row=3)
cancel.grid(column=4, row=3)


root.columnconfigure(0, weight=1),
root.rowconfigure(1, weight=1),
content.columnconfigure(0, weight=1),
content.columnconfigure(1, weight=1),
content.columnconfigure(2, weight=1),
content.rowconfigure(0, weight=1)
content.rowconfigure(1, weight=1)

#can add padding when setting it as a property or when defoine root at top
content.padding

root.mainloop()