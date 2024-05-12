import React from 'react';
import { render } from '@testing-library/react';
import { Dashboard } from '../Dashboard';

describe('Dashboard', () => {
  it('renders correctly', () => {
    const { getByText } = render(<Dashboard />);
    expect(getByText('Dashboard')).toBeInTheDocument();
  });
});
