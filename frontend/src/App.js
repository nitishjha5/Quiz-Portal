import React from 'react';
import './App.css';
//import Login from './components/login';
import {Navbar,NavDropdown} from 'react-bootstrap'
import Quiz from './components/quiz';


function App() {
  return (
    <div className="App">
<Navbar>
  <Navbar.Brand href="#home">Quiz-Portal</Navbar.Brand>
  <Navbar.Toggle />
  <Navbar.Collapse className="justify-content-end">
    <Navbar.Text>
    <NavDropdown title="nitish" id="basic-nav-dropdown">
        <NavDropdown.Item href="#action/3.1">My profile</NavDropdown.Item>
        <NavDropdown.Item href="#action/3.2">Perfomance</NavDropdown.Item>
        
        <NavDropdown.Divider />
        <NavDropdown.Item href="#action/3.4">Sign out</NavDropdown.Item>
      </NavDropdown>
      

    </Navbar.Text>
  </Navbar.Collapse>
</Navbar>
     
    <Quiz/>
    </div>
  );
}

export default App;
