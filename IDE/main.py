"""
    <BEGIN>
    Author : qLogan or ParsaAslani
    Date : 5/3/2023 25 Days Until 01/04/2023
    Codename : Silver Backpack Big Update
    Format : UTF-8, Style : CRLF
    Version : 23.03.05 PreRelease
    Launguage : Python
    Project : IDE
    Name : Katana IDE
    Repository : https://github.com/qlogananiversity/katana-ide/
    <END>
"""
try:
        import json
        import os,sys
        import subprocess
        import threading
        import tkinter as tk
        from functools import partial
        from pathlib import Path
        import webbrowser
        import zipfile
        import random
        from datetime import datetime
        from pathlib import Path
        try:
                from tkinter import *
                from tkinter import filedialog, font, messagebox, ttk
                from tkinter.filedialog import asksaveasfile
                import idlelib.colorizer as ic
                
                import idlelib.percolator as ip
                import re
                from tkinter.scrolledtext import ScrolledText
        except:
                print("Your Python was Not Configured for Tkinter...")
                input("Press Enter to EXIT...")
                

        try: 
                from lib_native.dialogs import * # * -Special_Import- *
                import lib_native.dialogs
                from lib_native import dialogs
                def msg(s,t,m,func=None):
                        print("[ DEBUG ] : Sun_Valley MessageBox Loaded")
                        if s=="err":
                                code = messagebox.showerror(t,m)
                                if code=="ok":
                                        return 0
                                if code==None:
                                        return 0
                        if s=="warn":
                                code = messagebox.showwarning(t,m)
                                if code=="ok":
                                        return 0
                                if code==None:
                                        return 0
                        if s=="info":
                                code = dialogs.show_message(t,m)
                                if code=="ok":
                                        return 0
                                if code==None:
                                        return 0
                        if s=="yon":
                                code = dialogs.ask_yes_no(t,m)
                                if code=="yes":
                                        func
                                if code=="no":
                                        return 0
                                else: {
                                        exit()
                                }
                        if s=="yoc":
                                code = dialogs.ask_ok_cancel(t,m)
                                if code=="ok":
                                        func
                                if code=="cancel":
                                        return 0
                                else : {
                                        exit()
                                }
                        if s=="yrc":
                                code = dialogs.ask_retry_cancel(t,m)
                                if code=="retry":
                                        func
                                if code=="cancel":
                                        return 0
                                else : {
                                        exit()
                                }
                        if s=="question":
                                code = messagebox.askquestion(t,m)
                                if code=="yes":
                                        func
                                if code=="cancel":
                                        return 0
                                else : {
                                        exit()
                                }
                        if s=="yab":
                                code = dialogs.ask_allow_block(t,m)
                                if code=="allow":
                                        func
                                else:
                                        return 0
                        else : {
                                print("اگه بلد نیستی کار کنی نکن\nفانکشن رو خودت نوشتی بعد بلد نیستی؟")
                        }

        except:
                print("Feature Warning","The Special Feature of Katana IDE was Fail to Load\nPlease Install Katana IDE Complete or Restart \nERROR CODE (sv_messagebox_fail01)")
                def msg(s,t,m,func=None):
                        if s=="err":
                                code = messagebox.showerror(t,m)
                                if code=="ok":
                                        return 0
                                if code==None:
                                        return 0
                        if s=="warn":
                                code = messagebox.showwarning(t,m)
                                if code=="ok":
                                        return 0
                                if code==None:
                                        return 0
                        if s=="info":
                                code = messagebox.showinfo(t,m)
                                if code=="ok":
                                        return 0
                                if code==None:
                                        return 0
                        if s=="yon":
                                code = messagebox.askyesno(t,m)
                                if code=="yes":
                                        func
                                if code=="no":
                                        return 0
                                else: {
                                        exit()
                                }
                        if s=="yoc":
                                code = messagebox.askokcancel(t,m)
                                if code=="ok":
                                        func
                                if code=="cancel":
                                        return 0
                                else : {
                                        exit()
                                }
                        if s=="yrc":
                                code = messagebox.askretrycancel(t,m)
                                if code=="retry":
                                        func
                                if code=="cancel":
                                        return 0
                                else : {
                                        exit()
                                }
                        if s=="question":
                                code = messagebox.askquestion(t,m)
                                if code=="yes":
                                        func
                                if code=="cancel":
                                        return 0
                                else : {
                                        exit()
                                }
                        else : {
                                print("اگه بلد نیستی کار کنی نکن\nفانکشن رو خودت نوشتی بعد بلد نیستی؟")
                        }
        
        try:
                import multitasking
                import platform as pt
                import socket as sc
                from chlorophyll import CodeView
                import keyboard
                import shutil
                import wmi
                from PyQt6 import QtWidgets
                from pygments import lexers
                from pygments import *
                import pygments
                from pygments.lexers import *
                try: 
                        '''
                                Test For Bad Import:
                                ( from pygments.lexers import * )
                        '''
                        pass
                except: msg("info","Warning","Please Reinstall Pygments")
        except:
                msg("err","Startup Error","Katana IDE Failed to Load Required Packages\nMake Sure you installed the packages\nERROR CODE (nitp01)")
                exit()
        try:
                #from codeeditor import *
                #from codeeditor import TextLineNumbers, TextPad
                from tkterm import Terminal
                try : from helper.tkinter.xenrender.demo import *
                except :
                        print("[ DEBUG ] : XEN-Render Cannot Be Loaded because Coding Bug")
                #from helper.tkinter import hotbird
        except:
                msg("err","Error","Katana IDE Failed to Load Required Files\nIf This is First Time You Launched the Katana IDE,Make Sure Katana IDE Installed Complete\nElse, Reinstall the Katana IDE\nERROR CODE (tptknf01)")
                #exit()
except:
        msg("err","Critical Error","Katana IDE Failed to Load Required Packages\nMake Sure You Installed All of the Packages with PIP\nERROR CODE (uniaotpwp01)")
        #exit()
multitasking.set_max_threads(20)
filename_show = 'Untitled'
__current__ = ("2023","04","01")
theme_used = None
stheme = "dark"
inited = False
roote = None


