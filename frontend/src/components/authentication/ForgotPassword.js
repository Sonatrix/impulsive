import React , {Component}from 'react'

export default class ForgotPassword extends Component {
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
	    <div className="card card-login mx-auto mt-5">
	      <div className="card-header">Reset Password</div>
	      <div className="card-body">
	        <div className="text-center mt-4 mb-5">
	          <h4>Forgot your password?</h4>
	          <p>Enter your email address and we will send you instructions on how to reset your password.</p>
	        </div>
	        <form>
	          <div className="form-group">
	            <input className="form-control" id="exampleInputEmail1" type="email" aria-describedby="emailHelp" placeholder="Enter email address">
	          </div>
	          <a className="btn btn-primary btn-block" href="login.html">Reset Password</a>
	        </form>
	        <div className="text-center">
	          <a className="d-block small mt-3" href="register.html">Register an Account</a>
	          <a className="d-block small" href="login.html">Login Page</a>
	        </div>
	      </div>
	    </div>
    )
  }
}
