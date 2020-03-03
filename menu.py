import tkinter
from start import start_camera

def make_menu():
    m=tkinter.Tk()
    m.title('R-cubed')
    startButton = tkinter.Button(m, text='Start', width=25, command=start_camera) 
    button = tkinter.Button(m, text='Exit', width=25, command=m.destroy) 
    button.pack() 
    startButton.pack()
    m.mainloop()