def init_theme(func):
    def wrapper(*args, **kwargs):
        global inited
        global roote

        if not inited:
            from tkinter import _default_root

            path = (Path(__file__).parent / "assets/theme/sv.tcl").resolve()

            try:
               _default_root.tk.call("source", str(path))
            except AttributeError:
                raise RuntimeError(
                    "can't set theme, because tkinter is not initialized. "
                    + "Please create a tkinter.Tk instance first and then set the theme."
                ) from None
            else:
                inited = True
                roote = _default_root

        return func(*args, **kwargs)

    return wrapper


@init_theme
def set_theme(theme):
    if theme not in {"dark", "light"}:
        raise RuntimeError("not a valid theme name: {}".format(theme))

    root.tk.call("set_theme", theme)


@init_theme
def get_theme():
    theme = root.tk.call("ttk::style", "theme", "use")

    return {"sun-valley-dark": "dark", "sun-valley-light": "light"}.get(theme, theme)


@init_theme
def toggle_theme():
    if get_theme() == "light":
        use_dark_theme()
    else:
        use_light_theme()


use_dark_theme = partial(set_theme, "dark")
use_light_theme = partial(set_theme, "light")
class TkErrorCatcher:

    '''
    In some cases tkinter will only print the traceback.
    Enables the program to catch tkinter errors normally

    To use
    import tkinter
    tkinter.CallWrapper = TkErrorCatcher
    '''

    def __init__(self, func, subst, widget):
        self.func = func
        self.subst = subst
        self.widget = widget

    def __call__(self, *args):
        try:
            if self.subst:
                args = self.subst(*args)
            return self.func(*args)
        except SystemExit as msg:
            raise SystemExit(msg)
        except Exception as err:
            raise err


tk.CallWrapper = TkErrorCatcher
null = 'nones'
@multitasking.task
def glade():
        try:
                subprocess.call(["run_glade.bat"])
        except:
                msg("err","Error","glade Runner Warrper Not Found\nPlease Reinstall The Katana IDE \nERROR CODE (grwnf01)")
                return 0
        
        
@multitasking.task
def run():
        """
                _summary_
                This Function was Run The Codes you write
        """
        root.f = asksaveasfile(initialfile = 'Untitled.py',defaultextension=".py",mode="w",filetypes=[("Python Source File","*.py"),("Python Source File","*.py")])
        if root.f is None:
                return
        file_save = str(textPad.get(1.0,END))
        args = root.f.name
        autosave(args)
        root.f.write(file_save)
        args = root.f.name
        print(root.f.name)
        fps = open(r'dir.ini', 'w') 
        path = root.f.name
        try:
                fps.write(root.f.name)
        except:
                msg("warn","Warning","Access denied\nPermissions not Allowed for Run the File\nPlease Run Katana IDE as Administrator\nWARN CODE (pnafr01)")
                return 0
        fps.close()
        root.f.close()
        try:
                subprocess.call(['runfile.bat'])
        except:
                msg("err","Error","run File Warrper was Not Found\nPlease Reinstall the Katana IDE\nERROR CODE (rfwwnf02)")
                return 0
@multitasking.task
def venv_create():
        folder = filedialog.askdirectory()
        if folder==None:
                return
        dir = folder
        try:
                subprocess.call(['create_venv.bat', dir])
        except:
                msg("err","Error","Virtual Enviroment Creator Warrper was Not Found\nPlease Reinstall the Katana IDE\nERROR CODE (vecwwnf01)")
def pip():
        pip = tk.Tk()
        theme_system()
        if null=='null':
                root.filename = filedialog.asksaveasfile(mode="w",defaultextension='.txt')
        pip.geometry('200x89')
        pip.minsize(200,89)
        pip.maxsize(200,89)
        pip.title('Package Installer')
        textp = Text(pip,width=25,height=3,relief=RIDGE,font=('Seoge UI Light',10,'bold'),borderwidth=2)
        textp.place(x=200,y=75)
        textp.pack()
        def pkg():
                pip.filename = str('tools/scripts/temp/requirements.txt')
                pkg_selected = str(textp.get(1.0,END))
                try:
                        fp = open(r'python/python37-32/scripts/temp/requirements.txt', 'w')
                        fp.write(pkg_selected)
                except:
                        msg("err","Error","Access Denied\nPlease Run Te Katana IDE as Administrator\nERROR CODE (access_denied)")
                        return 0
                try:
                        os.startfile("package.bat")
                except:
                        msg("err","Error","PIP Interface Warrper was Not Found\nPlease Reinstall the Katana IDE\nERROR CODE (piwwnf01)")
                        return 0
        package = ''
        install = ttk.Button(pip,text='Install',command=pkg)
        install.place(x=0,y=0)
        install.pack()
def torlboard():
        troot = tk.Tk()
        troot.title("TorlBoard - OfficialRelease")
        troot.geometry("600x500")
        final = open(r"assets/TorlBoard/saved_data.torl", "rb")
        finaly = final.read()
        #textPad = TextPad(troot, undo=True, maxundo=-1, autoseparators=True, width=89, height=23)
        #textPad.filename = None
        #textPad.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)
        def tb_save():
                
                
                codes = str(textPad.get(1.0,END))
                file = open(r"assets/TorlBoard/saved_data.torl", "w")
                file.write(codes)
                file.close()

        ttk.Button(troot, text="Save",command=tb_save).pack(side=TOP,expand=False)

        textPad.insert("end",finaly)
        troot.mainloop()
@multitasking.task
def compiler():
        try:
                subprocess.call(["python\\Python37-32\\Scripts\\apte.bat"])
        except:
                msg("err","Error","Compiler Run Warrper was Not Found\nPlease Reinstall The Katana IDE\nERROR CODE (crnwn01)")
                return 0
@multitasking.task
def pcp():
        os.startfile("python_cp.bat")

