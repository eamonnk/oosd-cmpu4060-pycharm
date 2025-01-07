from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("200x150")
root.resizable(False, False)

frame = Frame(root)
frame.pack()
vlist = ["January up to December"]

vlist2 = ["1 up to 31"]

vlist3 = ["2015 up to 2040"]

vlist4 = ["1 up to 30"]

Combo = ttk.Combobox(frame, values=vlist, state='readonly')
Combo.set("Pick a month")
Combo.pack(padx=5, pady=5)

Combo2 = ttk.Combobox(frame, values=vlist2, state='readonly')
Combo2.set("Pick a day")
Combo2.pack(padx=5, pady=5)

Combo3 = ttk.Combobox(frame, values=vlist3, state='readonly')
Combo3.set("Pick a year")
Combo3.pack(padx=5, pady=5)


def retrieve():
    if Combo.get() == "April":
        Combo2["values"] = (vlist4)
    else:
        Combo2["values"] = (vlist2)

    print(Combo.get(), Combo2.get(), Combo3.get())


Button = Button(frame, text="Submit", command=retrieve)
Button.pack(padx=5, pady=5)

root.mainloop()