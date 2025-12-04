import tkinter as tk
from random import randint as rnd
from math import sin, cos, radians

root = tk.Tk()
c = tk.Canvas(root, width=600, height=600, bg="blue")
c.pack()

global points, opposites
points = [[sin(radians(x)), cos(radians(x))] for x in range(18, 307, 72)]
opposites = points[3:] + points[:3]


def create_star(cordx: int, cordy: int):
    size = rnd(5, 10)
    for j in range(len(points)):
        c.create_line(cordx - size * points[j][1], cordy - size * points[j][0], cordx - size * opposites[j][1], cordy - size * opposites[j][0], fill="yellow", width=1)
        tempsize = size
        size -= 2
        c.create_line(cordx - size * points[j][1], cordy - size * points[j][0], cordx - size * opposites[j][1], cordy - size * opposites[j][0], fill="yellow", width=2)
        size -= 3
        c.create_line(cordx - size * points[j][1], cordy - size * points[j][0], cordx - size * opposites[j][1], cordy - size * opposites[j][0], fill="yellow", width=3)
        c.create_oval(cordx - 1, cordy - 1, cordx + 1, cordy + 1, fill="yellow", outline="yellow")
        size = tempsize


for i in range(50):
    create_star(rnd(15, 585), rnd(15, 585))

root.mainloop()
