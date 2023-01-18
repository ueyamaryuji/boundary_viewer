import numpy as np
import tkinter as tk
import random
import re
import sys
from cmath import atan

class circle:
    def __init__(self, x, y, r, color):
        self.x, self.y, self.r = x, y, r
        self.color = color
        self.shape = None
        self.read_poscar()

    def read_poscar(self):
        with open('p_ene.txt', 'r') as f:
            lines = f.readlines()
            title = lines[0]
        
        m = []
        la = []
        m = re.findall('\d+',title)
        n_t = int(m[3])
        nx = int(m[1])

        #追加
        for i in range(0,3):
            m = lines[i+2].split(' ')
            #print(m)
            la = float(m[i])
            if i==0:
                x_lat = la * scale
            if i==1:
                y_lat = la * scale
            
        m = re.match('[0-9]+',lines[6])
        n_atom = m[0]
        theta = atan(1.0/float(n_t))
        x0 = -0.5 * x_lat + canvas.winfo_width() / 2
        y0 = 0.5 * y_lat + canvas.winfo_height() / 2
        for i in range(0,int(n_atom)):
            m = lines[i+8].split(' ')
            x = float(m[0])*canvas.winfo_width()
            y = float(m[1])*canvas.winfo_height()
            print(x,y)
    def draw(self, canvas):
        self.shape = canvas.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, fill=self.color, width=0)
       
def loop():
    for b in balls:
        b.draw(canvas)
    root.after(10, loop)

def color_maker(a, b):
    color1 = "#"+hex(random.randint(a,b)).lstrip("0x")+hex(random.randint(a,b)).lstrip("0x")+hex(random.randint(a,b)).lstrip("0x")
    return color1


root = tk.Tk()
root.geometry("800x600")
canvas = tk.Canvas(root,width=800, height=600, bg='white')
canvas.place(x=0, y=0)

balls = []
scale = 80.0
for j in range(0,100):
    balls.append(circle(random.randint(0,800), random.randint(0,600), random.randint(0,20), color_maker(8,15)))
root.after(10,loop)
root.mainloop()