def extensions():
        exte = tk.Tk()
        theme_system()
        exte.title('Extension Manager')

        @multitasking.task
        def install():
                root.filename = filedialog.askopenfilename(
                initialdir = '/',
                title="Select file",
                filetypes=(("Katana Extension Package","*.kep"),("Katana Support Addon","*.ksa"),("all files","*.*")))
                if root.filename==None:
                        return
                try:
                        with zipfile.ZipFile(root.filename, 'r') as zip_ref:
                                zip_ref.extractall('extensions/')
                                Label(exte, text="Installed")
                except:
                        Label(exte, text="Not Installed due to Unsupported Format")
        #def disable():
        #        root.filename = filedialog.askopenfilename(
        #        initialdir = '/',
        #        title="Select file",
        #        filetypes=(("Extension or Support Addon index file","*.esf"),("all files","*.*")))
        #        try:
        #                
        #                os.rename(root.filename, 'extensions/disable/disabled_addon.dis')
        #        except:
        #                try:
        #                        os.rename(root.filename, 'extensions/disable/da.dis')
        #                except:
        #                        os.rename(root.filename, 'extensions/disable/disabled_extension.dis')
        #        else:
        #                Label(exte, text='Save Error (Error Code: glowhole)')
        #def enable():
        #        root.filename = filedialog.askopenfilename(
        #        initialdir = '/',
        #        title="Select file",
        #        filetypes=(("Disabled Extension File","*.dis"),("all files","*.*")))
        # انشاالله اپدیت بعد
        @multitasking.task
        def uninstall():
                
                root.filename = filedialog.askopenfilename(
                initialdir = '/',
                title="Select file",
                filetypes=(("Katana Extension Package Files List","*.ini"),("all files","*.*")))
                if root.filename==None:
                        return
                fp = open(root.filename, 'r')
                listen = fp.read()
                
                for p in Path(".").glob(listen):
                        p.unlink()
        ttk.Button(exte, text='Install Extension', command=install).pack()
        #Button(exte, text='Disable Extension', command=disable).pack()
        ttk.Button(exte, text='UnInstall Extension', command=uninstall).pack()
#def extension_warpper(event=None):
#        os.chdir("extensions")
#        from bootloader import Extension_Loader
#        bootloader = Extension_Loader
#        bootloader.__init__() 
#        bootloader.load_them()
#        bootloader.stablish()
def Import_Ext(extension_name):
        init_module = "init_module.bat" -extension_name
        subprocess.call(init_module)
@multitasking.task
def explorer():
        os.chdir('tools/explorer/')
        os.startfile('external_explorer.exe')
        os.chdir("/")

def about():
        """
                This is Katana IDE About Window
        """
        msg("info","Katana IDE is Fastest and OpenSource\nCopyRight 2023 Seemon(tm)","Katana IDE is Development Enviroment For C/C++/Java/JavaScript/AMDGPU/Cuda/Python/...\nPowered By Python and Python | This IDE Uses Lowest Hardware as Can like 311mb ram and 200mhz cpu\nCurrent Version : %s" %__current__)
@multitasking.task
def new():
        textPad.delete('1.0','end')
def firework_3d():
        try:
                subprocess.call(["assets/firework_3d/main.exe"])
        except FileNotFoundError:
                msg("err","Error","Firework 3D Development Package Launcher was Not Found\nMake Sure your Katana IDE Copy was Installed Successfuly\nERROR DESCRIPTION (Firework 3D SDK was Not Found)\nERROR CODE (nheihe_01)")
                return 0
def theme_system():
        return_theme()
        global theme_used
        style = ttk.Style(root)
        if theme_used=='d_f':
                try:
                        root.tk.call('source', 'assets/theme/forest-light.tcl')
                        sset_theme('d_f')
                except:
                        style.theme_use('forest-dark')
                style.theme_use('forest-dark')

        if theme_used=='l_f':
                try:
                        root.tk.call('source', 'assets/theme/forest-light.tcl')
                        sset_theme('d_f')
                except:
                        style.theme_use('forest-light')
                style.theme_use('forest-light')

        if theme_used=='d_a':
                try:
                        root.tk.call("source", "assets/theme/azure.tcl")
                        sset_theme('d_a')
                except:
                        root.tk.call("set_theme", "dark")
                root.tk.call("set_theme", "dark")

        if theme_used=='l_a':
                try:
                        root.tk.call("source", "assets/theme/azure.tcl")
                        sset_theme('l_a')
                except:
                        root.tk.call("set_theme", "light")
                root.tk.call("set_theme", "light")

        if theme_used=='d_sv':
                set_theme("dark")
                sset_theme('d_sv')

        if theme_used=='l_sv':
                set_theme("light")
                sset_theme('l_sv')

def theme():
        global theme_used
        @multitasking.task
        def toggle_theme():
                if get_theme() == "dark":
                        use_light_theme()
                elif get_theme() == "light":
                        use_dark_theme()

        def space():
                Label(root, text='\n').pack()

        def text(text):
                Label(root,text=text).pack()
        root = tk.Tk()
        theme_system()
        root.geometry('200x425')
        root.title('Personalization')
        text("Personalization")
        space()
        ttk.Button(root, text="Random Sun Valley", command=toggle_theme).pack()
        space()
        @multitasking.task
        def d_sv():
                set_theme("dark")
                sset_theme('d_sv')
                d_svo()
        ttk.Button(root, text="Dark Sun Valley", command=d_sv).pack()
        space()
        @multitasking.task
        def l_sv():
                set_theme("light")
                sset_theme('l_sv')
                l_svo()
        ttk.Button(root, text="Light Sun Valley (BETA)", command=l_sv).pack()
        space()
        style = ttk.Style(root)

        @multitasking.task
        def d_forest():
                try:
                        root.tk.call('source', 'assets/theme/forest-light.tcl')
                        sset_theme('d_f')
                except:
                        style.theme_use('forest-dark')
                style.theme_use('forest-dark')
                d_foresto()
        ttk.Button(root, text="Dark Forest", command=d_forest).pack()
        
        space()
        @multitasking.task
        def l_forest():
                try:
                        root.tk.call('source', 'assets/theme/forest-light.tcl')
                        sset_theme('l_f')
                except:
                        style.theme_use('forest-light')
                style.theme_use('forest-light')
                l_foresto()
        ttk.Button(root, text="Light Forest", command=l_forest).pack()
        space()
        @multitasking.task
        def d_azure():
                try:
                        root.tk.call("source", "assets/theme/azure.tcl")
                        sset_theme('d_a')
                except:
                        root.tk.call("set_theme", "dark")
                root.tk.call("set_theme", "dark")
                d_azureo()
        ttk.Button(root, text="Dark Azure", command=d_azure).pack()
        space()
        @multitasking.task
        def l_azure():
                try:
                        root.tk.call("source", "assets/theme/azure.tcl")
                        sset_theme('l_a')
                except:
                        root.tk.call("set_theme", "light")
                root.tk.call("set_theme", "light")
                l_azureo()

        ttk.Button(root, text="Light Azure", command=l_azure).pack()
        space()
        root.mainloop()
