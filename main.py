from tkinter import *
window = Tk()
window.title("You've got hacked")
label = Label(window, text="You've got hacked!", bg='black', fg='green', pady=10, padx=10, font=20)
label.pack()

def open_new_window():
    window2 = Toplevel()
    window2.title("You've got hacked")
    label = Label(window2, text="You've got hacked!", bg='black', fg='green', pady=10, padx=10, font=20)
    label.pack()

    window.after(100, open_new_window)
open_new_window()

window.mainloop()