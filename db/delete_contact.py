import tkinter.messagebox
import tkinter as tk
from db.Database import session
from db.models import Contact_list
from db.get_all_contacts import Get_all_contacts
from components.Contact import Contact_label

class Delete_contact(Contact_label):
    def __init__(self, name_label, phone_label, email_label, button_edit, tree):
        super().__init__(name_label, phone_label, email_label)
        self._button_edit = button_edit
        self._tree= tree
        self.contact_select_tree = self._tree.item(self._tree.selection())['text'] 
        self.contact_verifier()

    def contact_verifier(self):
        try:
            #Verify that a contact is selected
            self._tree.item(self._tree.selection())['text'][0]

        except IndexError as err: 
            self.delete_contact_label()

        else:
            self.delete_contact_select()

    def delete_contact(self, contact):
        # Database connection
        value = tkinter.messagebox.askyesno(message=f'Desea eliminar el contacto {contact}', title='Elimnar contacto')
        if value:
            session.query(Contact_list).filter(Contact_list.contact_name == contact).delete()
            session.commit()
            Get_all_contacts(self._tree)

    def delete_contact_label(self):
        # Remove the contact found in the labelframe
        if (self.get_name_label != ''):
            self.delete_contact(self.get_name_label)

            self.clear_label()
            self._button_edit['state'] = tk.DISABLED
        else:
            tkinter.messagebox.showinfo(message='Debe seleccionar un contacto.', title='No hay seleccion.')

    def delete_contact_select(self):
        # Deletes the selected contact in the tree
        self.delete_contact(self.contact_select_tree)

        if self.get_name_label == self.contact_select_tree:
            self.clear_label()
            self._button_edit['state'] = tk.DISABLED



            
