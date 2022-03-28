from db.add_contact import Add_contact
from components.get_all_contacts import Get_all_contacts
from db.select_contact_view import Select_contact_view
from db.delete_contact_select import Delete_contact_select
from db.delete_contact_view import Delete_contact_view
from db.update_contact_select import Update_contact_select
from db.search_contact import Search_contact
from components.clear_view import Clear_view
from screen.Edit_windows import Edit_window
import tkinter as tk
from tkinter import StringVar, ttk
from style import style
from PIL import ImageTk, Image

class Main_windows(tk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init_widgets()
        self.window_settings()
        self.grid(row=0, column=0, sticky=tk.NSEW)


    def init_widgets(self):
        self.logo_img_search = ImageTk.PhotoImage(Image.open("img/search.jpg").resize((25, 25), Image.ANTIALIAS))
        self.logo_img_delete = ImageTk.PhotoImage(Image.open("img/delete.jpg").resize((25, 25), Image.ANTIALIAS))
        self.logo_img_edit = ImageTk.PhotoImage(Image.open("img/edit.png").resize((25, 25), Image.ANTIALIAS))

        self.frame_contact = tk.Frame(self)
        self.frame_contact.columnconfigure(0, weight=1)
 
        # - Inputs -
        self.container_inputs = tk.LabelFrame(self.frame_contact, text='Nuevo contacto')
        self.container_inputs.columnconfigure(1, weight=1)

        # Text inputs
        name_label = tk.Label(self.container_inputs, text='Nombre: ')
        name_label.grid(row=0, column=0, sticky=tk.NSEW)
        self.new_name = tk.Entry(self.container_inputs, width=20)
        self.new_name.focus()
        self.new_name.grid(row=0, column=1, padx=5, sticky=tk.NSEW)

        phone_label = tk.Label(self.container_inputs, text='Telefono: ')
        phone_label.grid(row=1, column=0, sticky=tk.NSEW, padx=5)
        self.phone = tk.Entry(self.container_inputs, width=20)
        self.phone.grid(row=1, column=1, padx=5, pady=5, sticky=tk.NSEW)

        tk.Label(self.container_inputs, text='Email: ').grid(row=2, column=0, sticky=tk.NSEW)
        self.email = tk.Entry(self.container_inputs, width=20)
        self.email.grid(row=2, column=1, padx=5, sticky=tk.NSEW)

        tk.Button(self.container_inputs, text='Guardar', **style.button_style_save, relief=tk.FLAT, overrelief=tk.RAISED, command=lambda:Add_contact(self.new_name, self.phone, self.email, name_label, phone_label, self.tree)).grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky=tk.NSEW)

        self.container_inputs.grid(row=0, column=0, pady=10, padx=10, sticky=tk.NSEW)
        # ------------------------------------------------------------------------------
        # - Separator -
        ttk.Separator(self.frame_contact, orient='horizontal').grid(row=2, column=0, pady=10, sticky=tk.NSEW)

        # - Contact display -
        self.container_contact = tk.LabelFrame(self.frame_contact, text='Contacto')
        self.container_contact.columnconfigure(0, weight=1)

        name = StringVar()
        phone = StringVar()
        email = StringVar()
        
        self.container_name = tk.LabelFrame(self.container_contact, text='Nombre: ')
        self.container_name.columnconfigure(0, weight=1)
        tk.Label(self.container_name, textvariable=name).grid(row=0, column=0, sticky=tk.NSEW)
        self.container_name.grid(row=0, column=0, padx=10, columnspan=2, sticky=tk.NSEW)

        tk.Button(self.container_name, image=self.logo_img_delete, bd=0, command=lambda:Clear_view(name, phone,email, self.button_delete, self.button_edit)).grid(row=0, column=1, sticky=tk.E)
        
        tk.Label(self.container_contact, text='Número: ').grid(row=1, column=0, padx=20, sticky=tk.W)
        tk.Label(self.container_contact, textvariable=phone).grid(row=1, column=1, padx=20, sticky=tk.E)
        tk.Label(self.container_contact, text='Email: ').grid(row=2, column=0, padx=20, sticky=tk.W)
        tk.Label(self.container_contact, textvariable=email).grid(row=2, column=1, padx=20, sticky=tk.E)

        self.container_buttons = tk.Frame(self.container_contact)
        self.container_buttons.columnconfigure(0, weight=1)
        self.container_buttons.columnconfigure(1, weight=1)
        self.container_buttons.columnconfigure(2, weight=1)

        tk.Button(self.container_buttons, text='Ver', **style.button_style_save, relief=tk.FLAT, overrelief=tk.RAISED, command=lambda:Select_contact_view(name, phone, email, self.button_edit, self.button_delete, self.tree), width=10).grid(row=0, column=0, padx=5, sticky=tk.NSEW)

        self.button_edit = tk.Button(self.container_buttons, text='Editar', **style.button_style_edit, relief=tk.FLAT, overrelief=tk.RAISED, state=tk.DISABLED, command=lambda:Edit_window(self.tree, 'view', name, phone, email), width=10)
        self.button_edit.grid(row=0, column=1, padx=5, sticky=tk.NSEW)

        self.button_delete = tk.Button(self.container_buttons, text='Eliminar', **style.button_style_delete, relief=tk.FLAT, overrelief=tk.RAISED, state=tk.DISABLED, command=lambda:Delete_contact_view(name, phone, email, self.button_edit, self.button_delete, self.tree), width=10)
        self.button_delete.grid(row=0, column=2, padx=5, sticky=tk.NSEW)
        
        self.container_buttons.grid(row=4, column=0, columnspan=2, pady=5, sticky=tk.NSEW)
        self.container_contact.grid(row=3, column=0, sticky=tk.NSEW, padx=10)
        # ----------------------------------------------------------------------


        # - Search -
        self.container_search = tk.Frame(self.frame_contact)
        self.container_search.columnconfigure(0, weight=1)
        
        self.search = tk.Entry(self.container_search)
        self.search.grid(row=0, column=0, padx=5, sticky=tk.NSEW)
        tk.Button(self.container_search, image=self.logo_img_search, bd=0, command=lambda:Search_contact(self.search, name, phone, email, self.button_edit, self.button_delete)).grid(row=0, column=1, padx=5, sticky=tk.NSEW)

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

        self.button_table = tk.Frame(self)
        tk.Button(self.button_table, image=self.logo_img_delete, bd=0, command=lambda:Delete_contact_select(name, phone, email, self.button_edit, self.button_delete, self.tree)).grid(row=0, column=0, pady=5)

        tk.Button(self.button_table, image=self.logo_img_edit, bd=0, command=lambda:Edit_window(self.tree, 'selection', name, phone, email)).grid(row=1, column=0, pady=5)
        self.button_table.grid(row=0, column=3, padx=10, pady=10, sticky=tk.NSEW)
  

    
    def window_settings(self):
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, minsize=300)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(3, weight=1)

