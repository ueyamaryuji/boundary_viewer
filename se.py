import tkinter as tk
import tkinter.ttk as ttk
import subprocess

def change_app():
    frame_app.tkraise()

def finish():
    root.destroy()

def change_main():
    frame.tkraise()

def program_1():
    cmd = "Python3 fix.py"
    subprocess.Popen(cmd.split())

def program_2():
    cmd = "python3 twist07.py"
    subprocess.Popen(cmd.split())

def program_3():
    cmd = "python3 twist12.py"
    subprocess.Popen(cmd.split())

def program_4():
    cmd = "python3 twist34.py"
    subprocess.Popen(cmd.split())

def program_5():
    cmd = "python3 twist56.py"
    subprocess.Popen(cmd.split())

if __name__ == "__main__":
    # rootメインウィンドウの設定
    root = tk.Tk()
    root.title("tkinter application")
    root.geometry("280x280")

    # rootメインウィンドウのグリッドを 1x1 にする
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)


    # メインフレームの作成と設置
    frame = ttk.Frame(root)
    frame.grid(row=0, column=0, sticky="nsew", pady=20)

    # 各種ウィジェットの作成
    labeltitle = ttk.Label(frame, text=u'Atom', font=("MSゴシック", "40", "bold"), anchor="w")
    labeltitle.place(x = 0, y = -10, width = 280, height = 50)
    #button_change = ttk.Button(frame, text="アプリウィンドウに移動", command=change_app)
    program_1_Button = ttk.Button(frame, text=u'tilt', command=program_1)
    program_1_Button.place(x = 95, y = 70)
    program_2_Button = ttk.Button(frame, text=u'twist', command=change_app)
    program_2_Button.place(x = 95, y = 130)
    finish_menu_Button = ttk.Button(frame, text=u'finish', command=finish)
    finish_menu_Button.place(x = 95, y = 190)

    frame_app = ttk.Frame(root)
    frame_app.grid(row=0, column=0, sticky="nsew", pady=20)
    label = ttk.Label(frame_app,text=u'Atom', font=("MSゴシック", "40", "bold"), anchor="w")
    label.place(x = 0, y = -10, width = 280, height = 50)
    button1 = ttk.Button(frame_app, text=u'layer0-7', command=program_2)
    button1.place(x = 100, y = 70)
    button2 = ttk.Button(frame_app, text=u'layer1-2', command=program_3)
    button2.place(x = 100, y = 100)
    button3 = ttk.Button(frame_app, text=u'layer3-4', command=program_4)
    button3.place(x = 100, y = 130)
    button4 = ttk.Button(frame_app, text=u'layer5-6', command=program_5)
    button4.place(x = 100, y = 160)
    button_re = ttk.Button(frame_app, text=u'return', command=change_main)
    button_re.place(x = 100, y = 210)

    # frameを前面にする
    frame.tkraise()

    root.mainloop()