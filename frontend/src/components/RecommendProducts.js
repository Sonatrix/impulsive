import React, {Component} from 'react'
import Card from './Card';

export default class RecommendProduct extends Component {
	render() {
		const {title} = this.props;

		return (
			<div className="col-md-12">
				<div className="card">
				  <div className="card-header">
				    {title}
				  </div>
				  <div className="card-block">
				    <div className="card-group">
				    	{[1,2,3].map(()=> <Card/>)}
				    </div>
				  </div>
				</div>
			</div>
		)
	}
} 