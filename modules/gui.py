import tkinter as tk
from tkinter import ttk

try:
    from modules.settings import *
except ModuleNotFoundError:
    from settings import *

# https://www.geeksforgeeks.org/creating-tabbed-widget-with-python-tkinter/
# https://www.tutorialsteacher.com/python/create-gui-using-tkinter-python
root = tk.Tk()

class ChopperView:
    def __init__(self, win):
        self.win = win
        pass
    def initialize_user_interface(self):
        """Create window and inputs"""
        self.win.title("Movie Chopper Utilities")

        tabControl = ttk.Notebook(self.win)
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
        root_dir_label.grid(column=0, row=0, padx=5, pady=5)

        root_dir_input = ttk.Entry(tab1)
        root_dir_input.insert(0, ROOT_DIR)
        root_dir_input.grid(column=1, row=0, padx=5, pady=5)

        length_label = ttk.Label(tab1, text="Length")
        length_label.grid(column=0, row=1, padx=5, pady=5)

        length_label = ttk.Entry(tab1)
        length_label.insert(0, LENGTH)
        length_label.grid(column=1, row=1, padx=5, pady=5)

        # uniform_size_label = ttk.Label(tab1, text="Uniform Size Clips")
        # uniform_size_label.grid(column=0, row=2, padx=5, pady=5)
        #TODO: change boolean values to checkboxes
        uniform_size_value = tk.BooleanVar
        uniform_size_value.set(root, value=bool(UNIFORM_SIZE))
        uniform_size_input = ttk.Checkbutton(tab1, variable=uniform_size_value, text="Uniform Height/Width", onvalue=True, offvalue=False, command=printValue)
        uniform_size_input.grid(column=1, row=2, padx=5, pady=5)

        def printValue(self, val):
            print(val)



content = ChopperView(root)

root.geometry("800x600+10+10")
root.mainloop()
