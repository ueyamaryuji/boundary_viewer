# coding:utf-8
from cmath import atan
import tkinter as tk
import re
import numpy as np

root = tk.Tk()
root.geometry("800x600")

canvas = tk.Canvas(root, width = 800, height = 600, bg = 'white')
canvas.place(x = 0, y = 0)


scale = 80.0
min = 10000
max = -10000
rr = 6
xx = 0.8498366*3*scale
yy = 0.8498366*3*scale


with open('p_ene.txt', 'r') as f:
    lines = f.read().split("\n")
    #print(lines)
    title = lines[0]
    print(title)
    m = re.findall('\d+',title)
    #print(m)
    n_t = int(m[3])
    #print(n_t)
    nx = int(m[1])
    #print(nx)
    for i in range(0,3):
        #print(lines[i+2])
        m = lines[i+2].split(' ')
        #print(m)
        la = float(m[i])
        if i==0:
            x_lat = la * scale
        if i==1:
            y_lat = la * scale
    #print(lines[6])
    m = re.match('[0-9]+',lines[6])
    n_atom = m[0]   
    #print(n_atom)
    #print(x_lat)
    #print(y_lat)

    theta = atan(1.0/float(n_t))
    #print(theta)

    x0 = -0.5 * x_lat + canvas.winfo_width() / 2
    y0 = 0.5 * y_lat + canvas.winfo_height() / 2
    #print(x0)
    #print(y0) 
    f.close()

class circle:
    def __init__(self, x, y, r,color):
        self.x = x
        self.y = y
        self.r = r
        self.color = color
    def create(self, canvas):
        canvas.create_oval(self.x-self.r, self.y-self.r, self.x+self.r, self.y+self.r, fill=self.color)

#色付け//無視
for i in range(0,int(n_atom)):
    m = lines[i+8].split(' ')
    #print(s)
    if (min > float(m[3])):
        min = float(m[3])
    if (max < float(m[3])):
        max = float(m[3])

dif1 = (max - min) * 100
ratio = 240 / dif1

for i in range(0,int(n_atom)):
    m = lines[i+8].split(' ')
    x = float(m[0])*canvas.winfo_width()
    print(x)
    y = float(m[1])*canvas.winfo_height()
    print(y)
    zz = float(m[3])
    dif2 = (zz - max) * 100
    atom_color = (abs)(dif2 * ratio)
    
def shift(x,y):
    vv = []
    vv[0] = x+x0
    vv[1] = -y+y0
    return vv

def matrix(theta, x, y):
    vv = []
    vv[0] = np.cos(theta) * x - np.sin(theta) * y
    vv[1] = np.sin(theta) * x + np.cos(theta) * y
    return vv

def draw(theta, j, k):
    v0 = matrix(theta, (j+float(m[1]))*x_lat, (k+float(m[2]))*y_lat)
    v1 = shift(v0[0], v0[1])
    return v0,v1

def loop():
    for i in range(0,int(n_atom)):
        m = lines[i+8].split(' ')
        x = float(m[0])*canvas.winfo_width()
        y = float(m[1])*canvas.winfo_height()
        z = float(m[2])
        if(z == 0):
            a = circle(x,y,rr,"white")
        else:
            a = circle(x,y,rr,"black")
        a.create(canvas)
    root.after(10,loop)
#print(max)
#print(min)

root.after(10, loop)
root.mainloop()


