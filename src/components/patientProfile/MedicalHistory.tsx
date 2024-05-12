import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import { Card, CardContent, Typography } from '@material-ui/core';
import { MedicalHistoryItem } from './MedicalHistoryItem';

const useStyles = makeStyles((theme) => ({
  root: {
    marginTop: theme.spacing(3),
  },
  card: {
    marginBottom: theme.spacing(2),
  },
}));

interface MedicalHistoryItemProps {
  date: string;
  description: string;
}

const MedicalHistoryItem: React.FC<MedicalHistoryItemProps> = ({
  date,
  description,
}) => {
  const classes = useStyles();

  return (
    <Card className={classes.card}>
      <CardContent>
        <Typography variant="subtitle1">{date}</Typography>
        <Typography variant="body1">{description}</Typography>
      </CardContent>
    </Card>
  );
};

const MedicalHistory: React.FC = () => {
  const classes = useStyles();

  const medicalHistory = [
    {
      date: '01/01/2022',
      description: 'Initial consultation with Dr. Smith',
    },
    {
      date: '02/01/2022',
      description: 'Blood tests ordered',
    },
    {
      date: '03/01/2022',
      description: 'MRI scan scheduled',
    },
  ];

  return (
    <div className={classes.root}>
     {medicalHistory.map((item) => (
        <MedicalHistoryItem key={item.date} {...item} />
      ))}
    </div>
  );
};

export default MedicalHistory;
