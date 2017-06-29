from tkinter import *
from tkinter3 import MyGui

# Mainwindow
mainwin = Tk()
Label(mainwin, text=__name__).pack()

# Popupwindow
popup = Toplevel()
Label(popup, text='Attach').pack(side=LEFT)
MyGui(popup).pack(side=RIGHT)
mainwin.mainloop()
