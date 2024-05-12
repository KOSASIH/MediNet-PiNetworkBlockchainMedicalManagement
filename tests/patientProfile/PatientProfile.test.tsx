import React from 'react';
import { render } from '@testing-library/react';
import { PatientProfile } from '../PatientProfile';

describe('PatientProfile', () => {
  it('renders correctly', () => {
    const patient = {
      name: 'John Doe',
      age: 30,
      gender: 'Male',
      address: '123 Main St, Anytown USA',
    };
    const { getByText } = render(<PatientProfile patient={patient} />);
    expect(getByText('John Doe')).toBeInTheDocument();
    expect(getByText('30')).toBeInTheDocument();
    expect(getByText('Male')).toBeInTheDocument();
    expect(getByText('123 Main St, Anytown USA')).toBeInTheDocument();
  });
});
