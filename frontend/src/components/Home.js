import React from 'react';
import Heading from './Heading';
import Tagline from './Tagline';
import Card from './Card';
import Register from './authentication/Register';

const Home = (props) => {
  return (
    <div className="container" style={{paddingTop:'60px'}}>
      <Heading />
      <Tagline />
      <Register/>
      <div className="row">
      {[1, 2, 3].map((index) => <Card />)}
      </div>
    </div>
  );
};

export default Home;

