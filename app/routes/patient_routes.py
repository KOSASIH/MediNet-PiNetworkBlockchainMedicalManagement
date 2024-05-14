from flask import Blueprint, request, jsonify
from app.models.patient import Patient, MedicalRecord
from app.services.database_service import DatabaseService

patient_routes = Blueprint('patient_routes', __name__)

@patient_routes.route('/patients', methods=['POST'])
def create_patient():
    data = request.get_json()
    patient = Patient(name=data['name'], date_of_birth=data['date_of_birth'])
    DatabaseService.add_patient(patient)
    return jsonify({'message': 'Patient created successfully'}), 201

@patient_routes.route('/patients', methods=['GET'])
def get_patients():
    patients = DatabaseService.get_patients()
    return jsonify([patient.to_dict() for patient in patients]), 200

@patient_routes.route('/patients/<int:patient_id>', methods=['GET'])
def get_patient(patient_id):
    patient = DatabaseService.get_patient(patient_id)
    if patient:
        return jsonify(patient.to_dict()), 200
    else:
        return jsonify({'message': 'Patient not found'}), 404

@patient_routes.route('/patients/<int:patient_id>', methods=['PUT'])
def update_patient(patient_id):
    data = request.get_json()
    patient = DatabaseService.update_patient(patient_id, data)
    if patient:
        return jsonify({'message': 'Patient updated successfully'}), 200
    else:
        return jsonify({'message': 'Patient not found'}), 404

@patient_routes.route('/patients/<int:patient_id>', methods=['DELETE'])
def delete_patient(patient_id):
    patient = DatabaseService.delete_patient(patient_id)
    if patient:
        return jsonify({'message': 'Patient deleted successfully'}), 200
    else:
        return jsonify({'message': 'Patient not found'}), 404

@patient_routes.route('/patients/<int:patient_id>/medical_records', methods=['POST'])
def create_medical_record(patient_id):
    data = request.get_json()
    medical_record = MedicalRecord(patient_id=patient_id, record_data=data['record_data'])
    DatabaseService.add_medical_record(medical_record)
    return jsonify({'message': 'Medical record created successfully'}), 201

@patient_routes.route('/patients/<int:patient_id>/medical_records', methods=['GET'])
def get_medical_records(patient_id):
    medical_records = DatabaseService.get_medical_records(patient_id)
    return jsonify([medical_record.to_dict() for medical_record in medical_records]), 200
