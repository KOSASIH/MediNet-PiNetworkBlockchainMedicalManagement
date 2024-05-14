# medi_net/blockchain/interoperability/blockchain_interoperability.py

import requests
import json

class BlockchainInteroperability:
    def __init__(self, medi_chain_url: str, other_chain_url: str):
        self.medi_chain_url = medi_chain_url
        self.other_chain_url = other_chain_url

    def connect_to_medi_chain(self):
        # Connect to the MediChain blockchain network
        self.medi_chain = requests.get(self.medi_chain_url).json()

    def connect_to_other_chain(self):
        # Connect to the other healthcare blockchain network
        self.other_chain = requests.get(self.other_chain_url).json()

    def transfer_data(self, data: dict, from_chain: str, to_chain: str):
        # Transfer data from one blockchain network to another
        if from_chain == 'medi_chain':
            # Send data from MediChain to the other chain
            self.medi_chain['data'].append(data)
            response = requests.post(self.other_chain_url, json=self.medi_chain)
            if response.status_code == 200:
                print(f"Data transferred from MediChain to {to_chain} successfully!")
        elif from_chain == 'other_chain':
            # Send data from the other chain to MediChain
            self.other_chain['data'].append(data)
            response = requests.post(self.medi_chain_url, json=self.other_chain)
            if response.status_code == 200:
                print(f"Data transferred from {to_chain} to MediChain successfully!")
        else:
            raise ValueError("Invalid chain specified")

    def verify_data(self, data: dict, chain: str):
# Verify the data on a blockchain network
        if chain == 'medi_chain':
            # Verify the data on MediChain
            response = requests.get(f"{self.medi_chain_url}/{data['id']}")
            if response.status_code == 200:
                print(f"Data verified on MediChain!")
        elif chain == 'other_chain':
            # Verify the data on the other chain
            response = requests.get(f"{self.other_chain_url}/{data['id']}")
            if response.status_code == 200:
                print(f"Data verified on {to_chain}!")
        else:
            raise ValueError("Invalid chain specified")
