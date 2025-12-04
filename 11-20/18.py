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


c.bind("<Button-1>", draw_line)
root.mainloop()
