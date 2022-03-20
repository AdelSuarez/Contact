import tkinter.messagebox
from db.Database import session
from db.models import Contact_list
from db.select_contact import Select_contact
from screen.Edit_windows import Edit_window

class Update_contact:
    def __init__(self, tree):
        self._tree = tree
        self.update_contact()

    def update_contact(self):
        Edit_window(self._tree)

        # try:
        #     self._tree.item(self._tree.selection())['text'][0]

        # except IndexError as err:
        #     print(err)

        # else:
        #     name_db = self._tree.item(self._tree.selection())['text']
        #     print(name_db)

        #     contacts = session.query(contact_list.contact_name, contact_list.contact_phone, contact_list.contact_email).all()

        #     for i in contacts:
        #         if i[0] == name_db:
        #             self._name_entry.insert(0, i[0])
        #             self._phone_entry.insert(0, i[1])
        #             self._email_entry.insert(0, i[2])

        #             print(f'Contact:\nName:{i[0]}\nPhone:{i[1]}\nEmail:{i[2]}')
