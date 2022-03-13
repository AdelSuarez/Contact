from db.models import Contact_list
from db.Database import session
import tkinter as tk
import tkinter.messagebox
from db.get_all_contacts import Get_all_contacts
from components.Contact import Contact_entry
from style import style

class Add_contact(Contact_entry):
    def __init__(self, name_entry, phone_entry, email_entry, name_label, phone_label, tree):
        super().__init__(name_entry, phone_entry, email_entry)
        self.name_label = name_label
        self.phone_label = phone_label
        self._tree = tree
        self.add()

    def add(self):
        if self.validate_empty_fields(self.get_name_entry):
            self.name_label['fg'] = style.BLACK

            if self.validate_empty_fields(self.get_phone_entry) and self.validate_empty_int(self.get_phone_entry):
                self.phone_label['fg'] = style.BLACK

                contact = Contact_list(self.get_name_entry, self.get_phone_entry, self.get_email_entry)
                session.add(contact)
                print(repr(contact))
                session.commit()

                self.clear_inputs()

                Get_all_contacts(self._tree)

                tkinter.messagebox.showinfo(message='Contacto creado', title='Contacto creado con exito')

            else:
                self.phone_label['fg'] = style.RED 
        else:
            self.name_label['fg'] = style.RED
            
    def validate_empty_fields(self, entry):
        return len(entry) != 0

    def validate_empty_int(self, phone):
        # Verify that the phone entered is numbers
        try:
            if int(phone):
                value = True
        except:
            value = False

        return value