@multitasking.task
def d_svo():
        set_theme("dark")
@multitasking.task
def l_svo():
        set_theme("light")
@multitasking.task
def d_foresto():
        try:
                root.tk.call('source', 'assets/theme/forest-light.tcl')
        except:
                style.theme_use('forest-dark')
        style.theme_use('forest-dark')
@multitasking.task
def l_foresto():
        try:
                root.tk.call('source', 'assets/theme/forest-light.tcl')
        except:
                style.theme_use('forest-light')
        style.theme_use('forest-light')
@multitasking.task
def l_azureo():
        try:
                root.tk.call('source', 'assets/theme/azure.tcl')
        except:
                root.tk.call("set_theme","light")
        root.tk.call("set_theme", "light")
@multitasking.task
def d_azureo():
        try:
                root.tk.call('source', 'assets/theme/azure.tcl')
        except:
                root.tk.call("set_theme","dark")
        root.tk.call("set_theme", "dark")
#@multitasking.task
#def pysql():
        
@multitasking.task
def new_cons():
        os.startfile("start_new_cons.bat")
@multitasking.task
def new_wind():
        os.startfile("run.bat")
@multitasking.task
def backup_window():
        root = tk.Tk()
        root.geometry('500x500')
        root.title('Katana IDE')

        menubar = Menu(root)

        file = Menu(menubar,tearoff = 0)
        file.add_command(label="New",command=new)
        #file.add_command(label="New window",command=new_window)
        file.add_command(label="Open",command=Open)
        file.add_command(label="Save",command=save)
        file.add_command(label="Save as", command=save_as)
        file.add_separator()
        file.add_command(label="Exit",command=exit)
        menubar.add_cascade(label="File",menu=file,font=('verdana',10,'bold'))



        edit = Menu(menubar,tearoff = 0)

        edit.add_separator()
        edit.add_command(label="Cut",command=cut)
        edit.add_command(label="Copy",command=copy)
        edit.add_command(label="Paste",command=paste)
        edit.add_command(label="Delete",command=delete)
        edit.add_command(label="Select All",accelerator="Ctrl+A",command=select_all)
        edit.add_command(label="Time/Date",accelerator="F5",command=time)
        menubar.add_cascade(label="Edit",menu=edit)


        Format = Menu(menubar, tearoff = 0)

        
        Format.add_command(label="Font...", command=fonts)

        menubar.add_cascade(label="Format",menu=Format)


        Help = Menu(menubar, tearoff = 0)

        Help.add_command(label="View Help",command=view_help)
        Help.add_command(label="Send FeedBack",command=send_feedback)
        Help.add_command(label="About Katana IDE")

        menubar.add_cascade(label="Help",menu=Help)


        root.config(menu=menubar)





        text = ScrolledText(root,width=1000,height=1000)
        text.place(x=0,y=0)



        root.mainloop()

def newp():
        root = tk.Tk()
        root.title('New Project')
        root.geometry("765x600")
        theme_system()
        text = Label(frame_bar, text="Enter Name").pack(fill=("480","300"))
        frame_bar = ttk.Frame(root)
        textp = Text(root,width=25,height=1,relief=RIDGE,font=('Seoge UI Light',10,'bold'),borderwidth=2).pack(fill=("476","300"))
        frame_bar.pack(fill=tk.BOTH, expand=True)
        @multitasking.task
        def browsef():
                __yes_or_no__ = True
                proj_directory = filedialog.asksaveasfile(mode="w",defaultextension='.json')
                if proj_directory==None:
                        return
                #print(browse_func)
        browse = ttk.Button(frame_bar, text="Browse", command=browsef)
        x = ''
        browse.pack(side=LEFT, fill=("382","300"))
        @multitasking.task
        def createp():
                global __yes_or_no__
                global proj_directory
                if __yes_or_no__==False:
                        messagebox.showwarning(title='Please Select a Folder First')

                        
                #data = {
                #'katana_project' : [
                #        {
                #               'name' : proj_name,
                #                'dir' : proj_directory,
                #                'katana_version' : 'v0.1_public_beta',
                #                'stylment' : proj_style
                #        }
                #                ]
                #}
                original = r'C:\\Users\\usr_data\\Projects\\katana.json' 
                new_project = proj_directory
                shutil.copyfile()
                #parsed = json.dump(data, parse) 
                
                
        frame_bar = ttk.Frame(root)
        frame_bar.pack(fill=tk.BOTH, expand=True)
        create = ttk.Button(frame_bar, text="Create Project",command=createp)
        create.pack(side=RIGHT, fill=tk.BOTH)
        cancel = ttk.Button(frame_bar, text="Cancel",command=root.destroy)
        cancel.pack(side=RIGHT, fill=tk.BOTH)

@multitasking.task
def Open():
        global textPad
        root.filename = filedialog.askopenfilename(
                initialdir = '/',
                title="Select file",
                filetypes=(("python source file","*.py"),("all files","*.*")))
        content = open(root.filename,'r', encoding="utf8")
        content = content.read()
        textPad.insert('end',content)
@multitasking.task
def save():
        pass
@multitasking.task
def loging(file, text):
        '''
                using namespace std;\n
                the Log Function of Katana
        '''
        if file=="summon":
                fp = open(r"debug/summon.log", "w")
                fp.write(text)
        #if file=="process":
         #       fp = open("debug/summon.log", "w")
          #      fp.write(text)
