import React from 'react';
import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import Button from 'react-bootstrap/Button';
import "./Navbar.css"

function NavScrollExample() {
  return (
    <Navbar expand="lg" className="bg-body-tertiary">
      <Container fluid>
        <Navbar.Brand>Multi Organ Detection</Navbar.Brand>
        <Navbar.Toggle aria-controls="navbarScroll" />
        <Navbar.Collapse id="navbarScroll">
          <Nav
            className="me-auto my-2 my-lg-0"
            style={{ maxHeight: '100px' }}
            navbarScroll
          ></Nav>
          {/* Add the justify-content-end class to align links to the right */}
          <Nav className="justify-content-end">
            <Nav.Link href="/">Home</Nav.Link>
            <Nav.Link href="/aboutus">About Us</Nav.Link>
            <Nav.Link href="/Location">Location</Nav.Link>
            <Nav.Link href="#action2">Specialities</Nav.Link>
            <Nav.Link href="#action2">Book an Appointment</Nav.Link>
            {/* Use Button component for the Login link */}
            <Button variant="primary" href="#action2">
              Login
            </Button>
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
}

export default NavScrollExample;
