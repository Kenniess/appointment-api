from pydantic import BaseModel

class AppointmentForm(BaseModel):
    idCard: str
    fullName: str
    phone: str
    gender: str
    dob: str
    address: str
    maritalStatus: str
    appointmentDate: str
    appointmentTime: str