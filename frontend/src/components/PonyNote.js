import React, { Component } from 'react';
import {Route, Switch, BrowserRouter, Redirect,Link} from 'react-router-dom';
import { Provider, connect } from "react-redux";
import {auth} from "../actions";
import {Navbar,NavDropdown} from 'react-bootstrap'
import QuizHome from './quiz_front';

class PonyNote extends Component {

  render() {
    return (
      <div className="container">
        
        <Navbar>
  <Navbar.Brand href="!#">Quiz-Portal</Navbar.Brand>
  <Navbar.Toggle />
  <Navbar.Collapse className="justify-content-end">
    <Navbar.Text>
    <NavDropdown title={this.props.user.username} id="basic-nav-dropdown">
        <NavDropdown.Item href="#action/3.1">My profile</NavDropdown.Item>
        <NavDropdown.Item href="#action/3.2">Perfomance</NavDropdown.Item>
        
        <NavDropdown.Divider />
        <NavDropdown.Item  onClick={this.props.logout}>Sign out</NavDropdown.Item>
      </NavDropdown>
      

    </Navbar.Text>
  </Navbar.Collapse>
</Navbar>

<QuizHome/>

        </div>

        

      
    )
  }
}


const mapStateToProps = state => {
  return {
    
    user: state.auth.user,
  }
}

const mapDispatchToProps = dispatch => {
  return {
    
    logout: () => dispatch(auth.logout()),
  }
}
export default connect(mapStateToProps, mapDispatchToProps)(PonyNote);


