# coding:utf-8
from cmath import atan
import tkinter as tk
import re
import numpy as np

root = tk.Tk()
root.title(u"tilt")
root.geometry("600x480")

canvas = tk.Canvas(root, width = 600, height = 480, bg = 'white')
canvas.place(x = 0, y = 0)
root.update_idletasks()
scale = 80.0
rr = 6
xx = 0.8498366*3*scale
yy = 0.8498366*3*scale
xp = canvas.winfo_width()/2-3
yp = canvas.winfo_height()/2-3

#POSCARの読み込み
with open('P_ene.txt', 'r') as f:
    lines = f.read().split("\n")
    #print(lines)
    title = lines[0]
    #print(title)
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

    x0 = -0.5 * x_lat + xp
    y0 = 0.5 * y_lat + yp
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
        canvas.create_oval(self.x-self.r, self.y-self.r, self.x+self.r, self.y+self.r, fill=self.color, width = 1, outline = 'black')

def grid(x_lat, y_lat):
    mesh = nx
    canvas.create_rectangle(-0.5 * x_lat + xp, 0.5 * y_lat + yp, -0.5 * x_lat + xp + x_lat, 0.5 * y_lat + yp - y_lat, outline = 'black')
    xd = x_lat / mesh
    yd = y_lat / mesh
    x0 = -0.5 * x_lat + xp
    y0 = 0.5 * y_lat + yp
    for i in range(0,mesh):
        x0 = -0.5 * x_lat + xd * i + xp
        canvas.create_line(x0, y0, x0, y0 - y_lat, fill='black')
    
    for i in range(0,mesh):
        x0 = -0.5 * x_lat + xp
        y0 = 0.5 * y_lat - yd * i + yp
        canvas.create_line(x0, y0, x0 + x_lat, y0, fill='black')


def ratio():
    min = 10000
    max = -10000
    for i in range(0,int(n_atom)):
        m = lines[i+8].split(' ')
        #print(s)
        if (min > float(m[3])):
            min = float(m[3])
        if (max < float(m[3])):
            max = float(m[3])

    dif1 = (max - min) * 100
    ratio = 240 / dif1
    return ratio, max

def draw_atom():
    Ratio,MAX = ratio()
    grid(x_lat, y_lat)
    for i in range(0,int(n_atom)):
        m = lines[i+8].split(' ')
        #print(m)
        zz = float(m[3])
        dif2 = (zz - MAX) * 100
        hsv = (abs)(dif2 * Ratio)
        R, G, B = RGB(hsv)
        #print(R, G, B)
        atom_color = set_color(R,G,B)
        #print(atom_color)
        for j in range(-1,2):
            for k in range(-1,2):
                v1 = multiple(0.0,m[0],m[1],i,j,k)
                atom = circle(v1[0],v1[1],rr,atom_color)
                atom.create(canvas)

#https://www.peko-step.com/tool/hsvrgb.html
def RGB(h):
    R = 0
    G = 0
    B = 0
    max = 255
    if h < 60:
        R = max
        B = max - ((255 / 255) * 255)
        G = (h / 60) * (R - B) + B

    elif h >= 60 and h < 120:
        if h > 100:
            G = max
            B = max - ((255 / 255) * G)
            R = ((120 - h) / 60) * (G - B) + B
        else:
            G = max
            B = G - ((255 / 255) * G)
            R = ((120 - h) / 60) * (G - B) + B

    
    elif h >= 120 and h < 180:
        G = max
        R = G - ((255 / 255) * G)
        B = ((h - 120) / 60) * (G - R) + R

    if h >= 180 and h < 240:
        B = max
        R = B - ((255 / 255) * B) 
        G = ((240 - h) / 60) * (B - R) + R
    
    if R == 0 and G == 0 and B == 0:
        return 0, 0, 240
    return R,G,B

def set_color(R,G,B):
    return "#" + hex(int(R)).lstrip("0x").zfill(2) + hex(int(G)).lstrip("0x").zfill(2) + hex(int(B)).lstrip("0x").zfill(2)

def shift(x,y):
    vv = [0,0]
    vv[0] = x+x0
    vv[1] = -y+y0
    return vv[0],vv[1]

def matrix(theta, x, y):
    vv = [0,0]
    vv[0] = np.cos(theta) * x - np.sin(theta) * y
    vv[1] = np.sin(theta) * x + np.cos(theta) * y
    return vv[0],vv[1]

def draw_number(num, pos):
    canvas.create_text(pos[0], pos[1]-15, text=num, fill='black')

def multiple(theta, x, y, i, j, k):
    v0 = matrix(theta, (j+float(x))*x_lat, (k+float(y))*y_lat)
    v1 = shift(v0[0], v0[1])
    if j == 0 and k == 0:
        draw_number(i, v1)
    return v1


root.after(10, draw_atom)
root.mainloop()