loging("process", "[  INFO  ] : Katana IDE started with code 0\n[  INFO  ] : Defualt theme 'd_sv' loaded\n[WARRNING] : detected alphaRelease version\n[  INFO  ] : loging Function started without error")                
@multitasking.task
def save_as():
        global filename_show
        loging("summon", "[ SUMMON ] : save_as summoned by user")
        root.filename = filedialog.asksaveasfile(mode="w",defaultextension='.py')
        if root.filename is None:
                return
        filename_show = root.filename
        file_save =  str(textPad.get(1.0,END))
        root.filename.write(file_save)
        root.filename.close()
@multitasking.task
def exit():
        set_theme("dark")
        message = messagebox.askquestion('Katana IDE',"Do you want to save changes")
        
        if message == "yes":{
                save_as()
        }
        if message == "no":{
                root.destroy()
        }
        else:{
                root.destroy()
        }
        
@multitasking.task
def cut():
        textPad.event_generate("<<Cut>>")
@multitasking.task
def redo():
        textPad.event_generate("<<Redo>>")
@multitasking.task
def undo():
        textPad.event_generate("<<Undo>>")

@multitasking.task
def copy():
        try:
                textPad.event_generate("<<Copy>>")
        except:
                msg("warn","Warning","Your Clipboard was Clear")

                return 0

@multitasking.task
def paste():
        textPad.event_generate("<<Paste>>")
def upbge_030():
    try:
        subprocess.call(["helper/tkinter/upbge-0.30-windows-x86_64/blender-launcher.exe"])
    except:
        msg("err","Error","UPBGE-0.30 Launch Failed - File Not Found or Graphic Card Driver is Outdated\nPlease Update Your Graphic Driver or Reinstall Katana IDE\nERROR CODE (upbge_failure01)")
        return 0
@multitasking.task
def delete():
        message = messagebox.askquestion('Katana IDE',"Do you want to Delete all")
        if message == "yes":
                textPad.delete('1.0','end')
        else:
               return "break"
@multitasking.task
def autosave(file=None):
        global textPad
        while True:
                if file==None:
                        return
                file_save =  str(textPad.get(1.0,END))
                try:
                        fp = open(file, "w")
                        fp.write(file_save)
                except:
                        msg("err","Error","Autosave Feature was ran Into Critical Error\nPlease Run Katana IDE as Administrator\nERROR CODE (autosave_01)")
                        return 0
@multitasking.task
def select_all():
        textPad.tag_add('sel','1.0','end')
        return 'break'
@multitasking.task
def run_nsav():
        try:
                subprocess.call(['run_file.bat'])
        except:
                msg("err","Error","run File Warrper was Not Found\nReinstall the Katana IDE and Try Again\nERROR CODE (rfwnf)")

@multitasking.task
def ai_programming():
        ss="ssd"

@multitasking.task
def time():  
        d = datetime.now()
        textPad.insert('end',d)
@multitasking.task
def openp():
        nothing = 'donothing'


def fonts():
        root = tk.Tk()
        theme_system()
        root.geometry('400x400')
        root.title('Font')

        l1 = Label(root,text="Font:")
        l1.place(x=10,y=10)
        f = tk.StringVar() 
        fonts = ttk.Combobox(root, width = 15, textvariable = f, state='readonly',font=('verdana',10,'bold'),) 
        fonts['values'] = font.families()
        fonts.place(x=10,y=30)
        fonts.current(0) 


        l2 = Label(root,text="Font Style:")
        l2.place(x=180,y=10)
        st = tk.StringVar() 
        style = ttk.Combobox(root, width = 15, textvariable = st, state='readonly',font=('verdana',10,'bold'),) 
        style['values'] = ('bold','bold italic','italic')
        style.place(x=180,y=30)
        style.current(0) 

        l3 = Label(root,text="Size:")
        l3.place(x=350,y=10)
        sz = tk.StringVar() 
        size = ttk.Combobox(root, width = 2, textvariable = sz, state='readonly',font=('verdana',10,'bold'),) 
        
        size['values'] = (8,9,10,12,15,20,23,25,27,30,35,40,43,47,50,55,65,76,80,90,100,150,200,255,300)
        size.place(x=350,y=30)
        size.current(0) 
               
              
        sample = LabelFrame(root,text="Sample",height=100,width=200)
        sample['font'] = (fonts.get(),size.get(),style.get())
        sample.place(x=180,y=220)

        l4 = Label(sample,text="This is sample")
        l4.place(x=20,y=30)



        def OK():

               textPad['font'] = (fonts.get(),size.get(),style.get())
               selected_font = fonts.get()
               size = size.get()
               noe = style.get()
               root.destroy()
               
        ok = ttk.Button(root,text="OK",relief=RIDGE,borderwidth=2,padx=20,highlightcolor="blue",command=OK)
        ok.place(x=137,y=350)

        def Apl():
                l4['font'] = (fonts.get(),size.get(),style.get())
                selected_font = fonts.get()
                size = size.get()
                noe = style.get()
        Apply = ttk.Button(root,text="Apply",relief=RIDGE,borderwidth=2,padx=20,highlightcolor="blue",command=Apl)
        Apply.place(x=210,y=350)        

        def Cnl():
                root.destroy()

        cancel = ttk.Button(root,text="Cancel",relief=RIDGE,borderwidth=2,padx=20,command=Cnl)
        cancel.place(x=295,y=350)
        root.mainloop()
@multitasking.task
def example():
        subprocess.call("template.bat")
@multitasking.task
def view_help():
        webbrowser.open('seemon.ir')

@multitasking.task
def send_feedback():
        webbrowser.open('seemon.ir')
WINDOW_TITLE = "Katana IDE Beta_23.04"
WINDOW_MINSIZE = (1080, 768)
WINDOW_POSITION = (800, 600)
root = Tk()
frame1 = ttk.Frame(root)
root.configure(bg="#000000")
root.overrideredirect(False)

root.minsize(WINDOW_MINSIZE[0], WINDOW_MINSIZE[1])
root.geometry(str(WINDOW_MINSIZE[0]) + "x" + str(WINDOW_MINSIZE[1]) + "+" + str(WINDOW_POSITION[0]) + "+" + str(WINDOW_POSITION[1]))
root.title('Katana IDE Beta_23.04')
#photo = PhotoImage(file = 'feather.gif')
#root.wm_iconphoto(False, photo)
selected_font = ""
size = '10'
noe = 'bold'
#from BlurWindow.blurWindow import *
import sun_valley_titlebar
HWND = os.getpid()
style = ttk.Style(root)
menubar = sun_valley_titlebar.Menubar(root)
notebook = ttk.Notebook(frame1)
notebook.pack(expand=True,fill=tk.BOTH)


