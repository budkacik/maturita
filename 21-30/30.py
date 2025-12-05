import tkinter as tk

root = tk.Tk()
c = tk.Canvas(root, height=300, width=900, bg="white")
c.pack()


def draw_circ(x: int, y: int) -> None:
    c.create_oval(x - 10, y - 10, x + 10, y + 10, fill="red")


def shape1() -> None:
    for i in range(5):
        for j in range(5 - i):
            draw_circ(50 + 50 * j, 50 + 50 * i)


def shape2() -> None:
    for i in range(5):
        for j in range(i, 5):
            draw_circ(350 + 50 * j, 50 + 50 * i)


def shape3() -> None:
    for i in range(5):
        for j in range(5 - i):
            draw_circ(650 + i * 25 + j * 50, 50 + 50 * i)


shape1()
shape2()
shape3()

root.mainloop()
