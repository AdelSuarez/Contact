import tkinter as tk
from style import style
from db.update_contact_select import Update_contact_select

class Edit_window:
    def __init__(self, tree, selection):
        self._selection = selection
        self._tree = tree
        self.init_widgets()
        self.v()


    def init_widgets(self):
        self.win_edit = tk.Toplevel()
        self.settings()

        self.option_frame = tk.Frame(self.win_edit)
        self.option_frame.columnconfigure(0, weight=1)
        self.option_frame.columnconfigure(1, weight=1)

        tk.Label(self.option_frame, text='Nuevo nombre:').grid(row=0, column=0, sticky=tk.W)
        self.new_name = tk.Entry(self.option_frame, width=30)
        self.new_name.grid(row=0, column=1, sticky=tk.NSEW)
        
        tk.Label(self.option_frame, text='Nuevo numero: ').grid(row=1, column=0, sticky=tk.W)
        self.new_phone = tk.Entry(self.option_frame, width=30)
        self.new_phone.grid(row=1, column=1, sticky=tk.NSEW, pady=5)
        
        tk.Label(self.option_frame, text='Nuevo correo: ').grid(row=2, column=0, sticky=tk.W)
        self.new_email = tk.Entry(self.option_frame, width=30)
        self.new_email.grid(row=2, column=1, sticky=tk.NSEW)
        
        self.option_frame.grid(row=0, column=0, pady=10, padx=10, sticky=tk.NSEW)

        self.container_button = tk.Frame(self.win_edit)
        self.container_button.columnconfigure(0, weight=1)
        self.container_button.columnconfigure(1, weight=1)
        
        tk.Button(self.container_button, text='Guardar', **style.button_style_save, command=lambda:print('Guardando')).grid(row=0, column=0, sticky=tk.NSEW, padx=10)
        tk.Button(self.container_button, text='Cancelar', **style.button_style_delete, command=lambda:self.win_edit.destroy()).grid(row=0, column=1, sticky=tk.NSEW, padx=10)

        self.container_button.grid(row=1, column=0, sticky=tk.NSEW, padx=10, pady=10)

    def settings(self):
        self.win_edit.resizable(0, 0)
        self.win_edit.columnconfigure(0, weight=1)
        self.win_edit.rowconfigure(0, weight=1)
        self.win_edit.columnconfigure(1, weight=1)
        self.win_edit.rowconfigure(1, weight=1)
        self.win_edit.title('Editar contacto')

    def v(self):
        if self._selection == 'selection':
            Update_contact_select(self.new_name, self.new_phone, self.new_email, self._tree)
        elif self._selection== 'view':
            print('view')





