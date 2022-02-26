from db.Database import session
from db.models import contact_list

class Get_all_contacts:
    def __init__(self, tree):
        self._tree = tree
        self.get_contacts()


    def get_contacts(self):
        contacts = session.query(contact_list.contact_name, contact_list.contact_phone).all()

        self.records = self._tree.get_children()
        for element in self.records:
            self._tree.delete(element)

        for contact in contacts:
            self._tree.insert('', 'end', text=contact[0], values=contact[1])

        # tambien se puede hacer 
        # for (name, phone, email) in contacts:
        #     self._tree.insert('', 0, text=name, values=phone)