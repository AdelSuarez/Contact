from db.Database import session
from db.models import Contact_list
from components.get_all_contacts import Get_all_contacts
from style import style
from components.Contact import Contact_label


class Update_contact(Contact_label):
    def __init__(self, select,  new_name, new_phone, new_email, tree, win_edit, name_label_view, phone_label_view, email_label_view):
        super().__init__(name_label_view, phone_label_view, email_label_view)
        self._select = select
        self._tree = tree
        self._win_edit = win_edit
        self.contact_select = self._tree.focus()
        self._new_name = new_name
        self._new_phone = new_phone
        self._new_email = new_email

        self.contacts = session.query(Contact_list.contact_id, Contact_list.contact_name, Contact_list.contact_phone, Contact_list.contact_email).all()
        self.contact_values = self._tree.item(self.contact_select)

    def select_show_data(self):
        if self._select =='selection':
            self.data_select()
        
        elif self._select == 'view':
            self.data_view()

    def data_select(self):

        global id_contact

        for values in self.contact_values:
            if values == 'tags':
                self.id = self.contact_values[values]

        print(self.id[0])
        id_contact = self.id[0]

        for contact in self.contacts:
            if contact[0] == self.id[0]:
                self._new_name.insert(0, contact[1])
                self._new_phone.insert(0, contact[2])
                self._new_email.insert(0, contact[3])

                print(f'Contact:\nName:{contact[1]}\nPhone:{contact[2]}\nEmail:{contact[3]}\nID: {contact[0]}')

    def data_view(self):
        global id_contact

        for contact in self.contacts:
            if contact[1] == self.get_name_label and contact[2] ==self.get_phone_label:
                id_contact = contact[0]
                self._new_name.insert(0, contact[1])
                self._new_phone.insert(0, contact[2])
                self._new_email.insert(0, contact[3])

    def update_contact(self):
        print(id_contact)

        if self.validate_empty_fields(self._new_name.get()):
            self._name_label['fg'] = style.BLACK

            if self.validate_empty_fields(self._new_phone.get()):
                self._phone_label['fg'] = style.BLACK

                self.contact = session.query(Contact_list).filter(Contact_list.contact_id == id_contact).first()
                print(self.contact)
                self.contact.contact_name = self._new_name.get().strip()
                self.contact.contact_phone = self._new_phone.get().strip()
                self.contact.contact_email = self._new_email.get().strip()

                session.add(self.contact)
                session.commit()
                Get_all_contacts(self._tree)
                self._win_edit.destroy()
            else:
                self._phone_label['fg'] = style.RED
        else:
            self._name_label['fg'] = style.RED

    def validate_empty_fields(self, entry):
        return len(entry) != 0