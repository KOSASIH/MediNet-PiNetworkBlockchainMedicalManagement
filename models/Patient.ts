export interface Patient {
  id: string;
  firstName: string;
  lastName: string;
  email: string;
  phoneNumber: string;
  medicalRecords: MedicalRecord[];
  createdAt: Date;
  updatedAt: Date;
}
