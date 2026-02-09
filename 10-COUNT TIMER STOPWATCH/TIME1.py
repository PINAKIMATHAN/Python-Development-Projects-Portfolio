import tkinter as tk

running = False
hours, minutes, seconds = 0, 0, 0

def start():
    global running
    if not running:
        update()
        running = True

def pause():
    global running
    if running:
        stopwatch_label.after_cancel(update_time)
        running = False

def reset():
    global running
    if running:
        stopwatch_label.after_cancel(update_time)
        running = False
    global hours, minutes, seconds
    hours, minutes, seconds = 0, 0, 0
    stopwatch_label.config(text='00:00:00')

def update():
    global hours, minutes, seconds
    seconds += 1
    if seconds == 60:
        minutes += 1
        seconds = 0
    if minutes == 60:
        hours += 1
        minutes = 0
    hours_string = f'{hours}' if hours > 9 else f'0{hours}'
    minutes_string = f'{minutes}' if minutes > 9 else f'0{minutes}'
    seconds_string = f'{seconds}' if seconds > 9 else f'0{seconds}'
    stopwatch_label.config(text=hours_string + ':' + minutes_string + ':' + seconds_string)
    global update_time
    update_time = stopwatch_label.after(1000, update)

root = tk.Tk()
root.geometry('485x220')
root.title('TIMER')
root.configure(bg="gray68")

stopwatch_label = tk.Label(text='00:00:00', font=('Arial', 50, "bold"))
stopwatch_label.pack()

start_button = tk.Button(text='START', height=3, width=7, font=('Arial', 20, "bold"), command=start, bg="blue")
start_button.pack(side=tk.LEFT)
pause_button = tk.Button(text='PAUSE', height=3, width=7, font=('Arial', 20, "bold"), command=pause, bg="green")
pause_button.pack(side=tk.LEFT)
reset_button = tk.Button(text='RESET', height=3, width=7, font=('Arial', 20, "bold"), command=reset, bg="yellow")
reset_button.pack(side=tk.LEFT)
quit_button = tk.Button(text='QUIT', height=3, width=7, font=('Arial', 20, "bold"), command=root.quit, bg="red")
quit_button.pack(side=tk.LEFT)

root.mainloop()
