import tkinter as tk
from math import sqrt
root = tk.Tk()
c = tk.Canvas(root, width=800, height=800, bg="white")
c.pack()


def get_coords() -> list[int]:
    file = open("41.input.txt", "r")
    out = []
    for line in file:
        out += list(map(int, line.strip().split()))
    return out


def compute_length(surs: list) -> int:
    length = 0
    prev_x, prev_y = surs[0], surs[1]
    for i in range(1, len(surs) // 2):
        x, y = surs[2 * i], surs[2 * i + 1]
        length += sqrt(((x - prev_x) ** 2) + ((y - prev_y) ** 2))
        prev_x, prev_y = x, y
    return length


coords = get_coords()
c.create_polygon(coords, fill="white", outline="black", width=5)
print(f"Dlzka lomenej ciary je {compute_length(coords) :.02f} jednotiek dlzky")

root.mainloop()
