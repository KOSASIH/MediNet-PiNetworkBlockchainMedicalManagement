import { PatientState, patientReducer } from './patient.reducer';
import { PatientActions } from './patient.actions';

describe('PatientReducer', () => {
  let state: PatientState;

  beforeEach(() => {
    state = {
      patients: [],
    };
  });

  it('should handle the CREATE_NEW_PATIENT action', () => {
    const action = PatientActions.createNewPatient({ name: 'John Doe', age: 30 });
    const newState = patientReducer(state, action);
    expect(newState).toBeDefined();
    expect(newState.patients.length).toBe(1);
    expect(newState.patients[0].name).toBe('John Doe');
    expect(newState.patients[0].age).toBe(30);
  });

  it('should handle the UPDATE_PATIENT action', () => {
    const initialState = {
      patients: [
        { id: 1, name: 'John Doe', age: 30 },
      ],
    };
    const action = PatientActions.updatePatient({ id: 1, name: 'Jane Doe', age: 35 });
    const newState = patientReducer(initialState, action);
    expect(newState).toBeDefined();
    expect(newState.patients.length).toBe(1);
    expect(newState.patients[0].name).toBe('Jane Doe');
    expect(newState.patients[0].age).toBe(35);
  });

  it('should handle the DELETE_PATIENT action', () => {
    const initialState = {
      patients: [
        { id: 1, name: 'John Doe', age: 30 },
        { id: 2, name: 'Jane Doe', age: 35 },
      ],
    };
    const action = PatientActions.deletePatient({ id: 1 });
    const newState = patientReducer(initialState, action);
    expect(newState).toBeDefined();
    expect(newState.patients.length).toBe(1);
    expect(newState.patients[0].id).toBe(2);
  });
});
