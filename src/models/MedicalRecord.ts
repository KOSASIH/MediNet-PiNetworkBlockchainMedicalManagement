export interface MedicalRecord {
  id: string;
  patientId: string;
  doctorId: string;
  date: Date;
  diagnosis: string;
  prescription: string;
}
