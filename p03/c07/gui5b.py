from gui5 import HelloButton


class MyButton(HelloButton):
    """PP4E_gui5b.py"""
    def callback(self):
        print('Ignore press!')

if __name__ == '__main__':
    MyButton(None, text='Hello subclass world').mainloop()
