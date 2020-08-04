import React, {Component} from 'react';

import './Footer.css';

class Footer extends Component {
  render() {
    return (
      <div className="row" id="footer">
        <div className="medium-12 columns">
          <p>For entertainment <a href="https://www.facebook.com">facebook</a></p>
        </div>
      </div>
    );
  }
}

export default Footer;