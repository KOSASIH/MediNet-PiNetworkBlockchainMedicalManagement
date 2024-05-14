# medi_net/identity/decentralized_identity.py

import requests
import json

class DecentralizedIdentity:
    def __init__(self, identity_url: str):
        self.identity_url = identity_url

    def create_identity(self, patient_data: dict):
        # Create a new decentralized identity for a patient
        response = requests.post(self.identity_url, json=patient_data)
        if response.status_code == 201:
            print("Identity created successfully!")
            return response.json()
        else:
            print("Failed to create identity")
            return None

    def get_identity(self, patient_id: str):
        # Retrieve a patient's decentralized identity
        response = requests.get(f"{self.identity_url}/{patient_id}")
        if response.status_code == 200:
            print("Identity retrieved successfully!")
            return response.json()
        else:
            print("Failed to retrieve identity")
            return None

    def update_identity(self, patient_id: str, updated_data: dict):
        # Update a patient's decentralized identity
        response = requests.put(f"{self.identity_url}/{patient_id}", json=updated_data)
        if response.status_code == 200:
            print("Identity updated successfully!")
            return response.json()
        else:
            print("Failed to update identity")
            return None

    def delete_identity(self, patient_id: str):
        # Delete a patient's decentralized identity
        response = requests.delete(f"{self.identity_url}/{patient_id}")
        if response.status_code == 204:
            print("Identity deleted successfully!")
            return True
        else:
            print("Failed to delete identity")
            return False

    def add_record(self, patient_id: str, record_data: dict):
        # Add a medical record to a patient's decentralized identity
        identity = self.get_identity(patient_id)
        if identity:
            identity['records'].append(record_data)
            response = requests.put(f"{self.identity_url}/{patient_id}", json=identity)
            if response.status_code == 200:
                print("Record added successfully!")
                return response.json()
            else:
                print("Failed to add record")
                return None
        else:
            print("Failed to retrieve identity")
            return None

    def get_record(self, patient_id: str, record_id: str):
        # Retrieve a medical record from a patient's decentralized identity
        identity = self.get_identity(patient_id)
        if identity:
            for record in identity['records']:
                if record['id'] == record_id:
                    print("Record retrieved successfully!")
                    return record
            print("Record not found")
            return None
        else:
            print("Failed to retrieve identity")
            return None

    def update_record(self, patient_id: str, record_id: str, updated_data: dict):
        # Update a medical record in a patient's decentralized identity
        identity = self.get_identity(patient_id)
        if identity:
            for i, record in enumerate(identity['records']):
                if record['id'] == record_id:
                    identity['records'][i].update(updated_data)
                    response = requests.put(f"{self.identity_url}/{patient_id}", json=identity)
                    if response.status_code == 200:
                        print("Record updated successfully!")
                        return response.json()
                    else:
                        print("Failed to update record")
                        return None
            print("Record not found")
            return None
        else:
            print("Failed to retrieve identity")
            return None

    def delete_record(self, patient_id: str, record_id: str):
        # Delete a medical record from a patient's decentralized identity
        identity = self.get_identity(patient_id)
        if identity:
            for i, record in enumerate(identity['records']):
                if record['id'] == record_id:
                    identity['records'].pop(i)
                    response = requests.put(f"{self.identity_url}/{patient_id}", json=identity)
                    if response.status_code == 200:
                        print("Record deleted successfully!")
                        return response.json()
                    else:
                        print("Failed to delete record")
                        return None
            print("Record not found")
            return None
        else:
            print("Failed to retrieve identity")
            return None
