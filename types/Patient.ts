import { MedicalRecord } from './MedicalRecord';

export interface Patient {
  id: string;
  name: string;
  email: string;
  medicalRecords: MedicalRecord[];
}
