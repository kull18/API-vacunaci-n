from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from shared.mysql import Base



class User(Base):
    __tablename__ = "User"
    
    idUser = Column(Integer, primary_key=True, index=True)
    username = Column(String(45), unique=True, index=True)
    password = Column(String(45))
    role = Column(String(45))
    groupIdGroup = Column(Integer, ForeignKey("Group.idGroup"))  # asumiendo tabla Group con idGroup
    name = Column(String(45))
    lastname = Column(String(45))