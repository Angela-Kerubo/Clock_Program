from tkinter import *
from time import strftime
import tkinter as tk

def update():
    time_string = strftime("%I:%M:%S %p")
    time_label.config(text=time_string)

    day_string = strftime("%A")
    day_label.config(text=day_string)

    date_string = strftime("%B %d, %Y")
    date_label.config(text=date_string)

    window.after(1000, update)

window = Tk()
window.title("Clock")
window.configure(bg="gray")  # Set the background color to gray

time_label = Label(window, font=("Arial", 50), fg="#00FF00", bg="black")
time_label.pack(pady=20, fill=tk.BOTH, expand=True)

day_label = Label(window, font=("Ink Free", 40, "bold",), bg="grey")
day_label.pack(pady=20, fill=tk.BOTH, expand=True)

date_label = Label(window, font=("Ink Free", 30,), bg="grey")
date_label.pack(pady=20, fill=tk.BOTH, expand=True)

update()

window.mainloop()
