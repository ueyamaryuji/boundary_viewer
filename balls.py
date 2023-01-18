import tkinter as tk
import random
speed = 2
size = 10

class Ball:
    #global speed
    def __init__(self, x, y, dx, dy, color):
        self.x, self.y = x, y
        self.dx, self.dy = dx*speed, dy*speed
        self.color = color
        self.shape = None

    def move(self, canvas):
        self.erase(canvas)
        self.x += self.dx
        self.y += self.dy
        self.draw(canvas)
        if (self.x >= canvas.winfo_width() or self.x <= 0):
            self.dx = -self.dx
        if (self.y >= canvas.winfo_height() or self.y <= 0):
            self.dy = -self.dy

    def erase(self, canvas):
        canvas.delete(self.shape)

    def draw(self, canvas):
        self.shape = canvas.create_oval(self.x - size, self.y - size, self.x + size, self.y + size, fill= self.color, width=3, outline = "red")

def loop():
    for b in balls:
        b.move(canvas)
    root.after(10, loop)

def color_maker(a, b):
    color1 = "#"+hex(random.randint(a,b)).lstrip("0x")+hex(random.randint(a,b)).lstrip("0x")+hex(random.randint(a,b)).lstrip("0x")
    print(color1)
    return color1

root = tk.Tk()
root.geometry("800x600")

canvas = tk.Canvas(root, width=800, height=600, bg=color_maker(1,2))
canvas.place(x=0, y=0)

balls = []
for j in range(0,100):
    balls.append(Ball(random.randint(0,800), random.randint(0,600),random.randint(0,10)*2-10, random.randint(0,10)*2-10, color_maker(8,15)))

root.after(10,loop)
root.mainloop()
