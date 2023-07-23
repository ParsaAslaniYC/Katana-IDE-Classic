import sys
from tkinter import *
from tkinter import ttk

class TitleBar(Tk):
    def __init__(self):
        # Initilize The Frame:
        self.bar = ttk.Frame(self).pack()
        
