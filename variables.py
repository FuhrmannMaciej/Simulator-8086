from tkinter import *

class InputField(StringVar):
    def __init__(self):
        super().__init__()
        self.reset()

    def reset(self):
        self.set("0000")
    