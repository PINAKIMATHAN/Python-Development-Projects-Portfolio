from tkinter import messagebox as mb
import tkinter as tk
import random

r = tk.Tk()
r.geometry('700x550')
r.title('Roll Dice')
c = tk.Canvas(r, width=700, height=550, bg='#191970')
c.pack()


def roll_dice():
    global bttn_clicks
    dice = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    d = {'\u2680':1, '\u2681':2, '\u2682':3, '\u2683':4, '\u2684':5, '\u2685':6}
    die1 = random.choice(dice)
    die2 = random.choice(dice)
    ldice.configure(text=f'{die1} {die2}', bg='#191970')
    c.create_window(350, 250, window=ldice)
    res = d[die1] + d[die2]
    label2.configure(text="You got  "+str(res))
    bttn_clicks += 1
    label1['text'] = "Dice rolled: " + str(bttn_clicks) + " times"
    if (bttn_clicks == 10 and res != 10):
        rollbutton.configure(state='disabled')
        mb.showerror("Game Over", "Sorry,Try Again")
    elif (res == 10):
        rollbutton.configure(state='disabled')
        mb.showinfo("Winner", "Congrats,You Won!!")


def restart():
    global bttn_clicks
    bttn_clicks= 0
    label1.configure(text="")
    label2.configure(text="Not rolled yet")
    rollbutton.configure(state='normal')


ldice = tk.Label(r, text='', font=('Times', 120),fg='#FF69B4')
rollbutton = tk.Button(r, text='Roll the dice', font=('times', 20,"bold"),state="disabled",background="#C0FF3E",foreground='#C71585',height=1, width=15, command=roll_dice)
c.create_window(350, 120, window=rollbutton)
button1 = tk.Button(r, text='Start/Restart game', font=('times', 20,"bold"),background="#008000",foreground='white',height=1, width=15, command=restart)
c.create_window(350, 50, window=button1)
label1 = tk.Label(r, text='', font=('Times',20,'bold'),fg='#C0FF3E', bg='#191970')
c.create_window(180, 410, window=label1)
label2 = tk.Label(r, text='Not rolled yet', font=('Times',20,'bold'),bg='purple',fg='yellow',width=12)
c.create_window(480, 410, window=label2)
label3 = tk.Label(r, text='Winning Rule: The player wins if he or she gets a sum of 10 on rolling 2 dice within 10 chances.', font=('Times',13,'bold'),fg='red',bg="#7FFF00")
c.create_window(350, 500, window=label3)

r.mainloop()