@multitasking.task


def ojnb():
        try:
                subprocess.call(["ojnb.bat"])
        except:
                loging("summon", "[  ERROR  ] : file 'ojnb.bat' on disk not found ,may be deleted")

@multitasking.task
def gitc():
        """
                _summary_
                git clone function for Katana IDE
                usage in menubar

        """
        root = tk.Tk()

        root.geometry("400x200")
        root.minsize(400,200)
        root.maxsize(400,200)
        root.title("Git Window")
        def work():
                url = str(url_text.get(1.0,END))
                fp = open(r"dire.ini", 'w')
                fp.write(url)
                subprocess.call(["git.bat"])
        url_text = Text(root,width=50,height=5,relief=RIDGE,font=('Seoge UI Light',10,'bold'),borderwidth=2).pack(side=LEFT)
        ttk.Button(root,text="Clone",command=work).pack(side=RIGHT)
        root.mainloop()


ie = False



@multitasking.task
def djago():
        """
                _summary_
                django project create function for Katana IDE
                useage in menubar

        """
        git = tk.Tk()
        theme_system()
        if null=='null':
                root.filename = filedialog.asksaveasfile(mode="w",defaultextension='.txt')
        git.geometry('200x89')
        git.minsize(200,89)
        git.maxsize(200,89)
        git.title('Django Project Create')
        textp = Text(git,width=3,height=1,relief=RIDGE,font=('Seoge UI Light',10,'bold'),borderwidth=2)
        textp.place(x=200,y=75)
        textp.pack()
        def create_django():
                dir = filedialog.askdirectory()

                name = str(textp.get(1.0,END))
                args = "django.bat " + dir
                subprocess.call(args)
        package = ''
        install = ttk.Button(git,text='Create',command=create_django)
        install.place(x=0,y=0)
        install.pack()
@multitasking.task
def none():
        None

def page():
        subprocess.call(["assets\\page\\page.bat"])


frame1.pack(fill=tk.BOTH, expand=True)
class TextLineNumbers(tk.Canvas):
    def __init__(self, *args, **kwargs):
        tk.Canvas.__init__(self, *args, **kwargs)
        self.textwidget = None

    def attach(self, text_widget):
        self.textwidget = text_widget
        
    def redraw(self, *args):
        '''redraw line numbers'''
        self.delete("all")

        i = self.textwidget.index("@0,0")
        while True :
            dline= self.textwidget.dlineinfo(i)
            if dline is None: break
            y = dline[1]
            linenum = str(i).split(".")[0]
            self.create_text(2,y,anchor="nw", text=linenum)
            i = self.textwidget.index("%s+1line" % i)
def on_change(root):
        TextLineNumbers.redraw()
textPad = CodeView(frame1, lexer=lexers.PythonLexer)
textPad.bind("<<Change>>", on_change)
textPad.bind("<Configure>", on_change)
textPad.pack(side=tk.RIGHT, expand=True,fill=tk.BOTH)


frame2 = ttk.Frame(root)
frame2.pack(side='bottom', fill=BOTH)
ttk.Button(frame2,text='Open',command=Open).pack(side=tk.RIGHT)
Label(frame2,text='Evulution.Preview-23.04.01\nCopyright 2023 Seemon(tm)').pack(side=tk.LEFT)
terminal = Terminal(root, bd=0, width=50, height=23)
terminal.pack()

def use_theme_hub(wana):
        if wana=="d_sv":
                d_svo()
        if wana=="l_sv":
                l_svo()
        if wana=="d_a":
                d_azureo()
        if wana=="l_a":
                l_azureo()
        if wana=="d_f":
                d_foresto()
        if wana=="l_f":
                l_foresto()
        if wana=="random":
                themes = ['d_sv','l_sv','d_a','l_a','d_f','l_f']
                randome = random.choice(themes)
                use_theme_hub(randome)
        else : {
                print("BOMB BOMB BOMB BOMB BOMB BOMB BOMB BOMB BOMB BOMB BOMB BOMB BOMB BOMB BOMB BOMB BOMB BOMB BOMB BOMB BOMB BOMB")
        }
def sset_theme(theme):
        fp = open(r"assets/theme/used_theme.kut","w")
        fp.write(theme)
        theme_system()
filename = None
@multitasking.task
def return_theme():
        global theme_used
        fp = open(r"assets/theme/used_theme.kut","r")
        theme_used = fp.read()
        fp.close()

def load_theme_on_statup():
        """
                Loading the Theme...
        """
        def __load_theme__(themed):
                sset_theme(themed)
                theme_system()
        fp = open(r"assets/theme/used_theme.kut","r")
        theme_used = fp.read()
        __load_theme__(theme_used)
frame3 = TextLineNumbers(frame1, width=30)
frame3.pack(side="left", fill="x")

load_theme_on_statup()
 


def windows_env():
        a = "donothing"
def linux_env():
        a = "donothing"
def android_env():
        a = "donothing"
def ios_env():
        a = "donothing"


        
file = sun_valley_titlebar.Menu(menubar,"File")
#file.add_command(label="New Project",command=newp)
file.add_command("New Python File", new)
file.add_command("New Django Project", djago)
file.add_command("Open",Open)
#file.add_command(label="Open Project",command=openp)
file.add_command("Open Console Window", new_cons)
file.add_command('Open New Window', new_wind)
file.add_command("Save",save)
file.add_command("Save as", save_as)
file.add_separator()
file.add_command("Exit",exit)

