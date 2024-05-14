from app.models.patient import Patient
from app.models.prescription import Prescription
from app.models.medical_supply import MedicalSupply
from app.models.database import Base, engine

class DatabaseService:
    def __init__(self):
        self.Base = Base
        self.engine = engine

    def create_patient(self, name, date_of_birth):
        patient = Patient(name=name, date_of_birth=date_of_birth)
        self.Base.session.add(patient)
        self.Base.session.commit()
        return patient

    def get_patient(self, patient_id):
        return self.Base.session.query(Patient).filter(Patient.id == patient_id).first()

    def update_patient(self, patient_id, name=None, date_of_birth=None):
        patient = self.Base.session.query(Patient).filter(Patient.id == patient_id).first()
        if patient:
            if name:
                patient.name = name
            if date_of_birth:
                patient.date_of_birth = date_of_birth
            self.Base.session.commit()
            return patient
        else:
            return None

    def delete_patient(self, patient_id):
        patient = self.Base.session.query(Patient).filter(Patient.id == patient_id).first()
        if patient:
            self.Base.session.delete(patient)
            self.Base.session.commit()
            return True
        else:
            return False

    def create_prescription(self, patient_id, drug_name, drug_dosage, drug_frequency):
        prescription = Prescription(patient_id=patient_id, drug_name=drug_name, drug_dosage=drug_dosage, drug_frequency=drug_frequency)
        self.Base.session.add(prescription)
        self.Base.session.commit()
        return prescription

    def get_prescription(self, prescription_id):
        return self.Base.session.query(Prescription).filter(Prescription.id == prescription_id).first()

    def update_prescription(self, prescription_id, patient_id=None, drug_name=None, drug_dosage=None, drug_frequency=None):
        prescription = self.Base.session.query(Prescription).filter(Prescription.id == prescription_id).first()
        if prescription:
            if patient_id:
                prescription.patient_id = patient_id
            if drug_name:
                prescription.drug_name = drug_name
            if drug_dosage:
                prescription.drug_dosage = drug_dosage
            if drug_frequency:
                prescription.drug_frequency = drug_frequency
            self.Base.session.commit()
            return prescription
        else:
            return None

    def delete_prescription(self, prescription_id):
        prescription = self.Base.session.query(Prescription).filter(Prescription.id == prescription_id).first()
        if prescription:
            self.Base.session.delete(prescription)
            self.Base.session.commit()
            return True
        else:
            return False

    def create_medical_supply(self, name, quantity):
        medical_supply = MedicalSupply(name=name, quantity=quantity)
        self.Base.session.add(medical_supply)
        self.Base.session.commit()
        return medical_supply

    def get_medical_supply(self, medical_supply_id):
        return self.Base.session.query(MedicalSupply).filter(MedicalSupply.id == medical_supply_id).first()

    def update_medical_supply(self, medical_supply_id, name=None, quantity=None):
        medical_supply = self.Base.session.query(MedicalSupply).filter(MedicalSupply.id == medical_supply_id).first()
        if medical_supply:
            if name:
                medical_supply.name = name
            if quantity:
                medical_supply.quantity = quantity
            self.Base.session.commit()
            return medical_supply
        else:
            return None

    def delete_medical_supply(self, medical_supply_id):
        medical_supply = self.Base.session.query(MedicalSupply).filter(MedicalSupply.id == medical_supply_id).first()
        if medical_supply:
            self.Base.session.delete(medical_supply)
            self.Base.session.commit()
            return True
        else:
            return False
