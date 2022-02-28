from db.Database import Base
from sqlalchemy import create_engine, Column, Integer, String

class Contact_list(Base):
    __tablename__ = 'contacts'
    contact_id = Column(Integer, primary_key=True)
    contact_name = Column(String(50))
    contact_phone = Column(String(50))
    contact_email = Column(String(100))
    

    def __init__(self, name, phone, email):
        self.contact_name = name
        self.contact_phone = phone
        self.contact_email = email

    def __repr__(self) -> str:
        return f'Contact:\nName: {self.contact_name}.\nPhone: {self.contact_phone}.\nEmail: {self.contact_email}\n'

    def __str__(self) -> str:
        return self.contact_name

# if __name__ == '__main__':
#     Base.metadata.create_all(engine)