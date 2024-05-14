from datetime import datetime
from app.models.database import Base
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship

class Patient(Base):
    __tablename__ = 'patients'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    date_of_birth = Column(DateTime, nullable=False)
    medical_records = relationship('MedicalRecord', back_populates='patient')

    def __init__(self, name, date_of_birth):
        self.name = name
        self.date_of_birth = date_of_birth

    def __repr__(self):
        return f'<Patient {self.name}>'


class MedicalRecord(Base):
    __tablename__ = 'medical_records'

    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey('patients.id'), nullable=False)
    record_data = Column(Text, nullable=False)
    patient = relationship('Patient', back_populates='medical_records')

    def __init__(self, patient_id, record_data):
        self.patient_id = patient_id
        self.record_data = record_data

    def __repr__(self):
        return f'<MedicalRecord {self.id}>'
