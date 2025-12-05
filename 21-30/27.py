import tkinter as tk

root = tk.Tk()
c = tk.Canvas(root, width=800, height=800, bg="white")
c.pack()

for i in range(8):
    if i % 2 == 0:
        for j in range(4):
            c.create_rectangle(j * 200, i * 100, j * 200 + 100, i * 100 + 100, fill="black")
    else:
        for j in range(8):
            c.create_rectangle(j * 200 + 100, i * 100, j * 200 + 200, i * 100 + 100, fill="black")

root.mainloop()
