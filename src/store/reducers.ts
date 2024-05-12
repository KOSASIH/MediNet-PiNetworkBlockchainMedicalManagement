// reducers.ts
import { combineReducers } from 'redux';
import medicalRecordsReducer from './medicalRecordsReducer';

const rootReducer = combineReducers({
  medicalRecords: medicalRecordsReducer,
});

export default rootReducer;
