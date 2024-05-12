import React from 'react';
import { render, fireEvent } from '@testing-library/react';
import { Input } from './Input';

describe('Input', () => {
  it('renders correctly', () => {
    const { getByPlaceholderText } = render(<Input placeholder="Enter text" />);
    expect(getByPlaceholderText('Enter text')).toBeInTheDocument();
  });

  it('updates value when typed', () => {
    const onChange = jest.fn();
    const { getByPlaceholderText } = render(<Input placeholder="Enter text" onChange={onChange} />);
    fireEvent.change(getByPlaceholderText('Enter text'), { target: { value: 'Hello, world!' } });
    expect(onChange).toHaveBeenCalledTimes(1);
    expect(onChange).toHaveBeenCalledWith('Hello, world!');
  });
});
