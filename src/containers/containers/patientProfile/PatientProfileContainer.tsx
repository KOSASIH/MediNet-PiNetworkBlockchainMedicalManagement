import React from 'react';
import { useSelector } from 'react-redux';
import { PatientProfile } from '../../components/patientProfile';

const PatientProfileContainer: React.FC = () => {
  const isAuthenticated = useSelector((state) => state.auth.isAuthenticated);
  const patientId = useSelector((state) => state.auth.patientId);

  if (!isAuthenticated) {
    return <div>Please log in to access your patient profile.</div>;
  }

  if (!patientId) {
    return <div>Please select a patient to view their profile.</div>;
  }

  return <PatientProfile patientId={patientId} />;
};

export default PatientProfileContainer;
