from  components.Contact import Contact_label
from db.Database import session
from db.models import Contact_list

class Update_contact_view(Contact_label):
    def __init__(self, name_label, phone_label, email_label, new_name, new_phone, new_email):
        super().__init__(name_label, phone_label, email_label)
        self._new_name = new_name
        self._new_phone = new_phone
        self._new_email = new_email


    def show_data(self):
        global id_contact
        self.contacts = session.query(Contact_list.contact_id ,Contact_list.contact_name, Contact_list.contact_phone, Contact_list.contact_email).all()

        for contact in self.contacts:
            if contact[1] == self.get_name_label and contact[2] ==self.get_phone_label:
                id_contact = contact[0]
                self._new_name.insert(0, contact[1])
                self._new_phone.insert(0, contact[2])
                self._new_email.insert(0, contact[3])

    def update_contact(self):
        print(id_contact)
                
