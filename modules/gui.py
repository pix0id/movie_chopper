import tkinter as tk
from tkinter import ttk
# https://www.geeksforgeeks.org/creating-tabbed-widget-with-python-tkinter/
# https://www.tutorialsteacher.com/python/create-gui-using-tkinter-python
class ChopperView:
    def __init__(self, win):
        """Create window and inputs"""
        win.title("Movie Chopper Utilities")

        tabControl = ttk.Notebook(win)
        tab1 = ttk.Frame(tabControl)
        tab2 = ttk.Frame(tabControl)
        tab3 = ttk.Frame(tabControl)
        tab4 = ttk.Frame(tabControl)

        tabControl.add(tab1, text="Settings")
        tabControl.add(tab2, text="Movie Chopper")
        tabControl.add(tab3, text="Movie FrankenMovie")
        tabControl.add(tab4, text="Movie Scalpel")

        tabControl.pack(expand=1, fill="both")


root=tk.Tk()
mywin=ChopperView(root)

root.geometry("800x600+10+10")
root.mainloop()
