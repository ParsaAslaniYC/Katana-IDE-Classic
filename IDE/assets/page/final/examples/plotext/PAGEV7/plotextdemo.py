#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by SEEMAN version 7rc6
#  in conjunction with Tcl version 8.6
#    Dec 21, 2021 06:43:27 AM CST  platform: Linux

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

import plotextdemo_support

class Main:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("1038x609+614+224")
        top.minsize(1, 1)
        top.maxsize(4225, 1410)
        top.resizable(0,  0)
        top.title("Plotext 4.1.3 Demo")
        top.configure(background="skyblue4")
        top.configure(highlightcolor="black")

        self.top = top
        self.PlotData = tk.StringVar()
        self.combobox = tk.StringVar()
        self.cmboPType = tk.StringVar()

        self.btnPlot = tk.Button(self.top)
        self.btnPlot.place(x=620, y=20, height=33, width=113)
        self.btnPlot.configure(activebackground="#f9f9f9")
        self.btnPlot.configure(borderwidth="2")
        self.btnPlot.configure(command=plotextdemo_support.on_btnPlot)
        self.btnPlot.configure(compound='left')
        self.btnPlot.configure(font="-family {DejaVu Sans} -size 10 -weight bold")
        self.btnPlot.configure(text='''Plot''')

        self.btnClear = tk.Button(self.top)
        self.btnClear.place(x=760, y=20, height=33, width=114)
        self.btnClear.configure(activebackground="#f9f9f9")
        self.btnClear.configure(borderwidth="2")
        self.btnClear.configure(command=plotextdemo_support.on_btnClear)
        self.btnClear.configure(compound='left')
        self.btnClear.configure(font="-family {DejaVu Sans} -size 10 -weight bold")
        self.btnClear.configure(text='''Clear''')

        self.btnExit = tk.Button(self.top)
        self.btnExit.place(x=920, y=20, height=33, width=93)
        self.btnExit.configure(activebackground="#f9f9f9")
        self.btnExit.configure(borderwidth="2")
        self.btnExit.configure(command=plotextdemo_support.on_btnExit)
        self.btnExit.configure(compound='left')
        self.btnExit.configure(font="-family {DejaVu Sans} -size 10 -weight bold")
        self.btnExit.configure(text='''Exit''')

        self.lblPlotView = tk.Label(self.top)
        self.lblPlotView.place(x=10, y=80, height=511, width=1019)
        self.lblPlotView.configure(activebackground="#f9f9f9")
        self.lblPlotView.configure(anchor='w')
        self.lblPlotView.configure(background="skyblue3")
        self.lblPlotView.configure(borderwidth="2")
        self.lblPlotView.configure(compound='left')
        self.lblPlotView.configure(font="-family {DejaVu Sans Mono} -size 8")
        self.lblPlotView.configure(relief="groove")
        self.lblPlotView.configure(text='''Label''')
        self.lblPlotView.configure(textvariable=self.PlotData)

        self.TCombobox1 = ttk.Combobox(self.top)
        self.TCombobox1.place(x=20, y=40, height=21, width=197)
        self.TCombobox1.configure(exportselection="0")
        self.TCombobox1.configure(font="-family {DejaVu Sans} -size 10 -weight bold")
        self.TCombobox1.configure(textvariable=self.combobox)
        self.TCombobox1.configure(takefocus="")

        self.Label1 = tk.Label(self.top)
        self.Label1.place(x=20, y=15, height=21, width=179)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="skyblue4")
        self.Label1.configure(compound='left')
        self.Label1.configure(font="-family {DejaVu Sans} -size 10 -weight bold")
        self.Label1.configure(foreground="#ffffff")
        self.Label1.configure(text='''Plot Marker:''')

        self.TCombobox2 = ttk.Combobox(self.top)
        self.TCombobox2.place(x=230, y=40, height=21, width=257)
        self.TCombobox2.configure(exportselection="0")
        self.TCombobox2.configure(font="-family {DejaVu Sans} -size 10 -weight bold")
        self.TCombobox2.configure(textvariable=self.cmboPType)
        self.TCombobox2.configure(takefocus="")

        self.Label1_1 = tk.Label(self.top)
        self.Label1_1.place(x=231, y=15, height=21, width=179)
        self.Label1_1.configure(activebackground="#f9f9f9")
        self.Label1_1.configure(anchor='w')
        self.Label1_1.configure(background="skyblue4")
        self.Label1_1.configure(compound='left')
        self.Label1_1.configure(font="-family {DejaVu Sans} -size 10 -weight bold")
        self.Label1_1.configure(foreground="#ffffff")
        self.Label1_1.configure(text='''Plot Type:''')

def start_up():
    plotextdemo_support.main()

if __name__ == '__main__':
    plotextdemo_support.main()




