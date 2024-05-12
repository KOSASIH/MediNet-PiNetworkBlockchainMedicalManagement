import React from 'react';
import { render } from '@testing-library/react';
import { MedicalHistory } from '../MedicalHistory';

describe('MedicalHistory', () => {
  it('renders correctly', () => {
    const medicalHistory = [
      { date: '01/01/2022', condition: 'Flu' },
      { date: '03/15/2021', condition: 'Broken arm' },
      { date: '06/10/2020', condition: 'Strep throat' },
    ];
    const { getByText } = render(<MedicalHistory medicalHistory={medicalHistory} />);
    expect(getByText('01/01/2022')).toBeInTheDocument();
    expect(getByText('Flu')).toBeInTheDocument();
    expect(getByText('03/15/2021')).toBeInTheDocument();
    expect(getByText('Broken arm')).toBeInTheDocument();
    expect(getByText('06/10/2020')).toBeInTheDocument();
    expect(getByText('Strep throat')).toBeInTheDocument();
  });
});
