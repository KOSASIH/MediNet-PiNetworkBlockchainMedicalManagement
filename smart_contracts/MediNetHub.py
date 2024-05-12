import pi_blockchain as pi

class MedicalResourceSmartContract:
    def __init__(self):
        self.contract_id = pi.create_contract()

    def add_resource(self, resource_name, resource_quantity):
        pi.execute_contract(self.contract_id, {
            'function': 'add_resource',
            'resource_name': resource_name,
            'resource_quantity': resource_quantity
        })

    def get_resource_quantity(self, resource_name):
        result = pi.execute_contract(self.contract_id, {
            'function': 'get_resource_quantity',
            'resource_name': resource_name
        })
        return result['resource_quantity']

medical_resource_contract = MedicalResourceSmartContract()
medical_resource_contract.add_resource('Medical Masks', 1000)
quantity = medical_resource_contract.get_resource_quantity('Medical Masks')
print(f'Medical Masks quantity: {quantity}')
