from components.Contact import Contact_label
from db.Database import session
from db.models import Contact_list
from db.get_all_contacts import Get_all_contacts
import tkinter.messagebox
import tkinter as tk


class Delete_contact_view(Contact_label):
    def __init__(self, name_label, phone_label, email_label, button_edit, button_delete, tree):
        super().__init__(name_label, phone_label, email_label)
        self._button_edit = button_edit
        self._button_delete = button_delete
        self._tree = tree
        self.delete_contact()

    def delete_contact(self):
        if self.get_name_label != '':
            contacts = session.query(Contact_list.contact_id ,Contact_list.contact_name, Contact_list.contact_phone, Contact_list.contact_email).all()

            print(contacts)
            for contact in contacts:
                if contact[1] == self.get_name_label and contact[2] ==self.get_phone_label:
                    value = tkinter.messagebox.askyesno(message=f'Desea eliminar el contacto {contact[1]}', title='Elimnar contacto')
                    if value:
                        session.query(Contact_list).filter(Contact_list.contact_id == contact[0]).delete()
                        session.commit()
                        Get_all_contacts(self._tree)
                        
                        self.clear_label()

                        self._button_edit['state'] = tk.DISABLED
                        self._button_delete['state'] = tk.DISABLED
                    break
