import tkinter as tk
root = tk.Tk()
c = tk.Canvas(root, width=500, height=500, bg="white")
c.pack()


def kruh1(cordx: int, cordy: int) -> None:
    c.create_oval(cordx - 50, cordy - 50, cordx + 50, cordy + 50, fill="black", outline="black")
    c.create_oval(cordx - 25, cordy - 25, cordx + 25, cordy + 25, fill="grey", outline="grey")


def kruh2(cordx: int, cordy: int) -> None:
    c.create_oval(cordx - 50, cordy - 50, cordx + 50, cordy + 50, fill="grey", outline="grey")
    c.create_oval(cordx - 25, cordy - 25, cordx + 25, cordy + 25, fill="black", outline="black")


kruh1(100, 250)
kruh2(200, 250)
kruh1(300, 250)
kruh2(400, 250)

root.mainloop()
