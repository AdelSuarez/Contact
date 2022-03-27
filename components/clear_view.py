from components.Contact import Contact_label
import tkinter as tk

class Clear_view(Contact_label):
    def __init__(self, name_label, phone_label, email_label, button_edit, button_delete):
        super().__init__(name_label, phone_label, email_label)
        self._button_edit = button_edit
        self._button_delete = button_delete
        self.clear_label()
        self._button_delete['state'] = tk.DISABLED
        self._button_edit['state'] = tk.DISABLED