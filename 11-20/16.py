import tkinter as tk

root = tk.Tk()
c = tk.Canvas(root, width=600, height=600, bg="white")
c.pack()


def cart_no_parameters():
    c.create_rectangle(100, 100, 250, 200, fill="red")
    c.create_oval(100, 180, 140, 220, fill="black")
    c.create_oval(210, 180, 250, 220, fill="black")


def cart_parameters(color: str):
    c.create_rectangle(300, 100, 450, 200, fill=color)
    c.create_oval(300, 180, 340, 220, fill="black")
    c.create_oval(410, 180, 450, 220, fill="black")


cart_no_parameters()
cart_parameters("blue")

root.mainloop()
