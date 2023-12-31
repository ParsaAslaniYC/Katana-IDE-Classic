#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by SEEMAN version 7m
#  in conjunction with Tcl version 8.6
#    Aug 08, 2021 09:43:54 PM PDT  platform: Linux

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

import cal_support

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = 'wheat'  # X11 color: #f5deb3
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#b2c9f4' # Closest X11 color: 'SlateGray2'
        _ana1color = '#eaf4b2' # Closest X11 color: '{pale goldenrod}'
        _ana2color = '#f4bcb2' # Closest X11 color: 'RosyBrown2'

        top.geometry("568x411+833+450")
        top.minsize(1, 1)
        top.maxsize(1905, 1050)
        top.resizable(1,  1)
        top.title("Calendar 2")
        top.configure(background="wheat")
        top.configure(highlightbackground="wheat")
        top.configure(highlightcolor="black")

        self.top = top

        self.Custom1 = cal_support.Custom(self.top)
        self.Custom1.place(relx=0.16, rely=0.219, relheight=0.467, relwidth=0.68)

        self.Button1 = tk.Button(self.top)
        self.Button1.place(relx=0.44, rely=0.803, height=37, width=72)
        self.Button1.configure(activebackground="#f4bcb2")
        self.Button1.configure(background="wheat")
        self.Button1.configure(command=cal_support.quit)
        self.Button1.configure(disabledforeground="#b8a786")
        self.Button1.configure(highlightbackground="wheat")
        self.Button1.configure(text='''Quit''')

def start_up():
    cal_support.main()

if __name__ == '__main__':
    cal_support.main()




