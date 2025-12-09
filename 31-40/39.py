import tkinter as tk

root = tk.Tk()
c = tk.Canvas(width=800, height=800, bg="white")


def collision_handler(direction: int) -> bool:
    pos = c.coords(circle)
    pos = ((pos[0] + pos[2]) / 2, (pos[1] + pos[3]) / 2)
    match direction:
        case 0:  # W
            if pos[0] <= 50:
                return False
        case 1:  # E
            if pos[0] >= 750:
                return False
        case 2:  # N
            if pos[1] <= 50:
                return False
        case 3:  # S
            if pos[1] >= 750:
                return False
    return True


def move(event: tk.Event):
    match event.keysym:
        case "Left":
            if collision_handler(0):
                c.move(circle, -10, 0)
        case "Right":
            if collision_handler(1):
                c.move(circle, 10, 0)
        case "Up":
            if collision_handler(2):
                c.move(circle, 0, -10)
        case "Down":
            if collision_handler(3):
                c.move(circle, 0, 10)


root.bind("<KeyPress-Left>", move)
root.bind("<KeyPress-Right>", move)
root.bind("<KeyPress-Up>", move)
root.bind("<KeyPress-Down>", move)
c.pack()

circle = c.create_oval(350, 350, 450, 450, fill="blue", tags="2")
root.mainloop()
