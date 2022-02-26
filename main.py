import tkinter as tk
from Manager import Manager
from db.Database import Base, engine


if __name__ == '__main__':
    print('starting application...')
    Base.metadata.create_all(engine)
    root = tk.Tk()
    app = Manager(root)
    app.mainloop()

    print('Ending application')