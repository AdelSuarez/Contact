import tkinter as tk
import tkinter.messagebox
from db.Database import session
from db.models import Contact_list
from components.get_all_contacts import Get_all_contacts
from components.Contact import Contact_label

class Delete_contact_select(Contact_label):
    def __init__(self, name_label, phone_label, email_label, button_edit, button_delete, tree):
        super().__init__(name_label, phone_label, email_label)
        self._tree= tree
        self._button_edit = button_edit
        self._button_delete = button_delete
        self.contact_select = self._tree.focus()
        self.verify_selected_contact()

    def verify_selected_contact(self):
        try:
            #Verify that a contact is selected
            self._tree.item(self._tree.selection())['text'][0]

        except IndexError as err: 
            tkinter.messagebox.showinfo(message='Debe seleccionar un contacto.', title='No hay seleccion.')

        else:
            self.delete_contact()

    def delete_contact(self):
        self.obtaining_contact_information()
    
        # Database connection
        value = tkinter.messagebox.askyesno(message=f'Desea eliminar el contacto {self.name}', title='Elimnar contacto')
        if value:
            session.query(Contact_list).filter(Contact_list.contact_id == self.id[0]).delete()
            session.commit()
            self.check_the_labels()
            Get_all_contacts(self._tree)

    def obtaining_contact_information(self):
        # Get the data of the contact in the database to delete them

        self.contact_values = self._tree.item(self.contact_select)
        print(self.contact_values)

        for values in self.contact_values:
            if values == 'text':
                self.name = self.contact_values[values]

            if values == 'values':
                self.phone = self.contact_values[values]

            if values == 'tags':
                self.id = self.contact_values[values]


        print(self.name)
        print(self.phone[0])
        print(self.id[0])

    def check_the_labels(self):

        # Clean the labels if the contact is in the display section and has benn removed, to avoid errors

        if self.name == self.get_name_label and self.phone[0] == int(self.get_phone_label):
            self.clear_label()

            self._button_edit['state'] = tk.DISABLED
            self._button_delete['state'] = tk.DISABLED

