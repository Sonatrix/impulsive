import React, { Component } from 'react';
import { connect } from 'react-redux'

import {echo} from './actions/echo'
import {serverMessage} from './reducers'
import Navigation from './components/Navigation'
import Home from './components/Home'
import Footer from './components/Footer';

class App extends Component {
  componentDidMount() {
      this.props.fetchMessage('Hi!')
  }

  render() {
    return (
      <div className="fluid-container">
        <Navigation {...this.props}/>
        <Home />
        <Footer />
      </div>
    );
  }
}

export default connect(
  state => ({ message: serverMessage(state) }),
  { fetchMessage: echo }
)(App);
