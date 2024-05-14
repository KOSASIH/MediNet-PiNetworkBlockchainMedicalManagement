# app.py
from flask import Flask, request, jsonify
from web3 import Web3

app = Flask(__name__)

# Initialize Web3 provider
w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/YOUR_PROJECT_ID'))

# Define a function to interact with the smart contract
def interact_with_contract(contract_address, function_name, *args):
    try:
        contract = w3.eth.contract(address=contract_address, abi=YOUR_CONTRACT_ABI)
        result = getattr(contract.functions, function_name)(*args).call()
        return result
    except Exception as e:
        app.logger.error(f"Error interacting with contract: {e}")
        return None

# Define a route to retrieve a patient's medical records
@app.route('/patient/records', methods=['GET'])
def get_patient_records():
    patient_id = request.args.get('patient_id')
    if not patient_id:
        return jsonify({'error': 'Patient ID is required'}), 400

    contract_address = '0x...Your Contract Address...'
    records = interact_with_contract(contract_address, 'getPatientRecords', patient_id)
    if records:
        return jsonify({'records': records})
    else:
        return jsonify({'error': 'Failed to retrieve records'}), 500

if __name__ == '__main__':
    app.run(debug=True)
