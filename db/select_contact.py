import tkinter.messagebox
from db.Database import session
from db.models import contact_list

class Select_contact:
    def __init__(self, name, phone, email, tree):
        self._name = name
        self._phone = phone
        self._email = email
        self._tree = tree
        self.get_contact()

    def get_contact(self):
        try:
            self._tree.item(self._tree.selection())['text'][0]
        except IndexError:
            tkinter.messagebox.showinfo(message='Debe seleccionar un contacto.', title='No hay seleccion.')
        else:
            name_db = self._tree.item(self._tree.selection())['text']
            print(name_db)

            contacts = session.query(contact_list.contact_name, contact_list.contact_phone, contact_list.contact_email).all()

            for i in contacts:
                if i[0] == name_db:
                    self._name.set(i[0])
                    self._phone.set(i[1])
                    self._email.set(i[2])
                    print(f'contacto\n{i[0]}\n{i[1]}')
                

        