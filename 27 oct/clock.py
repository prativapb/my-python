"""A simple live digital clock built with Python's standard-library Tkinter."""

import tkinter as tk
from datetime import datetime


def update_clock() -> None:
    """Display the current local time and schedule the next update as showing below"""
    time_label.config(text=datetime.now().strftime("%H:%M:%S"))
    root.after(1000, update_clock)


root = tk.Tk()
root.title("Digital Clock")
root.configure(bg="#1e1e1e")
root.resizable(False, False)

time_label = tk.Label(
    root,
    font=("Segoe UI", 48, "bold"),
    bg="#1e1e1e",
    fg="#00ff99",
    padx=24,
    pady=16,
)
time_label.pack()

update_clock()
root.mainloop()