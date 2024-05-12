import axios from 'axios';
import { API_URL, AUTH_TOKEN, PATIENT_ID } from './constants';

export const getMedicalRecords = async () => {
  const response = await axios.get(`${API_URL}/medical-records/${PATIENT_ID}`, {
    headers: {
      Authorization: `Bearer ${AUTH_TOKEN}`,
    },
  });

  return response.data;
};

export const createMedicalRecord = async (medicalRecord: any) => {
  const response = await axios.post(`${API_URL}/medical-records`, medicalRecord, {
    headers: {
      Authorization: `Bearer ${AUTH_TOKEN}`,
    },
  });

  return response.data;
};

export const updateMedicalRecord = async (medicalRecordId: string, updatedMedicalRecord: any) => {
  const response = await axios.put(`${API_URL}/medical-records/${medicalRecordId}`, updatedMedicalRecord, {
    headers: {
      Authorization: `Bearer ${AUTH_TOKEN}`,
    },
  });

  return response.data;
};

export const deleteMedicalRecord = async (medicalRecordId: string) => {
  const response = await axios.delete(`${API_URL}/medical-records/${medicalRecordId}`, {
    headers: {
      Authorization: `Bearer ${AUTH_TOKEN}`,
    },
  });

  return response.data;
};
