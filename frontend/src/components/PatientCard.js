// Improved code
import React from 'eact';
import PropTypes from 'prop-types';

const PatientCard = ({ patient }) => {
  const { name, age, medicalHistory } = patient;

  return (
    <div>
      <h2>{name}</h2>
      <p>Age: {age}</p>
      <p>Medical History: {medicalHistory.join(', ')}</p>
    </div>
  );
};

PatientCard.propTypes = {
  patient: PropTypes.shape({
    name: PropTypes.string.isRequired,
    age: PropTypes.number.isRequired,
    medicalHistory: PropTypes.arrayOf(PropTypes.string).isRequired,
  }).isRequired,
};

export default PatientCard;
