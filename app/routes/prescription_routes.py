from flask import Blueprint, request, jsonify
from app.models.prescription import Prescription
from app.services.database_service import DatabaseService

prescription_routes = Blueprint('prescription_routes', __name__)

@prescription_routes.route('/prescriptions', methods=['POST'])
def create_prescription():
    data = request.get_json()
    prescription = Prescription(patient_id=data['patient_id'], medication=data['medication'], dosage=data['dosage'])
    DatabaseService.add_prescription(prescription)
    return jsonify({'message': 'Prescription created successfully'}), 201

@prescription_routes.route('/prescriptions', methods=['GET'])
def get_prescriptions():
    prescriptions = DatabaseService.get_prescriptions()
    return jsonify([prescription.to_dict() for prescription in prescriptions]), 200

@prescription_routes.route('/prescriptions/<int:prescription_id>', methods=['GET'])
def get_prescription(prescription_id):
    prescription = DatabaseService.get_prescription(prescription_id)
    if prescription:
        return jsonify(prescription.to_dict()), 200
    else:
        return jsonify({'message': 'Prescription not found'}), 404

@prescription_routes.route('/prescriptions/<int:prescription_id>', methods=['PUT'])
def update_prescription(prescription_id):
    data = request.get_json()
    prescription = DatabaseService.update_prescription(prescription_id, data)
    if prescription:
        return jsonify({'message': 'Prescription updated successfully'}), 200
    else:
        return jsonify({'message': 'Prescription not found'}), 404

@prescription_routes.route('/prescriptions/<int:prescription_id>', methods=['DELETE'])
def delete_prescription(prescription_id):
    prescription = DatabaseService.delete_prescription(prescription_id)
    if prescription:
        return jsonify({'message': 'Prescription deleted successfully'}), 200
    else:
        return jsonify({'message': 'Prescription not found'}), 404
