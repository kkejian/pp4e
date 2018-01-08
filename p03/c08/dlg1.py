from tkinter import *
from tkinter.messagebox import *

def callback():
    if askyesnow('Verify', 'Do you really want to quit?'):
        showwarning('Yes', 'Quit not implemented')
    else:
        showinfo('No', ' Quit has been cancelled')


errmsg = 'Sorry no Spam allowed!'
Button(text='Quit', command=callback).pack(fill=X)
Button(text='Spam', command=(lambda: showerror('Spam', errmsg))).pack(fill=X)
mainloop()
