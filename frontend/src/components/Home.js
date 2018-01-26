import React from 'react';
import { Jumbotron } from 'reactstrap';

const Home = (props) => {
  return (
    <div>
      <Jumbotron>
        <h1 className="display-3">Save and Earn Extra!</h1>
        <p>Tax breaks offered on your investments are not in the nature 
        of a discount or cashback - even though it feels like that. 
        You invest 10,000 and you immediately get a benefit in your 
        salary slip. Instead, they are an incentive for you to prepare 
        for the long term. Just consider the range of investment options 
          that qualify for a tax break: your employee provident fund 
        contribution (meant for retirement) qualifies for it, so does 
        your Public Provident Fund; Life Insurance is supposed to replace 
        your earning capacity for your loved ones, it too qualifies for a 
        tax break; equity funds help you beat inflation over the long term, 
        they figure in the list too.
        </p>
      </Jumbotron>
    </div>
  );
};

export default Home;

