import tkinter as tk

class Contact_entry:
    def __init__(self, name_entry, phone_entry, email_entry):
        self._name_entry = name_entry
        self._phone_entry = phone_entry
        self._email_entry = email_entry

        self.get_name_entry = self._name_entry.get().strip()
        self.get_phone_entry = self._phone_entry.get().strip()
        self.get_email_entry = self._email_entry.get().strip()

    def clear_inputs(self):
        self._name_entry.delete(0, tk.END)
        self._phone_entry.delete(0, tk.END)
        self._email_entry.delete(0, tk.END)



class Contact_label:
    def __init__(self, name_label, phone_label, email_label):
        self._name_label = name_label
        self._phone_label = phone_label
        self._email_label = email_label
        
        self.get_name_label = self._name_label.get()
        self.get_phone_label = self._phone_label.get()
        self.get_email_label = self._email_label.get()

    def clear_label(self):
        self._name_label.set('')
        self._phone_label.set('')
        self._email_label.set('')
