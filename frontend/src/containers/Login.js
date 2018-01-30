import React from 'react';
import { connect } from 'react-redux';
import { Redirect } from 'react-router';

import LoginForm from '../components/LoginForm';
import { login } from '../actions/auth';
import { authErrors, isAuthenticated } from '../reducers';
import Navigation from '../components/Navigation';

const Login = props => {
  if (props.isAuthenticated) {
    return <Redirect to="/" />;
  }

  return (
    <div>
      <Navigation />
      <section className="login-block" style={{ marginTop: 80 }}>
        <div className="container">
          <div className="row">
            <div className="col-md-4">
              <LoginForm {...props} />
            </div>
            <div className="col-md-8 right-sec">
              <img
                className="img-fluid"
                src="http://placehold.it/900x400"
                alt=""
              />
            </div>
          </div>
        </div>
      </section>
    </div>
  );
};

const mapStateToProps = state => ({
  errors: authErrors(state),
  isAuthenticated: isAuthenticated(state)
});

const mapDispatchToProps = dispatch => ({
  onSubmit: (username, password) => {
    dispatch(login(username, password));
  }
});

export default connect(mapStateToProps, mapDispatchToProps)(Login);
