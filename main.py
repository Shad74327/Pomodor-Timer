from tkinter import *
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer_text = None

def start_timer():
    global reps
    reps += 1
    if reps < 8 and reps % 2 != 0:
        count_down(WORK_MIN * 60)
        title_label.config(text="Work Mode", fg=RED)
    elif reps == 8:
        count_down(LONG_BREAK_MIN * 60)
        title_label.config(text="Long Break", fg=PINK)
    else:
        count_down(SHORT_BREAK_MIN * 60)
        title_label.config(text="Short Break", fg=GREEN)

def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec <= 9:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer_text
        timer_text = window.after(1000, count_down, count - 1)
    else:
        start_timer()

def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer_text)
    canvas.itemconfig(timer, text="00:00")
    title_label.config(text="Timer")


window = Tk()
window.config(bg=YELLOW, padx=100, pady=50)
window.title("Pomodoro Timer")

title_label = Label(text="Timer", font=(FONT_NAME, 50), bg=YELLOW, fg=GREEN)
title_label.grid(column=1, row=0)

start = Button(text="Start", highlightbackground=YELLOW, command=start_timer)
start.grid(column=0, row=2)

reset = Button(text="Reset", highlightbackground=YELLOW, command=reset_timer)
reset.grid(column=2, row=2)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
pomodoro_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=pomodoro_img)
timer = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

window.mainloop()
