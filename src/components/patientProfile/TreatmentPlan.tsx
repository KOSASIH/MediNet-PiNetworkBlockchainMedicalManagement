import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import { Card, CardContent, Typography } from '@material-ui/core';
import { TreatmentPlanItem } from './TreatmentPlanItem';

const useStyles = makeStyles((theme) => ({
  root: {
    marginTop: theme.spacing(3),
  },
  card: {
    marginBottom: theme.spacing(2),
  },
}));

interface TreatmentPlanItemProps {
  name: string;
  description: string;
  status: string;
}

const TreatmentPlanItem: React.FC<TreatmentPlanItemProps> = ({
  name,
  description,
  status,
}) => {
  const classes = useStyles();

  return (
    <Card className={classes.card}>
      <CardContent>
        <Typography variant="subtitle1">{name}</Typography>
        <Typography variant="body1">{description}</Typography>
        <Typography variant="body2" color="textSecondary">
          Status: {status}
        </Typography>
      </CardContent>
    </Card>
  );
};

const TreatmentPlan: React.FC = () => {
  const classes = useStyles();

  const treatmentPlan = [
    {
      name: 'Medication 1',
      description: 'Take 1 tablet twice a day',
      status: 'In Progress',
    },
    {
      name: 'Physiotherapy',
      description: 'Attend physiotherapy sessions twice a week',
      status: 'Not Started',
    },
  ];

  return (
    <div className={classes.root}>
      {treatmentPlan.map((item) => (
        <TreatmentPlanItem key={item.name} {...item} />
      ))}
    </div>
  );
};

export default TreatmentPlan;
