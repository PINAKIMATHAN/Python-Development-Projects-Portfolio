from tkinter import *
from tkinter.ttk import *
from time import strftime

FONT_SIZE = 80
FONT_STYLE = "ds-digital" 
TEXT_COLOR = "white" 
BACKGROUND_COLOR = "navy" 
TIME_FORMAT = "%I:%M:%S %p" # comment out this line for displaying 12 hours time format
#TIME_FORMAT = "%H:%M:%S" # comment out this line for displaying 24 hours time format

interface = Tk()
interface.title("Digital Clock") 
interface.state("zoomed") # display the window in full screen
interface.configure(bg = BACKGROUND_COLOR)

l = Label(interface, text = "D i g i t a l  C l o c k")
l.config(font =("ds-digital", 80, "bold"))

def display_time():
    time_text = strftime(TIME_FORMAT) 
    time_label = Label(interface, font = (FONT_STYLE, FONT_SIZE, "bold"), background = BACKGROUND_COLOR, foreground = TEXT_COLOR)
    time_label.config(text = time_text) 
    time_label.after(1000, display_time) 
    time_label.place(relx = 0.5, rely = 0.35, anchor = "center") 

def display_date():
    date = strftime("%d-%m-%Y") 
    date_label = Label(interface, font = (FONT_STYLE, FONT_SIZE, "bold"), background = BACKGROUND_COLOR, foreground = TEXT_COLOR)
    date_label.config(text = date) 
    date_label.after(1000, display_date) 
    date_label.place(relx = 0.5, rely = 0.65, anchor = "center")   
        
l.pack()
display_time() 
display_date() 

mainloop() 
