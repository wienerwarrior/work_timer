from tkinter import *
import time
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global timer, reps
    window.after_cancel(timer)
    timer_header.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    check.config(text=f"")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        timer_header.config(text="Long Break")
    elif reps % 2 == 0: 
        count_down(SHORT_BREAK_MIN * 60)
        timer_header.config(text="Short Break")
    else:
        count_down( WORK_MIN * 60)
        timer_header.config(text="Work Time")

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global reps, timer
    mins, sec = divmod(count, 60)
    
    canvas.itemconfig(timer_text, text="{:02d}:{:02d}".format(mins, sec))
    if count > 0:
       timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✓"
            check.config(text=f"{mark}")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Tomato Timer")
window.config(padx=100, pady=50)



canvas = Canvas(width=200, height=224)
tomato_img = PhotoImage(file="work_timer/tomato.png")

canvas.create_image(103, 112, image=tomato_img)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 36, 'bold'))
canvas.grid(column=1, row=1)   

timer_header = Label(text="TIMER", font=(FONT_NAME, 36, 'bold'))
start_button = Button(text='Start', command=start_timer)
reset_button = Button(text="Restart", command=reset)
check = Label()





# Grid Layout
timer_header.grid(column=1, row=0)
start_button.grid(column=0, row=2)
reset_button.grid(column=2, row=2)
check.grid(column=1, row=3)





window.mainloop()



