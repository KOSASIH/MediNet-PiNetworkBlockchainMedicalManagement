from flask import Blueprint, request, jsonify
from app.models.medical_supply import MedicalSupply
from app.services.database_service import DatabaseService

medical_supply_routes = Blueprint('medical_supply_routes', __name__)

@medical_supply_routes.route('/medical_supplies', methods=['POST'])
def create_medical_supply():
    data = request.get_json()
    medical_supply = MedicalSupply(name=data['name'], quantity=data['quantity'], expiration_date=data['expiration_date'])
    DatabaseService.add_medical_supply(medical_supply)
    return jsonify({'message': 'Medical supply created successfully'}), 201

@medical_supply_routes.route('/medical_supplies', methods=['GET'])
def get_medical_supplies():
    medical_supplies = DatabaseService.get_medical_supplies()
    return jsonify([medical_supply.to_dict() for medical_supply in medical_supplies]), 200

@medical_supply_routes.route('/medical_supplies/<int:medical_supply_id>', methods=['GET'])
def get_medical_supply(medical_supply_id):
    medical_supply = DatabaseService.get_medical_supply(medical_supply_id)
    if medical_supply:
        return jsonify(medical_supply.to_dict()), 200
    else:
        return jsonify({'message': 'Medical supply not found'}), 404

@medical_supply_routes.route('/medical_supplies/<int:medical_supply_id>', methods=['PUT'])
def update_medical_supply(medical_supply_id):
    data = request.get_json()
    medical_supply = DatabaseService.update_medical_supply(medical_supply_id, data)
    if medical_supply:
        return jsonify({'message': 'Medical supply updated successfully'}), 200
    else:
        return jsonify({'message': 'Medical supply not found'}), 404

@medical_supply_routes.route('/medical_supplies/<int:medical_supply_id>', methods=['DELETE'])
def delete_medical_supply(medical_supply_id):
    medical_supply = DatabaseService.delete_medical_supply(medical_supply_id)
    if medical_supply:
        return jsonify({'message': 'Medical supply deleted successfully'}), 200
    else:
        return jsonify({'message': 'Medical supply not found'}), 404
