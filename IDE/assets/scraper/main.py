import tkinter as tk
from tkinter import *
import webview
root = tk.Tk()
webview.create_window('Geeks for Geeks', 'https://github.com')
webview.start()