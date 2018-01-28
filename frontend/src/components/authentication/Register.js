import React, {Component} from 'react'

export default class Register extends Component {
  state = {
    username: '',
    password: ''
  }

  handleInputChange = (event) => {
    const target = event.target;
    const value = target.type ===
        'checkbox' ? target.checked : target.value;
    const name = target.name;

    this.setState({
      [name]: value
    });
  }

  componentDidMount() {
    //this.primaryInput?this.primaryInput.focus():'';
  }

  onSubmit = (event) => {
    event.preventDefault()
    this.props.onSubmit(this.state.username, this.state.password)
  }

  render() {
    const errors = this.props.errors || {}

    return (
	    <div className="card card-register mx-auto mt-5">
	      <div className="card-header">Register an Account</div>
	      <div className="card-body">
	        <form>
	          <div className="form-group">
	            <div className="form-row">
	              <div className="col-md-6">
	                <label for="exampleInputName">First name</label>
	                <input className="form-control" id="exampleInputName" type="text" aria-describedby="nameHelp" placeholder="Enter first name"/>
	              </div>
	              <div className="col-md-6">
	                <label for="exampleInputLastName">Last name</label>
	                <input className="form-control" id="exampleInputLastName" type="text" aria-describedby="nameHelp" placeholder="Enter last name"/>
	              </div>
	            </div>
	          </div>
	          <div className="form-group">
	            <label for="exampleInputEmail1">Email address</label>
	            <input className="form-control" id="exampleInputEmail1" type="email" aria-describedby="emailHelp" placeholder="Enter email"/>
	          </div>
	          <div className="form-group">
	            <div className="form-row">
	              <div className="col-md-6">
	                <label for="exampleInputPassword1">Password</label>
	                <input className="form-control" id="exampleInputPassword1" type="password" placeholder="Password"/>
	              </div>
	              <div className="col-md-6">
	                <label for="exampleConfirmPassword">Confirm password</label>
	                <input className="form-control" id="exampleConfirmPassword" type="password" placeholder="Confirm password"/>
	              </div>
	            </div>
	          </div>
	          <a className="btn btn-primary btn-block" href="login.html">Register</a>
	        </form>
	        <div className="text-center">
	          <a className="d-block small mt-3" href="login.html">Login Page</a>
	          <a className="d-block small" href="forgot-password.html">Forgot Password?</a>
	        </div>
	      </div>
	    </div>
    )
  }
}
