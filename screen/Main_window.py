from db.add_contact import Add_contact
from db.get_all_contacts import Get_all_contacts
import tkinter as tk
from tkinter import CENTER, ttk
from style import style
from PIL import ImageTk, Image
from db.get_all_contacts import Get_all_contacts

class Main_windows(tk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init_widgets()
        self.window_settings()
        self.grid(row=0, column=0, sticky=tk.NSEW)


    def init_widgets(self):
        self.frame_contact = tk.Frame(self)
        self.frame_contact.columnconfigure(0, weight=1)
 
        # - Inputs -
        self.container_inputs = tk.LabelFrame(self.frame_contact, text='Nuevo contacto')
        self.container_inputs.columnconfigure(1, weight=1)

        # Text inputs
        name_label = tk.Label(self.container_inputs, text='Nombre: ')
        name_label.grid(row=0, column=0, sticky=tk.NSEW)
        self.new_name = tk.Entry(self.container_inputs, width=20, )
        self.new_name.focus()
        self.new_name.grid(row=0, column=1, padx=5, sticky=tk.NSEW)

        phone_label = tk.Label(self.container_inputs, text='Telefono: ')
        phone_label.grid(row=1, column=0, sticky=tk.NSEW, padx=5)
        self.phone = tk.Entry(self.container_inputs, width=20)
        self.phone.grid(row=1, column=1, padx=5, pady=5, sticky=tk.NSEW)

        tk.Label(self.container_inputs, text='Email: ').grid(row=2, column=0, sticky=tk.NSEW)
        self.email = tk.Entry(self.container_inputs, width=20)
        self.email.grid(row=2, column=1, padx=5, sticky=tk.NSEW)

        tk.Button(self.container_inputs, text='Guardar', **style.button_style, relief=tk.FLAT, overrelief=tk.RAISED, fg='#FFF', activeforeground='#FFF', activebackground='#006600', bg='#008000', command=lambda:Add_contact(self.new_name, self.phone, self.email, name_label, phone_label, self.tree)).grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky=tk.NSEW)

        self.container_inputs.grid(row=0, column=0, pady=10, padx=10, sticky=tk.NSEW)
        # ------------------------------------------------------------------------------
        # - Separator -
        ttk.Separator(self.frame_contact, orient='horizontal').grid(row=2, column=0, pady=10, sticky=tk.NSEW)

        # - Contact display -
        self.container_contact = tk.LabelFrame(self.frame_contact, text='Contacto')
        self.container_contact.columnconfigure(1, weight=1)
        
        self.container_name = tk.LabelFrame(self.container_contact, text='Nombre: ')
        self.container_name.columnconfigure(0, weight=1)
        tk.Label(self.container_name, text='').grid(row=0, column=0)
        self.container_name.grid(row=0, column=0, padx=20, sticky=tk.NSEW, columnspan=2)
        
        tk.Label(self.container_contact, text='Número: ').grid(row=1, column=0, padx=20, sticky=tk.W)
        tk.Label(self.container_contact, text='Email: ').grid(row=2, column=0, padx=20, sticky=tk.W)

        self.container_buttons = tk.Frame(self.container_contact)
        self.container_buttons.columnconfigure(0, weight=1)
        self.container_buttons.columnconfigure(1, weight=1)

        tk.Button(self.container_buttons, text='Editar', **style.button_style, relief=tk.FLAT, overrelief=tk.RAISED, fg='#FFF', activeforeground='#FFF', activebackground='#cc8400' , bg='#FFA500', command=lambda:Get_all_contacts(self.tree), width=10).grid(row=0, column=0, padx=5, sticky=tk.NSEW)

        tk.Button(self.container_buttons, text='Eliminar', **style.button_style, relief=tk.FLAT, overrelief=tk.RAISED, fg='#FFF', activeforeground='#FFF', activebackground='#cc0000' , bg='#FF0000', command=lambda:print('eliminar'), width=10).grid(row=0, column=1, padx=5, sticky=tk.NSEW)
        
        self.container_buttons.grid(row=4, column=0, columnspan=2, pady=5, sticky=tk.NSEW)
        self.container_contact.grid(row=3, column=0, sticky=tk.NSEW, padx=10)
        # ----------------------------------------------------------------------

        self.logo_img = ImageTk.PhotoImage(Image.open("img/search.jpg").resize((25, 25), Image.ANTIALIAS))

        # - Search -
        self.container_search = tk.Frame(self.frame_contact)
        self.container_search.columnconfigure(0, weight=1)
        
        self.search = tk.Entry(self.container_search)
        self.search.grid(row=0, column=0, padx=5, sticky=tk.NSEW)
        tk.Button(self.container_search, image=self.logo_img, bd=0, command=lambda:print('buscando')).grid(row=0, column=1, padx=5, sticky=tk.NSEW)

        self.container_search.grid(row=4, column=0, pady=15, padx=10, sticky=tk.NSEW)

        self.frame_contact.grid(row=0, column=0, padx=10, sticky=tk.NSEW )
        #  ------------------------------------------------------------------------------
        
        # - Separator -
        ttk.Separator(self, orient='vertical').grid(row=0, column=1, pady=10, sticky=tk.NSEW)


        # - Table -
        self.table = tk.Frame(self)
        self.table.rowconfigure(0, weight=1)
        self.table.columnconfigure(0, weight=1)
        

        self.tree = ttk.Treeview(self.table, columns=2)
        self.tree.heading('#0', text='Nombre', anchor='center')
        self.tree.heading('#1', text='Número', anchor='center')
        self.tree.column('#1', anchor='center', stretch=0)

        self.tree.grid(row=0, column=0, pady=10, padx=10, sticky=tk.NSEW)
        
        self.table.grid(row=0, column=2, sticky=tk.NSEW)

        Get_all_contacts(self.tree)

    
    def window_settings(self):
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, minsize=300)
        self.columnconfigure(1, weight=1)

