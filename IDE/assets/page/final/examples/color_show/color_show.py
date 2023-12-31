#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by SEEMAN version 7.4l
#  in conjunction with Tcl version 8.6
#    Apr 25, 2022 07:46:20 PM PDT  platform: Linux

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

import color_show_support

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = 'wheat'  # X11 color: #f5deb3
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#b2c9f4' # Closest X11 color: 'SlateGray2'
        _ana1color = '#eaf4b2' # Closest X11 color: '{pale goldenrod}'
        _ana2color = 'beige' # X11 color: #f5f5dc
        _tabfg1 = 'black' 
        _tabfg2 = 'black' 

        top.geometry("221x292+733+169")
        top.minsize(1, 1)
        top.maxsize(1905, 1050)
        top.resizable(1,  1)
        top.title("Show Color")
        top.configure(background="wheat")
        top.configure(highlightbackground="wheat")
        top.configure(highlightcolor="black")

        self.top = top

        self.Message2 = tk.Message(self.top)
        self.Message2.place(relx=0.299, rely=0.205, relheight=0.089
                , relwidth=0.403)
        self.Message2.configure(background="wheat")
        self.Message2.configure(font="-family {DejaVu Sans} -size 13 -weight bold")
        self.Message2.configure(highlightbackground="wheat")
        self.Message2.configure(padx="1")
        self.Message2.configure(pady="1")
        self.Message2.configure(text='''Message''')
        self.Message2.configure(width=90)

        self.Frame1 = tk.Frame(self.top)
        self.Frame1.place(relx=0.217, rely=0.342, relheight=0.257
                , relwidth=0.566)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="wheat")
        self.Frame1.configure(highlightbackground="wheat")

        self.Message3 = tk.Message(self.top)
        self.Message3.place(relx=0.299, rely=0.616, relheight=0.089
                , relwidth=0.403)
        self.Message3.configure(background="wheat")
        self.Message3.configure(font="-family {DejaVu Sans} -size 13 -weight bold")
        self.Message3.configure(highlightbackground="wheat")
        self.Message3.configure(padx="1")
        self.Message3.configure(pady="1")
        self.Message3.configure(text='''Message''')
        self.Message3.configure(width=90)

        self.Button1 = tk.Button(self.top)
        self.Button1.place(relx=0.344, rely=0.719, height=35, width=69)
        self.Button1.configure(activebackground="beige")
        self.Button1.configure(background="wheat")
        self.Button1.configure(borderwidth="2")
        self.Button1.configure(command=color_show_support.sys.exit)
        self.Button1.configure(compound='left')
        self.Button1.configure(disabledforeground="#b8a786")
        self.Button1.configure(font="-family {DejaVu Sans} -size 12 -weight bold")
        self.Button1.configure(highlightbackground="wheat")
        self.Button1.configure(text='''Quit''')

        self.Label1 = tk.Label(self.top)
        self.Label1.place(relx=0.158, rely=0.068, height=27, width=151)
        self.Label1.configure(activebackground="#ffffcd")
        self.Label1.configure(background="wheat")
        self.Label1.configure(compound='left')
        self.Label1.configure(disabledforeground="#b8a786")
        self.Label1.configure(font="-family {DejaVu Sans} -size 14 -weight bold")
        self.Label1.configure(highlightbackground="wheat")
        self.Label1.configure(text='''Label''')

def start_up():
    color_show_support.main()

if __name__ == '__main__':
    color_show_support.main()




