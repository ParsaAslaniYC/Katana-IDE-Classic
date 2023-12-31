#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by SEEMAN version 7m
#  in conjunction with Tcl version 8.6
#    Aug 08, 2021 09:27:14 PM PDT  platform: Linux

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

import canvas

def main(*args):
    '''Main entry point for the application.'''
    global root
    root = tk.Tk()
    root.protocol( 'WM_DELETE_WINDOW' , root.destroy)
    # Creates a toplevel widget.
    global _top1, _w1
    _top1 = root
    _w1 = canvas.Toplevel1(_top1)
    init(_top1, _w1)
    root.mainloop()

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top
    fill_canvas()

def fill_canvas():
    global b
    global id
    inner_frame = w.Scrolledwindow1_f   # Rename for convenience.
    b = {}
    id = {}
    no_buttons_per_row = 10
    row = 0
    for j in range(100):
        row, col = divmod(j,no_buttons_per_row)
        b[j] = tk.Button(inner_frame, text="Button "+str(j),
                         width=9, height=3)
        b[j].grid(row=row,column=col)
        b[j].bind('<Button-1>', select_button)
        id[b[j].winfo_id()] = j
    # Magic which ties widget scrollbars to dimensions of the inner_frame.
    b[0].wait_visibility()             # Wait for widget to appear.
    bbox = inner_frame.bbox()          # Geometry of the frame.
    w.Scrolledwindow1.configure(scrollregion=bbox)  # Configure scrolling.

def select_button(event):
    selected = id[event.widget.winfo_id()]
    print(('select_button: selected  =', selected))

if __name__ == '__main__':
    canvas.start_up()




