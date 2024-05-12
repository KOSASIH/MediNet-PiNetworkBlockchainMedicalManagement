import React from 'react';
import { BrowserRouter as Router } from 'react-router-dom';
import { DashboardContainer } from './dashboard';
import { PatientProfileContainer } from './patientProfile';

const App: React.FC = () => {
  return (
    <Router>
      <Switch>
        <Route path="/dashboard" component={DashboardContainer} />
        <Route path="/patient-profile" component={PatientProfileContainer} />
      </Switch>
    </Router>
  );
};

export default App;
