from components.Contact import Contact_label
import tkinter.messagebox
from screen.Edit_windows import Edit_window


class Selection_checker(Contact_label):
    def __init__(self, tree, selection, name_label, phone_label, email_label):
        super().__init__(name_label, phone_label, email_label)
        self._tree = tree
        self.contact_select = self._tree.focus()
        self._selection = selection
        self.selection()

    def selection(self):
        if self._selection == 'selection':
            try:
                self._tree.item(self._tree.selection())['text'][0]

            except IndexError as err:
                print(err)
                tkinter.messagebox.showinfo(message='Debe seleccionar un contacto.', title='No hay seleccion.')

            else:
                Edit_window(self._tree, self._selection, self._name_label, self._phone_label, self._email_label)
        
        elif self._selection == 'view':
            Edit_window(self._tree, self._selection, self._name_label, self._phone_label, self._email_label)
            
