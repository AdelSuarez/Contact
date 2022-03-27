from db.Database import session
from db.models import Contact_list
import tkinter as tk
import tkinter.messagebox
from components.Contact import Contact_label

class Search_contact(Contact_label):
    def __init__(self, search_entry, name_label, phone_label, email_label, button_edit, button_delete):
        super().__init__(name_label, phone_label, email_label)
        self._search_entry = search_entry
        self._button_edit = button_edit
        self._button_delete = button_delete
        self.search()

    def search(self):

        value_message = True
        if self.validate_empty_fields():
            contacts = session.query(Contact_list.contact_name, Contact_list.contact_phone, Contact_list.contact_email).all()
            
            for contact in contacts:
                if contact[0] == self._search_entry.get().strip():
                    self._name_label.set(contact[0])
                    self._phone_label.set(contact[1])
                    self._email_label.set(contact[2])
                    value_message = False

                    print(f'Contact:\nName:{contact[0]}\nPhone:{contact[1]}\nEmail:{contact[2]}')
                    
                    self._button_edit['state'] = tk.NORMAL
                    self._button_delete['state'] = tk.NORMAL

            if value_message:
                tkinter.messagebox.showinfo(message='Contacto no existe', title=f'El contacto {self._search_entry.get()} No existe')
                print('Does not exist')

            self._search_entry.delete(0, tk.END)

    def validate_empty_fields(self):
        return len(self._search_entry.get()) != 0