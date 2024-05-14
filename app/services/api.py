from flask import request, jsonify
from app.services.database_service import DatabaseService
from app.services.contract_service import ContractService

database_service = DatabaseService()
contract_service = ContractService('your_contract_abi.json', 'your_contract_address', 'your_web3_provider')

def get_patient(patient_id):
    patient = database_service.get_patient(patient_id)
    if patient:
        return jsonify(patient.as_dict()), 200
    else:
        return jsonify({"error": "Patient not found"}), 404

def get_prescription(prescription_id):
    prescription = database_service.get_prescription(prescription_id)
    if prescription:
        return jsonify(prescription.as_dict()), 200
    else:
        return jsonify({"error": "Prescription not found"}), 404

def create_patient():
    data = request.get_json()
    patient = database_service.create_patient(data['name'], data['date_of_birth'])
    return jsonify(patient.as_dict()), 201

def create_prescription():
    data = request.get_json()
    prescription = database_service.create_prescription(data['patient_id'], data['drug_name'], data['drug_dosage'], data['drug_frequency'])
    return jsonify(prescription.as_dict()), 201

def update_patient():
    data = request.get_json()
    patient = database_service.update_patient(data['patient_id'], data.get('name'), data.get('date_of_birth'))
    if patient:
        return jsonify(patient.as_dict()), 200
    else:
        return jsonify({"error": "Patient not found"}), 404

def update_prescription():
    data = request.get_json()
    prescription = database_service.update_prescription(data['prescription_id'], data.get('patient_id'), data.get('drug_name'), data.get('drug_dosage'), data.get('drug_frequency'))
    if prescription:
        return jsonify(prescription.as_dict()), 200
    else:
        return jsonify({"error": "Prescription not found"}), 404

def delete_patient(patient_id):
    success = database_service.delete_patient(patient_id)
    if success:
        return jsonify({"message": "Patient deleted"}), 200
    else:
        return jsonify({"error": "Patient not found"}), 404

def delete_prescription(prescription_id):
    success = database_service.delete_prescription(prescription_id)
    if success:
        return jsonify({"message": "Prescription deleted"}), 200
    else:
        return jsonify({"error": "Prescription not found"}), 404

def get_contract_data():
    data = contract_service.get_contract_data()
    return jsonify(data), 200

def call_contract_method(method_name, *args):
    result = contract_service.call_contract_method(method_name, *args)
    return jsonify(result), 200

def send_contract_transaction(method_name, *args, gas=None, gas_price=None):
    result = contract_service.send_transaction(method_name, *args, gas=gas, gas_price=gas_price)
    return jsonify({"tx_hash": result.hex()}), 200

def deploy_contract(contract_source, constructor_args, gas=None, gas_price=None):
    contract = contract_service.deploy_contract(contract_source, constructor_args, gas=gas, gas_price=gas_price)
    return jsonify({"contract_address": contract.address}), 201
