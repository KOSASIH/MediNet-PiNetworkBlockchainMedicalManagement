import React from 'react';
import { useParams } from 'react-router-dom';
import { Patient } from '../models/Patient';
import { useQuery } from 'react-query';
import { getPatient } from '../api/patients';
import { PatientInfo } from '../components/PatientInfo';

export const PatientProfile: React.FC = () => {
  const { id } = useParams<{ id: string }>();
  const { data: patient } = useQuery<Patient, Error>(['patient', id], () => getPatient(id));

  if (!patient) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      <PatientInfo patient={patient} />
    </div>
  );
};
