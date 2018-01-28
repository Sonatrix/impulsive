import React, {Component} from 'react'
import { Alert, Button,  Form } from 'reactstrap';

import TextInput from './TextInput'

export default class LoginForm extends Component {
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
      <div className="container">
        <Form onSubmit={this.onSubmit}>
          <h2>Login Here</h2>
          {errors.non_field_errors?<Alert color="danger">{errors.non_field_errors}</Alert>:""}
          <TextInput name="username" label="Username" error={errors.username} onChange={this.handleInputChange}/>
          <TextInput name="password" label="Password" error={errors.password} type="password" onChange={this.handleInputChange}/>
          <Button type="submit" color="primary">Log In</Button>
        </Form>
      </div>
    )
  }
}
