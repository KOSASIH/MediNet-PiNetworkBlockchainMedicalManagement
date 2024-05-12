// Improved code
import Patient from '../models/patient';
import capitalizeFirstLetter from '../../utils/stringUtils';

describe('Patient', () => {
  it('should have a name', () => {
    const patient = new Patient('John Doe', 30, ['diabetes']);
    expect(patient.name).toBe('John Doe');
  });

  it('should have an age', () => {
    const patient = new Patient('John Doe', 30, ['diabetes']);
    expect(patient.age).toBe(30);
  });

  it('should have medical history', () => {
    const patient = new Patient('John Doe', 30, ['diabetes']);
    expect(patient.medicalHistory).toEqual(['diabetes']);
  });

  it('should capitalize the first letter of the name', () => {
    const patient = new Patient('john doe', 30, ['diabetes']);
    expect(patient.name).toBe('John Doe');
  });

  it('should have a default specialty', () => {
    const patient = new Patient('John Doe', 30, ['diabetes']);
    expect(patient.specialty).toBe('');
  });

  it('should return the specialty', () => {
    const patient = new Patient('John Doe', 30, ['diabetes'], 'general practitioner');
    expect(patient.getSpecialty()).toBe('general practitioner');
  });
});
