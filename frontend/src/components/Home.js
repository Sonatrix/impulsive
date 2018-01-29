import React from 'react';
import Heading from './Heading';
import Tagline from './Tagline';
import Card from './Card';
import Register from './authentication/Register';
import RecommendProduct from './RecommendProducts';

const Home = (props) => {
  return (
    <div className="container" style={{paddingTop:'60px'}}>
      <Heading />
      <Tagline />
      <div className="row">
      {[1, 2, 3].map((index) => <Card />)}
      </div>
      <div className="row mb-4">
        <RecommendProduct title="Featured Insurance Plans"/>
      </div>
      <div className="row mb-4">
        <RecommendProduct title="Loans At Lowest rates"/>
      </div>
    </div>
  );
};

export default Home;

