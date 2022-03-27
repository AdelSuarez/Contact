from db.Database import session
from db.models import Contact_list

class Update_contact_select:
    def __init__(self, new_name, new_phone, new_email, tree):
        self._tree = tree
        self.contact_select = self._tree.focus()
        self._new_name = new_name
        self._new_phone = new_phone
        self._new_email = new_email
        self.show_data()

    def show_data(self):
        try:
            self._tree.item(self._tree.selection())['text'][0]

        except IndexError as err:
            print(err)

        else:
            self.contacts = session.query(Contact_list.contact_id, Contact_list.contact_name, Contact_list.contact_phone, Contact_list.contact_email).all()

            self.contact_values = self._tree.item(self.contact_select)
            for values in self.contact_values:
                if values == 'tags':
                    self.id = self.contact_values[values]

            print(self.id[0])

            for contact in self.contacts:
                if contact[0] == self.id[0]:
                    self._new_name.insert(0, contact[1])
                    self._new_phone.insert(0, contact[2])
                    self._new_email.insert(0, contact[3])

                    print(f'Contact:\nName:{contact[1]}\nPhone:{contact[2]}\nEmail:{contact[3]}\nID: {contact[0]}')
