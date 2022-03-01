from cProfile import label
from distutils import command
from tkinter import Toplevel

import tkinter as tk

from sqlalchemy import column

class Edit_window:
    def __init__(self):
        self.win_edit = tk.Toplevel()
        self.win_edit.title('Editar contacto')
        self.win_edit.resizable(0, 0)
        self.win_edit.columnconfigure(0, weight=1)
        self.win_edit.rowconfigure(0, weight=1)
        self.win_edit.columnconfigure(1, weight=1)
        self.win_edit.rowconfigure(1, weight=1)


        self.option_frame = tk.Frame(self.win_edit)
        self.option_frame.columnconfigure(0, weight=1)
        self.option_frame.columnconfigure(1, weight=1)

        tk.Label(self.option_frame, text='Nombre:').grid(row=0, column=0, sticky=tk.W)
        tk.Entry(self.option_frame).grid(row=0, column=1, sticky=tk.NSEW)


        tk.Label(self.option_frame, text='Nuevo nombre:').grid(row=1, column=0, sticky=tk.W)
        tk.Entry(self.option_frame).grid(row=1, column=1, sticky=tk.NSEW)

        tk.Label(self.option_frame, text='Numero: ').grid(row=2, column=0, sticky=tk.W)
        tk.Entry(self.option_frame, width=30).grid(row=2, column=1, sticky=tk.NSEW)
        
        tk.Label(self.option_frame, text='Nuevo numero: ').grid(row=3, column=0, sticky=tk.W)
        tk.Entry(self.option_frame).grid(row=3, column=1, sticky=tk.NSEW)

        tk.Label(self.option_frame, text='Correo: ').grid(row=4, column=0, sticky=tk.W)
        tk.Entry(self.option_frame).grid(row=4, column=1, sticky=tk.NSEW)
        
        tk.Label(self.option_frame, text='Nuevo correo: ').grid(row=5, column=0, sticky=tk.W)
        tk.Entry(self.option_frame).grid(row=5, column=1, sticky=tk.NSEW)
        
        self.option_frame.grid(row=0, column=0, pady=10, padx=10, sticky=tk.NSEW)

        self.container_button = tk.Frame(self.win_edit)
        self.container_button.columnconfigure(0, weight=1)
        self.container_button.columnconfigure(1, weight=1)
        
        tk.Button(self.container_button, text='Guardar', command=lambda:print('Guardando')).grid(row=0, column=0, sticky=tk.NSEW, padx=10)
        tk.Button(self.container_button, text='Cancelar', command=lambda:self.win_edit.destroy()).grid(row=0, column=1, sticky=tk.NSEW, padx=10)

        self.container_button.grid(row=1, column=0, sticky=tk.NSEW, padx=10, pady=10)


