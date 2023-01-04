import tkinter as tk
from tkinter import ttk

try:
    from modules.settings import *
except ModuleNotFoundError:
    from settings import *

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
        tabControl.add(tab3, text="Franken Movie")
        tabControl.add(tab4, text="Movie Scalpel")

        tabControl.pack(expand=1, fill="both")

        # Settings tab
        root_dir_label = ttk.Label(tab1, text="root_dir")
        root_dir_label.grid(column=0, row=0, padx=30, pady=30)
        root_dir_input = ttk.Entry(tab1)
        root_dir_input.insert(0, root_dir)

        root_dir_input.grid(column=1, row=0, padx=30, pady=30)


root = tk.Tk()
content = ChopperView(root)

root.geometry("800x600+10+10")
root.mainloop()
