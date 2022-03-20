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
        self.contact_select = self._tree.focus()
        self.get_contact()

    def get_contact(self):

        try:
            self._tree.item(self._tree.selection())['text'][0]

        except IndexError as err:
            tkinter.messagebox.showinfo(message='Debe seleccionar un contacto.', title='No hay seleccion.')
        
        else:
            self.enable_button()

            self.contacts = session.query(Contact_list.contact_id ,Contact_list.contact_name, Contact_list.contact_phone, Contact_list.contact_email).all()

            print(self.contacts)
            
            self.insert_label()
            

    def enable_button(self):
        if self._button_edit['state'] == tk.DISABLED:
            self._button_edit['state'] = tk.NORMAL

    def insert_label(self):
        self.contact_values = self._tree.item(self.contact_select)
        for values in self.contact_values:
            if values == 'tags':
                self.id = self.contact_values[values]

        print(self.id[0])

        for contact in self.contacts:
            if contact[0] == self.id[0]:
                self._name_label.set(contact[1])
                self._phone_label.set(contact[2])
                self._email_label.set(contact[3])

                print(f'Contact:\nName:{contact[1]}\nPhone:{contact[2]}\nEmail:{contact[3]}\nID: {contact[0]}')
                    
                

        