import { MedicalRecord } from './MedicalRecord';

export interface Patient {
  id: string;
  firstName: string;
  lastName: string;
  email: string;
  phoneNumber: string;
  medicalRecords: MedicalRecord[];
}
