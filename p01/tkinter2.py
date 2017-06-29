from tkinter import *
from tkinter.messagebox import showinfo


def reply():
    showinfo(title='Popup', message='Button pressed! Thank you.')


window = Tk()
button = Button(window, text='Press the button, please.', command=reply)
button.pack()
window.mainloop()
