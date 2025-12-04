import tkinter as tk

root = tk.Tk()
root.withdraw()
w_a = tk.Toplevel()
w_a.title("Obrazok 1")
a = tk.Canvas(w_a, width=512, height=512, bg="white")
a.pack()
w_b = tk.Toplevel()
w_b.title("Obrazok 2")
b = tk.Canvas(w_b, width=512, height=512, bg="white")
w_c = tk.Toplevel()
w_c.title("Obrazok 3")
b.pack()
c = tk.Canvas(w_c, width=512, height=512, bg="white")
c.pack()

for i in range(256):
    for j in range(256):
        color_a = f"#{i:02X}{255 - j:02X}{i:02X}"
        color_b = f"#{0:02X}{255 - j:02X}{i:02X}"
        color_c = f"#{j:02X}{i:02X}{0:02X}"
        a.create_rectangle(2 * i, 2 * j, (2 * i) + 2, (2 * j) + 2, fill=color_a, outline=color_a)
        b.create_rectangle(2 * i, 2 * j, (2 * i) + 2, (2 * j) + 2, fill=color_b, outline=color_b)
        c.create_rectangle(2 * i, 2 * j, (2 * i) + 2, (2 * j) + 2, fill=color_c, outline=color_c)


root.mainloop()
