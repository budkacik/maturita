import tkinter as tk
from math import sin, cos, radians

root = tk.Tk()
c = tk.Canvas(root, width=600, height=600, bg="white")
c.pack()


global points, opposites
points = [[sin(radians(x)), cos(radians(x))] for x in range(0, 181, 45)]


def draw_star(cordx: int, cordy: int):
    size = 10
    for x, y in points:
        c.create_line(cordx - x * size, cordy - y * size, cordx + x * size, cordy + y * size, width=2)


for i in range(9):
    for j in range(9 - i):
        draw_star(100 + i * 25 + 50 * j, 50 + 50 * i)

root.mainloop()
