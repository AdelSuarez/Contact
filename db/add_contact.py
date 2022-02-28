from db.models import Contact_list
from db.Database import session
import tkinter as tk
import tkinter.messagebox
from db.get_all_contacts import Get_all_contacts

class Add_contact:
    def __init__(self, name_entry, phone_entry, email_entry, name_label, phone_label, tree):
        self._name_entry = name_entry
        self._phone_entry = phone_entry
        self._email_entry = email_entry
        self.name_label = name_label
        self.phone_label = phone_label
        self._tree = tree
        self.add()

    def add(self):
        name_entry_get = self._name_entry.get()
        phone_entry_get = self._phone_entry.get()

        if self.validate_empty_fields(name_entry_get):
            self.name_label['fg'] = '#000'

            if self.validate_empty_fields(phone_entry_get) and self.validate_empty_int(phone_entry_get):
                self.phone_label['fg'] = '#000'

                contact = Contact_list(name_entry_get, phone_entry_get, self._email_entry.get())
                session.add(contact)
                print(repr(contact))
                session.commit()

                self.clear_inputs()

                Get_all_contacts(self._tree)

                tkinter.messagebox.showinfo(message='Contacto creado', title='Contacto creado con exito')

            else:
                self.phone_label['fg'] = 'red' 
        else:
            self.name_label['fg'] = 'red'
            

    def validate_empty_fields(self, entry):
        return len(entry) != 0

    def clear_inputs(self):
        self._name_entry.delete(0, tk.END)
        self._phone_entry.delete(0, tk.END)
        self._email_entry.delete(0, tk.END)

    def validate_empty_int(self, phone):
        # Verify that the phone entered is numbers
        try:
            if int(phone):
                value = True
        except:
            value = False

        return value



