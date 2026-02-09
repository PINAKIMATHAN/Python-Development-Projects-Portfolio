from tkinter import *
from datetime import datetime
from time import strftime

WIN =  Tk()
WIN.maxsize(680, 220)
WIN.resizable(False, False)
WIN.configure(bg="navy")
WIN.title("DIGITAL CLOCK") 

def stay_on_top():
   WIN.lift()
   WIN.after(2000, stay_on_top)

a = datetime.today().strftime("%A")
b = (a.upper())
c = (b[0:3]) 

frame =  Frame(WIN, width=680, height=200, bg="navy")
frame.pack(expand=True)

def time():

    a = strftime("%H : %M : %S")
    label.config(text= a)
    label.after(1000, time)

label = Label(frame, font=("Arial", 40, "bold"), bg="navy", fg="white")

label.place(x= 32, y=15)
time()

label1 = Label(frame, font=('Arial',40, "bold"), bg='navy', fg='cyan2')
label1.config(text=c)
label1.place(x=358, y=15)

label1 = Label(frame, font=('Arial',40, "bold"), bg='navy', fg='yellow', text='|')
label1.place(x=300, y=10)

def labels():

    label2=Label(frame, font=('Century Gothic',13),bg='#0e1013',fg='cyan2',text='DAY')
    label2.place(x=392, y=80)

    label3=Label(frame, font=('Century Gothic',13),bg='#0e1013',fg='cyan2',text='HOURS')
    label3.place(x=46, y=80)

    label4=Label(frame, font=('Century Gothic',13),bg='#0e1013',fg='cyan2',text='MINUTES')
    label4.place(x=134, y=80)
 
    label5=Label(frame, font=('Century Gothic',13),bg='#0e1013',fg='cyan2',text='SECONDS')
    label5.place(x=230, y=80)

labels()

WIN.mainloop()
