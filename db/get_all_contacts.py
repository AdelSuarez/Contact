from db.Database import session
from db.models import Contact_list

class Get_all_contacts:
    def __init__(self, tree):
        self._tree = tree
        self.get_contacts()


    def get_contacts(self):
        contacts = session.query(Contact_list.contact_name, Contact_list.contact_phone).all()

        self.clear_tree()

        for contact in contacts:
            self._tree.insert('', 'end', text=contact[0], values=contact[1])

        # tambien se puede hacer 
        # for (name, phone, email) in contacts:
        #     self._tree.insert('', 0, text=name, values=phone)

    def clear_tree(self):        
        self.all_contact = self._tree.get_children()
        for contact in self.all_contact:
            self._tree.delete(contact)