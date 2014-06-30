import os
from Tkinter import *
 

def Alert():
    root = Tk()
    root.title('Alert Gateway')
    w =500
    h = 100
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws/2) - (500/2)
    y = (hs/2) - (100/2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    Message(root, text="Your gateway has been changed.", background='red', width=300,
          fg='ivory', relief=GROOVE).pack(padx=100, pady=10)
    root.mainloop()
 

gateway = (os.popen("route -n | grep 'UG[ \t]' | awk '{print $2}'")).read()
while 1:
    gateway2 = (os.popen("route -n | grep 'UG[ \t]' | awk '{print $2}'")).read()
    if gateway != gateway2:
        Alert()
        break