editd = sun_valley_titlebar.Menu(menubar,"Development Options")
editd.add_command("Compile",compiler)
editd.add_command("Install Package",pip)
editd.add_command("Git Clone",gitc)
itk_data = """
import tkinter as tk
form tkinter import *
"""
ittk_data = """
import tkinter as tk
from tkinter import *
from tkinter import ttk
"""
hl2_exa1 = """
# *Katana Clasic* #
#^initilize_hl2_eng^#

import Hl2Engine
from Hl2Engine import *

Engine = Hl2Engine.begin(name=" Python HL2 Port ",dir_name="./games/pyhl2",gui=Hl2Engine.VGUI,platform=("Windows")) #Gets The Required Informations (You Can Set Custom GUI For Your Game)
Engine.init() #Init Engine
Engine.init_dir() #Copys The Required Files in The Game Dir 

@Hl2Engine.function
def test(Point): #Initilize's The Game Resources and GUI
    global Engine
    background = Engine.gui.Load_backmap("./games/pyhl2/maps/Background01.bsp","./games/pyhl2/maps/Background02.bsp","./games/pyhl2/maps/Background03.bsp","./games/pyhl2/maps/Background04.bsp","./games/pyhl2/maps/Background05.bsp") #Loads The Bakcground Maps For GUI 
    Engine.gui.backmap_init(background)
    Engine.gui.init_buttons()
    if Point=="True":
        Engine.mainloop()
test(Point=True) #Starts The Game Loop
"""
hl2_exa2 = """
# *Katana Clasic* #
#^initilize_hl2_eng^#

import Hl2Engine
from Hl2Engine import *

Engine = Hl2Engine.begin(name=" Python HL2 Port ",dir_name="./games/pyhl2",gui=Hl2Engine.VGUI,platform=("Windows")) #Gets The Required Informations (You Can Set Custom GUI For Your Game)
Engine.init() #Init Engine
Engine.init_dir() #Copys The Required Files in The Game Dir 

@Hl2Engine.function
def test(Point): #Initilize's The Game Resources and GUI
    global Engine
    Engine.Set(style="Benchmark") #Sets The Game Style to Benchmark Type
    Engine.gui.init_buttons()
    bench = Engine.load_map("./games/pyhl2/maps/sysTest.bsp") #Loads Benchmark Map
    Engine.init_map(bench) #Init's Map
    if Point=="True":
        Engine.mainloop()
test(Point=True) #Starts The Game Loop
"""

patlate = sun_valley_titlebar.Menu(menubar,"PreWrited Syntax")
patlate.add_command("Add Comment to Line",lambda : textPad.insert("insert","#"))
patlate.add_command("print",lambda : textPad.insert("insert","print('msg')"))
patlate.add_command("Input",lambda : textPad.insert("insert","data = input('msg')"))
patlate.add_command("Open File",lambda : textPad.insert("insert","fp = open(r'your file location','select a mode like w')"))
patlate.add_command("Import Themed Tkinter",lambda : textPad.insert("insert",ittk_data))
patlate.add_command("Import Tkinter",lambda : textPad.insert("insert",itk_data))
#patlate.add_command("Import HL2_Engine",lambda : textPad.insert("insert",hl2_eng))
patlate.add_command("Tkinter Themed Frame",lambda : textPad.insert("insert","myframe = ttk.Frame(root).pack()"))
patlate.add_command("Tkinter Window",lambda : textPad.insert("insert","root = tk.Tk()"))
patlate.add_command("Tkinter Button",lambda : textPad.insert("insert","Button(root,label='msg').pack()"))
patlate.add_command("Themed Tkinter Button",lambda : textPad.insert("insert","ttk.Button(root,label='msg').pack()"))
patlate.add_command("HL2_Engine Example 1",lambda : textPad.insert("insert",hl2_exa1))
patlate.add_command("HL2_Engine Example 2",lambda : textPad.insert("insert",hl2_exa2))
#patlate.add_command("Import From Examples",lambda : textPad.insert("insert",exa_import))

editd.add_command("Examples", example)
editd.add_command("Open Torl Board",torlboard)
editd.add_command("Create Virtual Enviroment",venv_create)
editd.add_command("Manage Extensions", extensions)
editd.add_command("Create GUI With Glade-3", glade)
editd.add_command("Create GUI With PAGE Builder",page)
run_code = sun_valley_titlebar.Menu(menubar,"Run")
run_code.add_command("Run",run)
run_code.add_command("Run Without Save", run_nsav)

def c(ass):
        textPad.insert("insert","'")
def dc(ass):
        textPad.insert("insert",'"')
def p(ass):
        textPad.insert("insert",")")
def cb(ass):
        textPad.insert("insert","}")
def cshe(ass):
        textPad.insert("insert","]")
def coose(ass):
        textPad.insert(tk.CURRENT,">")
def ss(ass):
        textPad.insert("insert","\\")
computer = wmi.WMI()
gpu_info = computer.Win32_VideoController()[0]
def render_window():
        try:
                Main().mainloop()
        except:
                msg("err","Error While Running XEN-Render","an Unknown Exception was Handled in Katana IDE Thread\nPlease Restart The Katana IDE For Solve The Problem\nIf This Error Returned Many Times, Please Contact Developers with parsaaslani.67@cmon.com\nERROR CODE (exception_08)")
                return 0
def serv_run():
        try: subprocess.call(["helper/cli/hotbird/serv_run.bat"])
        except FileNotFoundError:
                msg("err","Fatal Error","Katana IDE was ran into Fatal Error while Running The Hotbird Server Side\nMake Sure the Katana IDE was Installed Successfully\n\nThe System cannot find 'serv_run.bat'\nERROR CODE (hb_serv_notfound)")
                return 0
        except PermissionError:
                msg("warn","Warning","Permisions for Running Server Side of Hotbird Connected Not Allowed\nPlease Run The Katana IDE as Administrator\nWARNING CODE (permision_not_alowed)")
                return 0
def clie_run():
        try: subprocess.call(["helper/tkinter/hotbird/client_run.bat"])
        except FileNotFoundError:
                msg("err","Fatal Error","Katana IDE was ran into Fatal Error while Running The Hotbird Client Side\nMake Sure the Katana IDE was Installed Successfully\n\nThe System cannot find 'client_run.bat'\nERROR CODE (hb_client_notfound)")
                return 0
        except PermissionError:
                msg("warn","Warning","Permisions for Running Client Side of Hotbird Connected Not Allowed\nPlease Run The Katana IDE as Administrator\nWARNING CODE (permision_not_alowed)")
                return 0
