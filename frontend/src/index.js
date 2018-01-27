import React from 'react';
import ReactDOM from 'react-dom';
import createHistory from 'history/createBrowserHistory'
import { ConnectedRouter } from 'react-router-redux'
import { Provider } from 'react-redux'
import {Route, Switch} from 'react-router'

import 'bootstrap/dist/css/bootstrap.css';
import App from './App';
import About from './components/About';
import PrivateRoute from './containers/PrivateRoute';
import configureStore from './store'

import Login from './containers/Login';
const history = createHistory()

const store = configureStore(history)

ReactDOM.render((
  <Provider store={store}>
    <ConnectedRouter history={history}>
      <Switch>
        <Route exact path="/" component={App} />
        <Route exact path="/about" component={About} />
        <Route exact path="/login" component={Login} />
        <PrivateRoute path="/" component={App}/>
      </Switch>
    </ConnectedRouter>
  </Provider>
), document.getElementById('root'));
