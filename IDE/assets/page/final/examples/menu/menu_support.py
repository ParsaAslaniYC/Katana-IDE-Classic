#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by SEEMAN version 7l
#  in conjunction with Tcl version 8.6
#    Aug 08, 2021 02:26:40 PM PDT  platform: Linux

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

import menu

def main(*args):
    '''Main entry point for the application.'''
    global root
    root = tk.Tk()
    root.protocol( 'WM_DELETE_WINDOW' , root.destroy)
    # Creates a toplevel widget.
    global _top32, _w32
    _top32 = root
    _w32 = menu.Toplevel1(_top32)
    root.mainloop()

def check1(*args):
    print('menu_support.check1')
    sys.stdout.flush()

def check2(*args):
    print('menu_support.check2')
    sys.stdout.flush()

def copy(*args):
    print('menu_support.copy')
    sys.stdout.flush()

def cut(*args):
    print('menu_support.cut')
    sys.stdout.flush()

def no(*args):
    print('menu_support.no')
    sys.stdout.flush()

def paste(*args):
    print('menu_support.paste')
    sys.stdout.flush()

def post():
    print('menu_support.post')
    sys.stdout.flush()

def quit(*args):
    print('menu_support.quit')
    sys.stdout.flush()
    sys.exit()

def radio_a(*args):
    print('menu_support.radio_a')
    sys.stdout.flush()

def radio_b(*args):
    print('menu_support.radio_b')
    sys.stdout.flush()

def save(*args):
    print('menu_support.save')
    sys.stdout.flush()

def sync(*args):
    print('menu_support.sync')
    sys.stdout.flush()

def yes():
    print('menu_support.yes')
    sys.stdout.flush()

if __name__ == '__main__':
    menu.start_up()




