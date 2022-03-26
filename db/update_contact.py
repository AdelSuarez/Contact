from db.Database import session
from screen.Edit_windows import Edit_window

class Update_contact:
    def __init__(self, tree):
        self._tree = tree
        self.update_contact()

    def update_contact(self):
        Edit_window(self._tree)
