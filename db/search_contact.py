from db.Database import session
from db.models import Contact_list

class Search_contact:
    def __init__(self, search_entry, name_label, phone_label, email_label):
        self._name_label = name_label
        self._phone_label = phone_label
        self._email_label = email_label
        self._search_entry = search_entry
        self.search()

    def search(self):
        if self.validate_empty_fields():
            contacts = session.query(Contact_list.contact_name, Contact_list.contact_phone, Contact_list.contact_email).all()
                
            for contact in contacts:
                if contact[0] == self._search_entry.get():
                    self._name_label.set(contact[0])
                    self._phone_label.set(contact[1])
                    self._email_label.set(contact[2])

                    print(f'Contact:\nName:{contact[0]}\nPhone:{contact[1]}\nEmail:{contact[2]}')



    def validate_empty_fields(self):
        return len(self._search_entry.get()) != 0