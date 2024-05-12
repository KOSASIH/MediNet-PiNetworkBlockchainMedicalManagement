// api.ts
import axios from 'axios';
import { environment } from '../config/environment';

const api = axios.create({
  baseURL: environment.api.url,
});

export const getMedicalRecords = async () => {
  const response = await api.get('/medical-records');
  return response.data;
};
