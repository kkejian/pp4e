from tkinter import *
from gui7c import HelloPackage

frm = Frame()
frm.pack()
Label(frm, text='Hello').pack()

part = HelloPackage(frm)
part.pack(side=RIGHT)
frm.mainloop()
