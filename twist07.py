# coding:utf-8
from cmath import atan
import tkinter as tk
import re
import numpy as np
import math

root = tk.Tk()
root.title(u"twist0-7")
root.geometry("600x480")

canvas = tk.Canvas(root, width = 600, height = 480, bg = 'white')
canvas.place(x = 0, y = 0)

scale = 80.0
min = 10000
max = -10000
rr = 5
rx = 0.866025*1.2
ry = 0.5*1.2
root.update_idletasks()
#root.wm_attributes('-alpha',0.5)
xp = canvas.winfo_width()/2-3
yp = canvas.winfo_height()/2-3
#print(xp, yp)

with open('POSCAR.txt', 'r') as f:
    lines = f.read().split("\n")
    #print(lines)
    title = lines[0]
    #print(title)
    m = re.findall(r'\d+\.\d+|\d+',title)
    #print(m)
    theta = math.atan2(1.0, float(m[0]))
    #print(theta)
    
    for i in range(0,3):
        m = lines[i+2].split(' ')
        #print(m)
        la = float(m[i])
        #print(la)
        if i==0:
            x_lat = la * scale
        if i==1:
            y_lat = la * scale

    m = re.findall('[0-9]+',lines[5])
    #print(m)
    n_atom = m[0]   
    #print(x_lat, y_lat)
    f.close()

canvas.create_rectangle(-0.5*x_lat+xp, 0.5*y_lat+yp, -0.5*x_lat+xp+x_lat, 0.5*y_lat+yp-y_lat, fill = 'white', outline='black')   

class tri:
    def __init__(self, x, y, r, color):
        self.x = x
        self.y = y
        self.r = r
        self.color = color

    def up(self, canvas):
        x1 = self.x - rx * self.r
        y1 = self.y + ry * self.r 
        x2 = x1 + self.r * 2
        y2 = y1
        x3 = self.x 
        y3 = self.y - self.r * 1.2
        #print(x1, y1, x2, y2, x3, y3)
        canvas.create_polygon(x1,y1,x2,y2,x3,y3, fill=self.color, outline='black')

    def down(self, canvas):
        x1 = self.x - rx * self.r 
        y1 = self.y - ry * self.r 
        x2 = x1 + self.r * 2
        y2 = y1
        x3 = self.x 
        y3 = self.y + self.r * 1.2
        #print(x1, y1, x2, y2, x3, y3)
        canvas.create_polygon(x1,y1,x2,y2,x3,y3, fill=self.color, outline='black')

def matrix(theta, x, y):
    vv = [0,0]
    vv[0] = np.cos(theta) * x - np.sin(theta) * y
    vv[1] = np.sin(theta) * x + np.cos(theta) * y
    return vv[0],vv[1]

def draw_tilt_rect():
    p_v = [
        [0.0, 0.0],
        [0.0, 1.0],
        [1.0, 1.0],
        [1.0, 0.0],
        [0.0, 0.0]
    ]
    v0 = [0,0]
    v1 = [0,0]
    for i in range(0,4):
        v0 = matrix(theta, p_v[i][0], p_v[i][1])
        v1 = matrix(theta, p_v[i+1][0], p_v[i+1][1])
        canvas.create_line((-0.5+v0[0])*x_lat+xp, (0.5-v0[1])*y_lat+yp, (-0.5+v1[0])*x_lat+xp, (0.5-v1[1])*y_lat+yp, fill='grey')
        v0 = matrix(-theta, p_v[i][0], p_v[i][1])
        v1 = matrix(-theta, p_v[i+1][0], p_v[i+1][1])
        canvas.create_line((-0.5+v0[0])*x_lat+xp, (0.5-v0[1])*y_lat+yp, (-0.5+v1[0])*x_lat+xp, (0.5-v1[1])*y_lat+yp, fill = 'grey')

def draw_number(num,pos,argv,x,y):
    flg = bool(argv)
    #print(pos[0], pos[1])
    if flg:
        canvas.create_text(pos[0]-x, pos[1]-y, text=num, fill='blue')

def loop(argv, dev, init, fin):
    pos = np.zeros((int(n_atom), 3))
    draw_tilt_rect()
    for i in range(0,int(n_atom)):
        m = lines[i+7].split('    ')
        #print(m)
        pos[i][0] = (float(m[0])-0.5)*x_lat+xp
        #print(pos[i][0])
        pos[i][1] = (-float(m[1])+0.5)*y_lat+yp
        #print(pos[i][1])
        pos[i][2] = float(m[2])
        for j in range(-1,2):
            for k in range(-1,2):
                if pos[i][2] >= init and pos[i][2] < init+dev:
                    a = tri(pos[i][0]+x_lat*j, pos[i][1]+y_lat*k, rr,'black')
                    a.down(canvas)
                    #print(pos[i])
                    draw_number(i, pos[i], argv,0,10)
                    
                elif pos[i][2] >= (fin-dev)/1.0 and pos[i][2] < (fin-0.01)/1.0:
                    a = tri(pos[i][0]+x_lat*j, pos[i][1]+y_lat*k, rr,'white')
                    a.up(canvas)
                    draw_number(i, pos[i], argv,0,14)
#print(max)
#print(min)

#0.125, 0.0, 1.0 // 0-7  
#0.125, 0.125, 0.5-0.125 // 1-2
#0.125, 0.5-0.125, 0.5+0.125 // 3-4
#0.125, 0.5+0.125, 1.0-0.125 // 5-6
root.after(10, loop(1,0.125, 0.0, 1.0))
root.mainloop()
