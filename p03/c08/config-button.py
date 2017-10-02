from tkinter import *
widget = Button(text='Big in Japan', padx=10, pady=10)
widget.pack(padx=20, pady=20)
widget.config(cursor='pencil')
widget.config(bd=8, relief=SOLID)
widget.config(bg='white', fg='red')
widget.config(font=('helvetica', 20, 'bold'))
mainloop()
