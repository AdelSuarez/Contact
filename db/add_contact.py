from db.models import contact_list
from db.Database import session
import tkinter as tk
import tkinter.messagebox
from db.get_all_contacts import Get_all_contacts

class Add_contact:
    def __init__(self, name, phone, email, name_label, phone_label, tree):
        self._name = name
        self._phone = phone
        self._email = email
        self.name_label = name_label
        self.phone_label = phone_label
        self._tree = tree
        self.add()

    def add(self):
        if self.validate_empty_fields(self._name.get()):
            self.name_label['fg'] = '#000'

            if self.validate_empty_fields(self._phone.get()) and self.validate_empty_int():
                self.phone_label['fg'] = '#000'

                contact = contact_list(self._name.get(), self._phone.get(), self._email.get())
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
            

    def validate_empty_fields(self, input):
        return len(input) != 0

    def clear_inputs(self):
        self._name.delete(0, tk.END)
        self._phone.delete(0, tk.END)
        self._email.delete(0, tk.END)

    def validate_empty_int(self):
        try:
            if int(self._phone.get()):
                value = True
        except:
            value = False

        return value



