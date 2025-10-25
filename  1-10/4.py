import tkinter as tk
from random import randint as rnd
root = tk.Tk()
c = tk.Canvas(height="400", width="600")
c.pack()

for i in range(1000):
    x, y = rnd(10, 590), rnd(10, 390)
    if 200 < x < 250:
        color = "blue"
    elif 175 < y < 225:
        color = "blue"
    else:
        color = "white"
    c.create_oval(x - 10, y - 10, x + 10, y + 10, fill=color)

root.mainloop()
