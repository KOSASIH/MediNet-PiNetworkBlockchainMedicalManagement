import React from 'react';
import { render } from '@testing-library/react';
import { ResourceChart } from '../ResourceChart';

describe('ResourceChart', () => {
  it('renders correctly', () => {
    const data = [
      { name: 'Resource 1', value: 10 },
      { name: 'Resource 2', value: 20 },
      { name: 'Resource 3', value: 30 },
    ];
    const { getByText } = render(<ResourceChart data={data} />);
    expect(getByText('Resource 1')).toBeInTheDocument();
    expect(getByText('Resource 2')).toBeInTheDocument();
    expect(getByText('Resource 3')).toBeInTheDocument();
  });
});
