import tkinter as tk
from random import randint as rnd
from math import sqrt

root = tk.Tk()
c = tk.Canvas(root, width=600, height=400, bg="white")
c.pack()

for i in range(10000):
    x = rnd(10, 590)
    y = rnd(10, 390)
    r = 100

    if y < 200:
        if sqrt(abs(300 - x) ** 2 + abs(200 - y) ** 2) < r:
            color = "red"
        else:
            color = "white"
    else:
        if sqrt(abs(300 - x) ** 2 + abs(200 - y) ** 2) < r:
            color = "white"
        else:
            color = "red"

    c.create_oval(x - 5, y - 5, x + 5, y + 5, fill=color)

root.mainloop()
