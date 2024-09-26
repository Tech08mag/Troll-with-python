from tkinter import *
from mouse import mouse
import threading 
import random
from banana import Game

window = Tk()
window.title("You've got hacked")
label = Label(window, text="You've got hacked!", bg='black', fg='green', pady=10, padx=10, font=20)
label.pack()

def open_new_window():
    x = random.randint(0, 3840)
    y = random.randint(0,2160)
    window2 = Toplevel()
    window2.title("You've got hacked")
    window2.geometry(f"200x200+{x}+{y}")
    label = Label(window2, text="You've got hacked!", bg='black', fg='green', pady=10, padx=10, font=20)
    label.pack()

    window.after(10, open_new_window)

while True:
    try:
        t1 = threading.Thread(target = mouse)
        t2 = threading.Thread(target= open_new_window)
        t1.start()
        t2.start()
    except:
        pass

    window.mainloop()