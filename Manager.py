import tkinter as tk
from screen.Main_window import Main_windows

class Manager(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self._master = master
        self.window_settings()
        self.pack(expand=True, fill=tk.BOTH)

        Main_windows(self)
    
    def window_settings(self):
        self._master.title('APP Contacto')
        self._master.resizable(0, 0)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)


    
