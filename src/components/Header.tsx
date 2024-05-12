// Header.tsx
import React from 'react';
import { Link } from 'react-router-dom';

const Header = () => {
  return (
    <header>
      <nav>
        <ul>
          <li>
            <Link to="/">Dashboard</Link>
          </li>
          <li>
            <Link to="/patients">Patients</Link>
          </li>
        </ul>
      </nav>
    </header>
  );
};

export default Header;
