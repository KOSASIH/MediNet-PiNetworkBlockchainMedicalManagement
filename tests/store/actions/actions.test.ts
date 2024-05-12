import { PatientActions } from './patient.actions';

describe('PatientActions', () => {
  it('should create a new patient action', () => {
    const action = PatientActions.createNewPatient({ name: 'John Doe', age: 30 });
    expect(action).toBeDefined();
    expect(action.type).toBe('CREATE_NEW_PATIENT');
    expect(action.payload).toEqual({ name: 'John Doe', age: 30 });
  });

  it('should update a patient action', () => {
    const action = PatientActions.updatePatient({ id: 1, name: 'Jane Doe', age: 35 });
    expect(action).toBeDefined();
    expect(action.type).toBe('UPDATE_PATIENT');
    expect(action.payload).toEqual({ id: 1, name: 'Jane Doe', age: 35 });
  });

  it('should delete a patient action', () => {
    const action = PatientActions.deletePatient({ id: 1 });
    expect(action).toBeDefined();
    expect(action.type).toBe('DELETE_PATIENT');
    expect(action.payload).toEqual({ id: 1 });
  });
});
