import tkinter as tk
from random import randint as rnd
from math import sqrt

root = tk.Tk()
c = tk.Canvas(root, width=600, height=400, bg="white")
c.pack()

for i in range(10000):
    x, y = rnd(5, 595), rnd(5, 395)
    r = 100

    if y < 200:
        if sqrt((300 - x) ** 2 + (200 - y) ** 2) <= r:
            color = "red"
        else:
            color = "white"
    else:
        if sqrt((300 - x) ** 2 + (200 - y) ** 2) <= r:
            color = "white"
        else:
            color = "red"

    c.create_oval(x - 5, y - 5, x + 5, y + 5, fill=color)

root.mainloop()
