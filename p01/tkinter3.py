from tkinter import *
from tkinter.messagebox import showinfo


class MyGui(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        button = Button(self, text='Press the button, please.',
                        command=self.reply)
        button.pack()

    def reply(self):
        showinfo(title='Popup', message='Button pressed! Thank you.')


if __name__ == '__main__':
    window = MyGui()
    window.pack()
    window.mainloop()
