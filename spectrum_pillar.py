import tkinter as tk

canvas = tk.Canvas(master=None, width=100, height=360)
canvas.pack()
s = 255
v = 255

def RGB(h):
    R = 0
    G = 0
    B = 0
    max = v
    min = max - ((s / 255) * max)
    if h < 60:
        R = max
        B = min
        G = (h / 60) * (R - B) + B

    elif h >= 60 and h < 120:
        G = max
        B = min
        R = ((120 - h) / 60) * (G - B) + B

    
    elif h >= 120 and h < 180:
        G = max
        R = min
        B = ((h - 120) / 60) * (G - R) + R

    elif h >= 180 and h < 240:
        B = max
        R = min
        G = ((240 - h) / 60) * (B - R) + R
    
    elif h >= 240 and h < 300:
        B = max
        G = min
        R = ((h - 240) / 60) * (B - G) + G

    elif h >= 300 and h < 360:
        R = max
        G = min
        B = ((360 - h) / 60) * (R - G) + G 
    
    return "#" + hex(int(R)).lstrip("0x").zfill(2) + hex(int(G)).lstrip("0x").zfill(2) + hex(int(B)).lstrip("0x").zfill(2)

Range = 360
for i in range(0,Range):
    color = RGB(i)
    print(color)
    canvas.create_rectangle(0,i,100,i+1,outline=color,fill=color)

canvas.mainloop()