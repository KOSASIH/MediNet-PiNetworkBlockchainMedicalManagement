import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import { Container, Typography } from '@material-ui/core';

const useStyles = makeStyles((theme) => ({
  footer: {
    backgroundColor: theme.palette.background.paper,
    padding: theme.spacing(6, 0),
  },
  copyright: {
    marginTop: theme.spacing(2),
  },
}));

const Footer: React.FC = () => {
  const classes = useStyles();

  return (
    <footer className={classes.footer}>
      <Container maxWidth="lg">
        <Typography variant="body1" color="textSecondary" align="center">
          {'Copyright © '}
          <a
            color="inherit"
            href="https://www.yourwebsite.com/"
            target="_blank"
            rel="noopener"
          >
            Your Company
          </a>{' '}
          {new Date().getFullYear()}
          {'.'}
        </Typography>
      </Container>
    </footer>
  );
};

export default Footer;
