#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by SEEMAN version 7bb
#  in conjunction with Tcl version 8.6
#    Nov 02, 2021 05:13:16 PM PDT  platform: Linux

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

import busycursor
import time

def main(*args):
    '''Main entry point for the application.'''
    global root
    root = tk.Tk()
    root.protocol( 'WM_DELETE_WINDOW' , root.destroy)
    # Creates a toplevel widget.
    global _top1, _w1
    _top1 = root
    _w1 = busycursor.Toplevel1(_top1)
    global busyWidgets
    busyWidgets = (_top1, )
    root.mainloop()

def quit(*args):
    print('busycursor_support.quit')
    for arg in args:
        print ('another arg:', arg)
    sys.stdout.flush()
    sys.exit()

def run(*args):
    print('busycursor_support.run')
    for arg in args:
        print ('another arg:', arg)
    sys.stdout.flush()
    busyStart()
    time.sleep(5)           # Simulate a long running task.
    busyEnd()

busyCursor = 'watch'
preBusyCursors = None

def busyStart(newcursor=None):
    '''We first check to see if a value was passed to newcursor. If
       not, we default to the busyCursor. Then we walk through the
       busyWidgets tuple and set the cursor to whatever we want.'''
    global preBusyCursors
    if not newcursor:
        newcursor = busyCursor
    newPreBusyCursors = {}
    for component in busyWidgets:
        newPreBusyCursors[component] = component['cursor']
        component.configure(cursor=newcursor)
        component.update_idletasks()
    preBusyCursors = (newPreBusyCursors, preBusyCursors)

def busyEnd():
    '''In this routine, we basically reset the cursor for the widgets
       in our busyWidget tuple back to our default cursor.'''
    global preBusyCursors
    if not preBusyCursors:
        return
    oldPreBusyCursors = preBusyCursors[0]
    preBusyCursors = preBusyCursors[1]
    for component in busyWidgets:
        try:
            component.configure(cursor=oldPreBusyCursors[component])
        except KeyError:
            pass
        component.update_idletasks()    
    
if __name__ == '__main__':
    busycursor.start_up()




