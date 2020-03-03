import tkinter
from tkinter import Button
from ibm_watson.compare_comply_v1 import Label

def make_menu():
    m=tkinter.Tk()

    m.title("r-cubed")

    lbl = Label(m, text="images")

    lbl.grid(column=0, row=0)

    btn = Button(m, text="Capture image")

    def clicked():
            
        lbl.configure(text="Image clicked")

    btn.grid(column=1, row=0)

    m.mainloop()


