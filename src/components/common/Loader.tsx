import React from 'react';
import styled from 'styled-components';

const LoaderStyled = styled.div`
  border: 4px solid ${(props) => props.theme.loaderColor};
  border-top: 4px solid ${(props) => props.theme.primaryColor};
  border-radius: 50%;
  width: 30px;
  height: 30px;
  animation: spin 1s linear infinite;

  @keyframes spin {
    0% {
      transform: rotate(0deg);
    }
    100% {
      transform: rotate(360deg);
    }
  }
`;

interface LoaderProps {
  size?: number;
}

const Loader: React.FC<LoaderProps> = ({ size = 30 }) => {
  return <LoaderStyled style={{ width: size, height: size }} />;
};

export default Loader;
