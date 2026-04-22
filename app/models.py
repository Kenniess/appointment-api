from sqlalchemy import Column, Integer, String
from app.database import Base
class Appointment(Base):
    __tablename__ = "appointments"
    id = Column(Integer, primary_key=True, index=True)
    idCard = Column(String, index=True)
    fullName = Column(String)
    phone = Column(String)
    gender = Column(String)
    dob = Column(String)
    address = Column(String)
    maritalStatus = Column(String)
    appointmentDate = Column(String)
    appointmentTime = Column(String)