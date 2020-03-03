from tkinter import *
from start import start_camera

def make_menu():
    m=Tk()
    m.title('R-cubed')
    
    m.attributes("-fullscreen", True)

    label = Label(m, text='Let us organize your waste!', bg='lightgreen', font=("Helvetica", 16))
    label.pack()

    startButton = Button(m, text='Start', width=25, command=start_camera) 
    button = Button(m, text='Exit', width=25, command=m.destroy) 

    button.pack() 
    startButton.pack()
    m.mainloop()