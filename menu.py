from tkinter import *
from start import start_camera
from PIL import ImageTk, Image
import os

def make_menu():
    m=Tk()
    m.title('R-cubed')
    
    m.attributes("-fullscreen", True)


    screen_w = m.winfo_screenwidth()
    screen_h = m.winfo_screenheight()


    top_frame = Frame(m)

    label = Label(top_frame, text='Let us organize your waste!', font=("Helvetica", 30), bg='limegreen')
    label.pack(fill=X)
    top_frame.pack(fill=X)

    pic_frame = Frame(m)

    img = ImageTk.PhotoImage(Image.open("recycle_vs_organic.jpg").resize(
            (screen_w, screen_h - 250), Image.ANTIALIAS))
    img_panel = Label(pic_frame, image = img)
    img_panel.pack(fill = X, expand = "yes")
    pic_frame.pack(fill = X)

    button_frame = Frame(m, width=screen_w)

    startButton = Button(button_frame, text='Start', width=45, height=15, font=("Helvetica", 60), highlightbackground='lawn green', command=start_camera) 
    button = Button(button_frame, text='Exit', height=15, font=("Helvetica", 60), highlightbackground='red', command=m.destroy)
    startButton.pack(in_=button_frame, side=LEFT, fill=BOTH, expand=True)
    button.pack(in_=button_frame, side=RIGHT, fill=BOTH, expand=True)
    button_frame.pack(fill = X)

    

    m.mainloop()