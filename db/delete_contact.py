import tkinter.messagebox
import tkinter as tk
from db.Database import session
from db.models import Contact_list
from db.get_all_contacts import Get_all_contacts

class Delete_contact:
    def __init__(self, name_label, phone_label, email_label, button_edit, tree):
        self._name_label = name_label
        self._phone_label = phone_label
        self._email_label = email_label
        self._button_edit = button_edit
        self._tree= tree
        self.contact_select_tree = self._tree.item(self._tree.selection())['text'] 
        self.contact_verifier()

    def contact_verifier(self):
        name_label_get = self._name_label.get()
        try:
            #Verify that a contact is selected
            self._tree.item(self._tree.selection())['text'][0]

        except IndexError as err:
            # Remove the contact found in the labelframe
            if( name_label_get != ''):
                self.delete_contact(name_label_get)

                self.clear_label()
                self._button_edit['state'] = tk.DISABLED
            else:
                tkinter.messagebox.showinfo(message='Debe seleccionar un contacto.', title='No hay seleccion.')

        else:
            # Deletes the selected contact in the tree
            self.delete_contact(self.contact_select_tree)

            if name_label_get == self.contact_select_tree:
                self.clear_label()
                self._button_edit['state'] = tk.DISABLED

    def delete_contact(self, contact):
        # Database connection
        value = tkinter.messagebox.askyesno(message=f'Desea eliminar el contacto {contact}', title='Elimnar contacto')
        if value:
            session.query(Contact_list).filter(Contact_list.contact_name == contact).delete()
            session.commit()
            Get_all_contacts(self._tree)

    def clear_label(self):
        self._name_label.set('')
        self._phone_label.set('')
        self._email_label.set('')


            
