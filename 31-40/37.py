import tkinter as tk
from random import choice as rnd

root = tk.Tk()
c = tk.Canvas(root, width=600, height=700, bg="white")
c.pack()

x = 60
y = 40
poc = int(input('Zadaj počet guličiek v závese: '))

for i in range(0, poc):
    y = 40
    for j in range(0, poc):
        r = rnd((10, 30))
        c.create_oval(x - r / 2, y, x + r / 2, y + r, fill="red" if r == 10 else "blue")
        y += r
    x += 30

root.mainloop()
