import React from 'react';
import styled from 'styled-components';

const InputStyled = styled.input`
  background-color: ${(props) => props.theme.inputBackgroundColor};
  color: ${(props) => props.theme.textColor};
  border: none;
  border-radius: 5px;
  padding: 10px 20px;
  font-size: 16px;
  width: 100%;
  box-sizing: border-box;
  transition: background-color 0.3s ease;

  &:focus {
    background-color: ${(props) => props.theme.inputFocusBackgroundColor};
  }
`;

interface InputProps {
  value: string;
  onChange: (event: React.ChangeEvent<HTMLInputElement>) => void;
  placeholder?: string;
}

const Input: React.FC<InputProps> = ({ value, onChange, placeholder }) => {
  return (
    <InputStyled
      value={value}
      onChange={onChange}
      placeholder={placeholder}
    />
  );
};

export default Input;
