import React ,{Component}from 'react';


class Login extends Component {
	state={
		credentials: {username: '',password: ''}
	}
	login= event=>{
		console.log(this.state.credentials)
		fetch('http://127.0.0.1:8000/auth/',{
			method: 'POST',
			headers: {'Content-Type':'application/json'},
			body: JSON.stringify(this.state.credentials)
	}).then(
	data=>{
		data.json()
	}).catch(
	error=>{
		console.log(error)
	})
	}
	register= event=>{
		console.log(this.state.credentials)
		fetch('http://127.0.0.1:8000/api/User',{
			method: 'POST',
			headers: {'Content-Type':'application/json'},
			body: JSON.stringify(this.state.credentials)
	}).then(
	data=>{
		data.json()
	}).catch(
	error=>{
		console.log(error)
	})
	}
	inputChanged=event=>{
		const cred=this.state.credentials
		cred[event.target.name]=event.target.value
		this.setState({credentials:cred})
	}
	render(){

  return (
    <div className="App">
    
          <h1> Login </h1>
          <label>
          Username:
          <input type="text" name ="username" 
          value={this.state.credentials.username} 
          onChange={this.inputChanged} />
          </label>
          <br/>
          <label>
          Password:
          <input type="password" name ="password"
          value={this.state.credentials.password} 
          onChange={this.inputChanged} />
          </label>
          <br/>
          <button onClick={this.login} > Login </button>
          <button onClick={this.register} > Register </button>
          
      
    </div>
  );
}
}

export default Login;
