import React from 'react';

const Card = (props) => {
  return (
  	<div className="col-md-4 mb-4">
      <div className="card h-100">
        <div className="card-body">
          <h2 className="card-title">Card One</h2>
          <p className="card-text">Lorem ipsum dolor sit amet, consectetur adipisicing elit. Rem magni quas ex numquam, maxime minus quam molestias corporis quod, ea minima accusamus.</p>
        </div>
        <div className="card-footer">
          <a href="#" className="btn btn-primary">More Info</a>
        </div>
      </div>
    </div>
  )
}

export default Card;