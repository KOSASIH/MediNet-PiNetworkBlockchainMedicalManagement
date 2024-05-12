import React from 'react';
import { render } from '@testing-library/react';
import { Loader } from './Loader';

describe('Loader', () => {
  it('renders correctly', () => {
    const { getByTestId } = render(<Loader data-testid="loader" />);
    expect(getByTestId('loader')).toBeInTheDocument();
  });
});
