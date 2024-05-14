from datetime import datetime
from app.models.database import Base
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship

class Prescription(Base):
    __tablename__ = 'prescriptions'

    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey('patients.id'), nullable=False)
    medication = Column(String(100), nullable=False)
    dosage = Column(Float, nullable=False)
    prescription_date = Column(DateTime, nullable=False, default=datetime.utcnow)
    patient = relationship('Patient', back_populates='prescriptions')

    def __init__(self, patient_id, medication, dosage):
        self.patient_id = patient_id
        self.medication = medication
        self.dosage = dosage

    def __repr__(self):
        return f'<Prescription {self.id}>'
