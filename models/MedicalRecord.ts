export interface MedicalRecord {
  id: string;
  patientId: string;
  medicalHistory: string;
  allergies: string;
  medications: string;
  createdAt: Date;
  updatedAt: Date;
}
