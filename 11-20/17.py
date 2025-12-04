import tkinter as tk
from math import sin, cos

root = tk.Tk()
c = tk.Canvas(root, width=600, height=600, bg="white")
c.pack()


def cart_no_parameters():
    c.create_rectangle(100, 100, 250, 200, fill="red", tags="1")
    c.create_oval(100, 180, 140, 220, fill="black", tags="2")
    c.create_oval(210, 180, 250, 220, fill="black", tags="3")


def cart_parameters(color: str):
    c.create_rectangle(300, 100, 450, 200, fill=color, tags="4")
    c.create_oval(300, 180, 340, 220, fill="black", tags="5")
    c.create_oval(410, 180, 450, 220, fill="black", tags="6")


cart_no_parameters()
cart_parameters("blue")

angle = 0
while 1:
    x = -cos(angle)
    y = sin(angle)
    c.move("1", x, y)
    c.move("2", x, y)
    c.move("3", x, y)
    c.move("4", x, y)
    c.move("5", x, y)
    c.move("6", x, y)
    angle += 0.01
    c.update()
    c.after(10)
