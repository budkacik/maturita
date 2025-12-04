import tkinter as tk

root = tk.Tk()
c = tk.Canvas(root, width=600, height=600, bg="white")
c.pack()


def draw_line(event: tk.Event):
    if event.x < 300:
        if event.y < 300:
            color = "red"
        else:
            color = "blue"
    else:
        if event.y < 300:
            color = "green"
        else:
            color = "yellow"

    c.create_line(event.x, event.y, 300, 300, fill=color, width=3)


def erase(event: tk.Event):
    c.create_oval(event.x - 25, event.y - 25, event.x + 25, event.y + 25, fill="white", outline="white")


c.bind("<Button-1>", draw_line)
c.bind("<B1-Motion>", erase)
root.mainloop()
