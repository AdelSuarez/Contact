import tkinter as tk
import tkinter.messagebox
from db.Database import session
from db.models import Contact_list
from components.Contact import Contact_label


class Select_contact(Contact_label):
    def __init__(self, name_label, phone_label, email_label, button_edit, tree):
        super().__init__(name_label, phone_label, email_label)
        self._button_edit = button_edit
        self._tree = tree
        self.get_contact()

    def get_contact(self):

        try:
            self._tree.item(self._tree.selection())['text'][0]

        except IndexError as err:
            tkinter.messagebox.showinfo(message='Debe seleccionar un contacto.', title='No hay seleccion.')
        
        else:
            self.enable_button()

            self.name_select_tree = self._tree.item(self._tree.selection())['text']
            print(self.name_select_tree)


            self.contacts = session.query(Contact_list.contact_name, Contact_list.contact_phone, Contact_list.contact_email).all()
            
            self.insert_label()
            

    def enable_button(self):
        if self._button_edit['state'] == tk.DISABLED:
            self._button_edit['state'] = tk.NORMAL

    def insert_label(self):
        for contact in self.contacts:
                if contact[0] == self.name_select_tree:
                    self._name_label.set(contact[0])
                    self._phone_label.set(contact[1])
                    self._email_label.set(contact[2])

                    print(f'Contact:\nName:{contact[0]}\nPhone:{contact[1]}\nEmail:{contact[2]}')
                    
                

        