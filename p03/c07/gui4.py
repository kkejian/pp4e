from tkinter import *


def greeting():
    print('Hello stdout world! ... ')


win = Frame()
win.pack(side=TOP, expand=YES, fill=BOTH)
Label(win, text='Hello Container world').pack(side=TOP)
Button(win, text='Hello', command=greeting).pack(side=LEFT, expand=YES, fill=Y)
Button(win, text='Quit', command=win.quit).pack(side=RIGHT, expand=YES, fill=X)

win.mainloop()
