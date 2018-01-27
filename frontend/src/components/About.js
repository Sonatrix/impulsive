import React from 'react';
import { Jumbotron } from 'reactstrap';
import Navigation from './Navigation'

const Home = (props) => {
  return (
    <div className="fluid-container">
      <Navigation />
      <Jumbotron>
        <p>About Us
        </p>
      </Jumbotron>
    </div>
  );
};

export default Home;

