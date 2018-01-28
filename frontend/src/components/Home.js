import React from 'react';
import Heading from './Heading';
import Tagline from './Tagline';
import Card from './Card';

const Home = (props) => {
  return (
    <div className="container" style={{paddingTop:'60px'}}>
      <Heading />
      <Tagline />
      <div className="row">
      {[1, 2, 3].map((index) => <Card />)}
      </div>
    </div>
  );
};

export default Home;

