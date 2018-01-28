import React from 'react';

const Heading = (props) => {
  return (
    <div className="row my-4">
      <div className="col-lg-8">
        <img className="img-fluid rounded" src="http://placehold.it/900x400" alt=""/>
      </div>
      <div className="col-lg-4">
        <h1>Business Name or Tagline</h1>
        <p>This is a template that is great for small businesses. It doesn't have too much fancy flare to it, but it makes a great use of the standard Bootstrap core components. Feel free to use this template for any project you want!</p>
        <a className="btn btn-primary btn-lg" href="#">Call to Action!</a>
      </div>
    </div>
  );
};

export default Heading;

