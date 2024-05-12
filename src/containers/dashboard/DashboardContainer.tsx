import React from 'react';
import { useSelector } from 'react-redux';
import { Dashboard } from '../../components/dashboard';

const DashboardContainer: React.FC = () => {
  const isAuthenticated = useSelector((state) => state.auth.isAuthenticated);

  if (!isAuthenticated) {
    return <div>Please log in to access the dashboard.</div>;
  }

  return <Dashboard />;
};

export default DashboardContainer;
