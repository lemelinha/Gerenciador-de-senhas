from tkinter import Tk
from Config import *


class App(Tk):
    def __init__(self):
        super().__init__()
        self.Config = Config(self)


    def draw(self):
        self.geometry('400x200')
        self.title('Gerenciador de senhas')
        self.Config.setFrames()
        self.Config.setInputs()


if __name__ == '__main__':
    app = App()
    app.draw()
    app.mainloop()
