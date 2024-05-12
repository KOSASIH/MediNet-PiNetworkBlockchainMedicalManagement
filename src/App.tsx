import React from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { getMedicalRecords } from './utils/helpers';
import { MedicalRecord } from './models/MedicalRecord';

const App: React.FC = () => {
  const dispatch = useDispatch();
  const medicalRecords = useSelector((state: any) => state.medicalRecords);

  const fetchMedicalRecords = async () => {
    const records = await getMedicalRecords();
    dispatch({ type: 'SET_MEDICAL_RECORDS', payload: records });
  };

  return (
    <div>
      <h1>Medical Records</h1>
      <button onClick={fetchMedicalRecords}>Fetch Medical Records</button>
      <ul>
        {medicalRecords.map((record: MedicalRecord) => (
          <li key={record.id}>
            <h3>{record.date}</h3>
            <p>{record.diagnosis}</p>
            <p>{record.prescription}</p>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default App;
