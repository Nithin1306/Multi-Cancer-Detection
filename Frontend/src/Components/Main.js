// Main.js
import React from 'react';
import { Link } from 'react-router-dom';
import NavScrollExample from './Navbar/Navbar';
import Image from './Images/Main.jpeg';
import './Images/Main.css'; // Import your CSS file
import Button from 'react-bootstrap/esm/Button';

function Main() {
  return (
    <>
      <NavScrollExample />
      <div className="main-container">
        <div className="image-container">
          <img src={Image} alt="Main" className="main-image" />
        </div>

        <div className="text-container">
          <h1>
            <span className="highlight"> <b>Your Life Our Prediction</b></span>
            <br />
          </h1>
          <div className='text1'>
            <h1> </h1>
          </div>
        </div>

        <div className="button-container">
          <Link to="/lung">
            <Button className='button1'>Lung</Button>
          </Link>
          <Link to="/brain">
            <Button className='button1'>Brain</Button>
          </Link>
          <Link to="/breast">
            <Button className='button1'>Breast</Button>
          </Link>
          <Link to="/kidney">
            <Button className='button1'>Kidney</Button>
          </Link>
        </div>
      </div>
    </>
  );
}

export default Main;
