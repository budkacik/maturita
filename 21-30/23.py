import tkinter as tk
from PIL import ImageTk, Image
from math import sin, cos

root = tk.Tk()
c = tk.Canvas(root, width=500, height=500, bg="white")
c.pack()

img = Image.open("car_photo.jpg")
img = img.resize(
    (img.width // 3, img.height // 3), Image.Resampling.LANCZOS)
img = ImageTk.PhotoImage(img)

c.create_image(250, 400, anchor="center", image=img, tags="1")

angle = 0

while 1:
    x, y = cos(angle), -sin(angle)
    print(x, y)
    c.move("1", x, y)
    c.update()
    angle += 0.008
    c.after(1)
