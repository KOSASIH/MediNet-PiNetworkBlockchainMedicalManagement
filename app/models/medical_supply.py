from datetime import datetime
from app.models.database import Base
from sqlalchemy import Column, Integer, String, Float, DateTime

class MedicalSupply(Base):
    __tablename__ = 'medical_supplies'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    quantity = Column(Float, nullable=False)
    expiration_date = Column(DateTime, nullable=False)

    def __init__(self, name, quantity, expiration_date):
        self.name = name
        self.quantity = quantity
        self.expiration_date = expiration_date

    def __repr__(self):
        return f'<MedicalSupply {self.id}>'
