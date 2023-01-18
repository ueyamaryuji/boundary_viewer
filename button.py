import tkinter as tk
import sys
import subprocess

root = tk.Tk()
root.title(u"menu")
root.geometry("280x240")

def program_1():
    cmd = "Python3 fix.py"
    subprocess.Popen(cmd.split())

def program_2(widget):
    #cmd = "Python3 twist.py"
    #subprocess.Popen(cmd.split())
    widget.destroy()
    root2 = tk.Tk()
    root2.title(u"menu2")
    root2.geometry("280x300")
    labeltitle = tk.Label(root2, text=u'Atom', font=("MSゴシック", "30", "bold"), anchor="w", bg="black", fg="white")
    labeltitle.place(x = 0, y = 0, width = 280, height = 50)
    layer07 = tk.Button(root2, text=u'layer0-7', width = 27, height = 2)
    layer07.place(x = 0, y = 80)
    layer12 = tk.Button(root2, text=u'layer1-2', width = 27, height = 2)
    layer12.place(x = 0, y = 120)
    layer34 = tk.Button(root2, text=u'layer3-4', width = 27, height = 2)
    layer34.place(x = 0, y = 160)
    layer56 = tk.Button(root2, text=u'layer5-6', width = 27, height = 2)
    layer56.place(x = 0, y = 200)
    re = tk.Button(root2, text=u'return')
    re.place(x = 100, y = 260)

def finish_menu():
    sys.exit()

#操作メニューボックス
labeltitle = tk.Label(root, text=u'Atom', font=("MSゴシック", "30", "bold"), anchor="w", bg="black", fg="white")
labeltitle.place(x = 0, y = 0, width = 280, height = 50)

# プログラム１
program_1_Button = tk.Button(root, text=u'tilt', width = 27, height = 2)
program_1_Button["command"] = program_1
program_1_Button.place(x = 0, y = 80)

# プログラム２
program_2_Button = tk.Button(root, text=u'twist', width = 27, height = 2)
program_2_Button["command"] =  command=lambda:program_2(root)
program_2_Button.place(x = 0, y = 140)

# 終了

finish_menu_Button = tk.Button(root, text=u'finish')
finish_menu_Button["command"] = finish_menu
finish_menu_Button.place(x = 105, y = 200)


root.mainloop()