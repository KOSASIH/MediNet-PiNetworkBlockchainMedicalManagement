import React from 'react';
import { useStyles } from './Dashboard.styles';
import { PatientList } from '../components/PatientList';

export const Dashboard: React.FC = () => {
  const classes = useStyles();

  return (
    <div className={classes.root}>
      <PatientList />
    </div>
  );
};