#Atention : DONT FUCK THIS CODES FOR ANY REASONS 'a note from q'
VideoMem_min = -2147483648
VideoDriver_revision = gpu_info.DriverVersion;
edit = sun_valley_titlebar.Menu(menubar,"Edit")
edit.add_command("Undo",undo)
edit.add_command("Redo",redo)
edit.add_separator()

edit.add_command("Cut",cut)
edit.add_command("Copy",copy)
edit.add_command("Paste",paste)
edit.add_command("Delete",delete)
edit.add_command("Select All",select_all)
edit.add_command("Time/Date",time)
Format = sun_valley_titlebar.Menu(menubar,"Format")
theme = sun_valley_titlebar.Menu(menubar,"Theme")
theme.add_command("Theme Changes will be Applyed until You Restarted The Katana")
theme.add_command("Dark Sun Valley",lambda :
        sset_theme('d_sv'))
theme.add_command("Light Sun Valley",lambda :
        sset_theme('l_sv'))
theme.add_command("Dark Azure",lambda :
        sset_theme('d_a'))
theme.add_command("Light Azure",lambda :
        sset_theme('l_a'))
theme.add_command("Dark Forest",lambda :
        sset_theme('d_f'))
theme.add_command("Light Forest",lambda :
        sset_theme('l_f'))
theme.add_command("Random",lambda :
        sset_theme("random"))
Format.add_command("Auto Save", lambda : autosave(file=filename))
#Format.add_command(label='Show Clipboard',command=clipboard)
Format.add_command("Open Jupyter Notebook",ojnb)

Format.add_command("Python Command Prompt", pcp)
Format.add_command("Font...", fonts)
advanced = sun_valley_titlebar.Menu(menubar,"Advanced")
if pt.system() == "Windows":
        advanced.add_command("Linux Enviroment",linux_env)
if pt.system() == "Linux":
        advanced.add_command("Windows Enviroment",windows_env)
advanced.add_command("Android Enviroment",android_env)
advanced.add_command("Run Hotbird Server",lambda : serv_run())
advanced.add_command("KatanaGPT",lambda : KatanaGPT())
advanced.add_command("Run Hotbird Client",lambda : clie_run())
advanced.add_command("iOS Enviroment",ios_env)
if VideoMem_min == gpu_info.AdapterRAM:
        version = null
        
        for VideoDriver_revision in version:
                if version == none:
                        msg("warn","Warning","Warning - Your Graphic Card Driver is Outdated and Cannot be Used\nPlease Update your Driver\nCurrent Version : %s"%version)
        advanced.add_command(label="Render 3D Model",command=render_window)
hotbird = (menubar,"Hotbird Connected")
advanced = (menubar,"Advanced Options")
Format = (menubar,"Format")
@multitasking.task
def KatanaGPT():
        from helper import KatanaGPT
        from helper.KatanaGPT import ChatWindow
        if __name__ == '__main__':
            app = QtWidgets.QApplication(sys.argv)
            window = ChatWindow()
            window.show()
            sys.exit(app.exec())
        

Help = sun_valley_titlebar.Menu(menubar,"Help")

Help.add_command("View Help",view_help)
Help.add_command("Send FeedBack",send_feedback)
Help.add_command("About Katana",about)


#def detect_lib(library_name):
#    os.scandir("../","./","%s/AppData/Local/Programs/Python"%USERS)

m = Menu(root, tearoff = 0)
m.add_command(label ="Select All",accelerator="Ctrl+A",command=select_all) 
m.add_command(label ="Cut",accelerator="Ctrl+X",command=cut) 
m.add_command(label ="Copy",accelerator="Ctrl+C",command=copy) 
m.add_command(label ="Paste",accelerator="Ctrl+V",command=paste) 
m.add_command(label ="Delete",accelerator="Del",command=delete) 
m.add_separator() 

m.add_command(label ="Undo",accelerator="Ctrl+Z",command=undo)
m.add_command(label ="Redo",accelerator="Ctrl+Z",command=redo)
m.add_separator() 
m.add_command(label ="Run",accelerator="Ctrl+LShift+R",command=run)
m.add_command(label ="Examples",command=example)
@multitasking.task
def easter_egg():
        root.bind("<stdio3_goto_secret>",begin)
        def begin():
                msg("info","Secret about Katana IDE","HAPPYEST DAY!\nyou have found the secret key\nThe Real Creator of Katana IDE is Parsa Aslani!\nCan i Hear You\nERROR CODE (null)")
                return 0
data = """
# Pick a Licence Like "MIT","GPL-3"
# Import Your Packages Like "matplotlib","numpy","tkinter","PySide2"
# Import the Katana Lib Like "import klib"
# And Write Your Codes
# <coding type "UTF-8">
"""
#def load_lib():
#        try:
#                from lib import klib
#
#        except ImportError:
#                msg("err","Error","Katana IDE Cannot Import klib\nMake Sure Your Katana IDE copy was Installed Complete\nERROR CODE (kilib_01)")
#                return 0     

@multitasking.task
def do_popup(event): 
    try:
        m.tk_popup(event.x_root, event.y_root) 
    finally: 
        m.grab_release()
root.bind("<'>",c)
root.bind('<">',dc)
root.bind("<(>",p) 
root.bind("<{>",cb)
root.bind("<[>",cshe)
root.bind("<s-t-d-i-o-3")
root.bind("<\\>",ss)

root.bind("<Button-3>", do_popup) 
load_theme_on_statup()
root.config(menu=menubar)

def mainlooped():
        for i in range(999999999999999999999999999999999999999999999999999999999999999999999999999999999):
                try:
                        root.mainloop()
                except:
                        try:
                                root.mainloop()
                        except:
                                try:
                                        root.mainloop()
                                except:
                                        try:
                                                root.mainloop()
                                        except:
                                                try:
                                                        root.mainloop()
                                                except:
                                                        try: root.mainloop()
                                                        except : 
                                                                try: root.mainloop() 
                                                                except: 
                                                                        try: root.mainloop() 
                                                                        except: root.mainloop()
if __name__=="__main__":
    mainlooped()


