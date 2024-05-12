import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import { AppBar, Toolbar, Typography } from '@material-ui/core';
import { ResourceChart } from './ResourceChart';
import { OutbreakMap } from './OutbreakMap';

const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
    padding: theme.spacing(3),
  },
  toolbar: {
    backgroundColor: theme.palette.primary.main,
  },
  title: {
    flexGrow: 1,
    textAlign: 'center',
  },
}));

const Dashboard: React.FC = () => {
  const classes = useStyles();

  return (
    <div className={classes.root}>
      <AppBar position="static" className={classes.toolbar}>
        <Toolbar>
          <Typography variant="h6" className={classes.title}>
            Dashboard
          </Typography>
        </Toolbar>
      </AppBar>
      <ResourceChart />
      <OutbreakMap />
    </div>
  );
};

export default Dashboard;
