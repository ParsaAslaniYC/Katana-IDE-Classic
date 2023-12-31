#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by SEEMAN version 7m
#  in conjunction with Tcl version 8.6
#    Aug 08, 2021 09:10:14 PM PDT  platform: Linux

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

import button_support

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = 'wheat'  # X11 color: #f5deb3
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#b2c9f4' # Closest X11 color: 'SlateGray2'
        _ana1color = '#eaf4b2' # Closest X11 color: '{pale goldenrod}'
        _ana2color = '#f4bcb2' # Closest X11 color: 'RosyBrown2'

        top.geometry("600x450+654+293")
        top.minsize(1, 1)
        top.maxsize(1905, 1170)
        top.resizable(1,  1)
        top.title("Button Example")
        top.configure(background="wheat")
        top.configure(highlightbackground="wheat")
        top.configure(highlightcolor="black")

        self.top = top

        self.Button1 = tk.Button(self.top)
        self.Button1.place(relx=0.383, rely=0.267, height=73, width=142)
        self.Button1.configure(activebackground="#f4bcb2")
        self.Button1.configure(background="wheat")
        self.Button1.configure(command=button_support.quit)
        self.Button1.configure(compound='top')
        self.Button1.configure(disabledforeground="#b8a786")
        self.Button1.configure(font="-family {DejaVu Sans} -size 14")
        self.Button1.configure(highlightbackground="wheat")
        self._img0 = tk.PhotoImage(file="./stop.gif")
        self.Button1.configure(image=self._img0)
        self.Button1.configure(text='''Push to Quit''')

def start_up():
    button_support.main()

if __name__ == '__main__':
    button_support.main()




