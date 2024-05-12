import { Patient } from '../models/Patient';
import { MedicalRecord } from '../models/MedicalRecord';
import { BLOCKCHAIN_PORT, API_PORT, MEDICAL_RECORDS_API_ROUTE, PATIENTS_API_ROUTE } from './constants';

export const getMedicalRecordsApiUrl = (): string => {
  return `http://localhost:${API_PORT}${MEDICAL_RECORDS_API_ROUTE}`;
};

export const getPatientsApiUrl = (): string => {
  return `http://localhost:${API_PORT}${PATIENTS_API_ROUTE}`;
};

export const createPatient = (patient: Patient): Promise<Patient> => {
  return fetch(getPatientsApiUrl(), {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(patient)
  }).then(response => response.json());
};

export const getPatient = (id: string): Promise<Patient> => {
  return fetch(`${getPatientsApiUrl()}/${id}`).then(response => response.json());
};

export const updatePatient = (patient: Patient): Promise<Patient> => {
  return fetch(`${getPatientsApiUrl()}/${patient.id}`, {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(patient)
  }).then(response => response.json());
};

export const deletePatient = (id: string): Promise<void> => {
  return fetch(`${getPatientsApiUrl()}/${id}`, {
    method: 'DELETE'
  }).then(() => {});
};

export const createMedicalRecord = (medicalRecord: MedicalRecord): Promise<MedicalRecord> => {
  return fetch(getMedicalRecordsApiUrl(), {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(medicalRecord)
  }).then(response => response.json());
};

export const getMedicalRecord = (id: string): Promise<MedicalRecord> => {
  return fetch(`${getMedicalRecordsApiUrl()}/${id}`).then(response => response.json());
};

export const updateMedicalRecord = (medicalRecord: MedicalRecord): Promise<MedicalRecord> => {
  return fetch(`${getMedicalRecordsApiUrl()}/${medicalRecord.id}`, {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(medicalRecord)
  }).then(response => response.json());
};

export const deleteMedicalRecord = (id: string): Promise<void> => {
  return fetch(`${getMedicalRecordsApiUrl()}/${id}`, {
    method: 'DELETE'
  }).then(() => {});
};
