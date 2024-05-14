# medi_net/security/secure_multi_party_computation.py

import random
import os
import json
from cryptography.fernet import Fernet

class SecureMultiPartyComputation:
    def __init__(self, participants: list):
        self.participants = participants
        self.shares = {}

    def generate_key(self):
        # Generate a random symmetric key for encryption
        key = Fernet.generate_key()
        return key

    def encrypt_data(self, data: dict, key: bytes):
        # Encrypt data using a symmetric key
        f = Fernet(key)
        encrypted_data = f.encrypt(json.dumps(data).encode())
        return encrypted_data

    def split_data(self, data: dict, num_parties: int):
        # Split data into shares for each party
        shares = {}
        for i in range(num_parties):
            share = {}
            for key, value in data.items():
                share[key] = random.randint(0, 100)
            shares[i] = share
        return shares

    def reconstruct_data(self, shares: dict):
        # Reconstruct data from shares
        num_parties = len(shares)
        data = {}
        for key in shares[0].keys():
            values = [shares[i][key] for i in range(num_parties)]
            sum_values = sum(values)
            data[key] = sum_values / num_parties
        return data

    def generate_shares(self, data: dict):
        # Generate shares for each party
        key = self.generate_key()
        encrypted_data = self.encrypt_data(data, key)
        shares = self.split_data(data, len(self.participants))
        for i, participant in enumerate(self.participants):
            participant_shares = {i: shares[i] for i in shares}
            self.shares[participant] = {
                'key': key.decode(),
                'encrypted_data': encrypted_data,
                'shares': participant_shares
            }

    def perform_secure_computation(self, function: callable, inputs: dict):
        # Perform secure computation on encrypted data
        outputs = {}
        for participant, share in self.shares.items():
            key = share['key'].encode()
            encrypted_data = share['encrypted_data']
            participant_inputs = {k: self.decrypt_data(v, key) for k, v in inputs.items() if k in share['shares']}
            participant_output = function(participant_inputs)
            outputs[participant] = self.encrypt_data(participant_output, key)
        return outputs

    def decrypt_data(self, encrypted_data: bytes, key: bytes):
        # Decrypt data using a symmetric key
        f = Fernet(key)
        decrypted_data = f.decrypt(encrypted_data)
        return json.loads(decrypted_data.decode())

    def perform_secure_aggregation(self, inputs: dict):
        # Perform secure aggregation on encrypted data
        outputs = self.perform_secure_computation(sum, inputs)
        aggregated_output = self.reconstruct_data(outputs)
        return aggregated_output
