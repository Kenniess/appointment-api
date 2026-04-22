from sqlalchemy.orm import Session
from app import models, schemas

def create_appointment(db: Session, appointment: schemas.AppointmentForm):
    db_appointment = models.Appointment(
        idCard=appointment.idCard,
        fullName=appointment.fullName,
        phone=appointment.phone,
        gender=appointment.gender,
        dob=appointment.dob,
        address=appointment.address,
        maritalStatus=appointment.maritalStatus,
        appointmentDate=appointment.appointmentDate,
        appointmentTime=appointment.appointmentTime
    )
    db.add(db_appointment)
    db.commit()
    db.refresh(db_appointment)
    return db_appointment

def get_appointments(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Appointment).offset(skip).limit(limit).all()
