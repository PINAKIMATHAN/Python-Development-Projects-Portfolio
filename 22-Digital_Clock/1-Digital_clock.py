from time import strftime
from tkinter import Label, Tk

window = Tk()
window.title("")
window.geometry("400x150")
window.configure(bg="black")  
window.resizable(True, True)  

clock_label = Label(window,text="Digital Clock", bg="black", fg="cyan", font=("Arial", 40, "bold"))
clock_label.place(x=20, y=20)


def update_label():

    current_time = strftime("%H: %M: %S\n %d-%m-%Y ")
    clock_label.configure(text=current_time)
    clock_label.after(80, update_label)
    clock_label.pack(anchor="center")


update_label()
window.mainloop()

