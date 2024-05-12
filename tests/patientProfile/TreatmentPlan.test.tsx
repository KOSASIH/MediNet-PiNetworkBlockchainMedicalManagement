import React from 'react';
import { render } from '@testing-library/react';
import { TreatmentPlan } from '../TreatmentPlan';

describe('TreatmentPlan', () => {
  it('renders correctly', () => {
    const treatmentPlan = [
      { name: 'Medication 1', dosage: '2x/day' },
      { name: 'Medication 2', dosage: '1x/day' },
      { name: 'Physical therapy', frequency: '3x/week' },
    ];
    const { getByText } = render(<TreatmentPlan treatmentPlan={treatmentPlan} />);
    expect(getByText('Medication 1')).toBeInTheDocument();
    expect(getByText('2x/day')).toBeInTheDocument();
    expect(getByText('Medication 2')).toBeInTheDocument();
    expect(getByText('1x/day')).toBeInTheDocument();
    expect(getByText('Physical therapy')).toBeInTheDocument();
    expect(getByText('3x/week')).toBeInTheDocument();
  });
});
