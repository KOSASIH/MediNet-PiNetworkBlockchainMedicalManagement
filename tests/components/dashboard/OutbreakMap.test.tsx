import React from 'react';
import { render } from '@testing-library/react';
import { OutbreakMap } from '../OutbreakMap';

describe('OutbreakMap', () => {
  it('renders correctly', () => {
    const data = [
      { lat: 37.7749, lng: -122.4194, name: 'Outbreak 1' },
      { lat: 34.0522, lng: -118.2437, name: 'Outbreak 2' },
      { lat: 40.7128, lng: -74.0060, name: 'Outbreak 3' },
    ];
    const { getByText } = render(<OutbreakMap data={data} />);
    expect(getByText('Outbreak 1')).toBeInTheDocument();
    expect(getByText('Outbreak 2')).toBeInTheDocument();
    expect(getByText('Outbreak 3')).toBeInTheDocument();
  });
});
