import React,{Component} from 'react';
//import Quizdata from './questionbank.json';
import 'bootstrap/dist/css/bootstrap.css';
import axios from 'axios';
import Pagination from './pagination';
import {Button} from 'react-bootstrap'
import {connect} from 'react-redux';

import {notes, auth} from "../actions";

class Quiz extends React.Component{
  constructor(props) {
    super(props);
    this.state = {
      useranswers:[],
      quiz: [],
      questions:[],

      currentpage:1,
      postsPerPage:1,
      Token: localStorage.getItem("token"),

    }
    
    this.paginate=this.paginate.bind(this)

  }

  componentDidMount(){
  console.log(axios.default.headers)
    const {handle} =this.props.match.params
    axios.get('http://127.0.0.1:8000/api/auth/quizzes/'+handle+'/' ,{
      headers: {
        
      "Authorization": "Token "+this.state.Token


      }

}
      )
    .then(response => {
      console.log(response);
      this.setState({useranswers:response.data.quiz.quiztakers_set})
      this.setState({quiz:response.data.quiz})
      this.setState({questions:response.data.quiz.question_set})
      console.log(response);
       })
    .catch(error => {
      console.log(error);
    })
  }
    
    

   
   
    paginate=(pageno)=> {
    
    this.setState({
      currentpage:pageno
    });
  }



  
onAnswer(q, option) {
    let temp = {};
console.log(q)
console.log(option)
temp=this.state.useranswers.usersanswer_set
{temp.map(name => {
  
  
    if(name.question===q.id)
      {


        if(name.answer===option.id){
     name.answer=null}
    else{
      name.answer=option.id 

    }
  }
    console.log(name.question)

}
)

    }
console.log(temp)

    

this.state.useranswers.usersanswer_set=temp;

console.log(this.state.useranswers)
  }
    
    
onSubmit()
{
  this.state.useranswers.completed=true;
  <Link to={"/"+item.slug}+result>
  </Link>
}  

  

  render(){
console.log(this.state.quiz)

    return(

    <div id="quiz">
    <h2 className="text-center font-weight-normal">Quiz</h2>
    <hr />
    { (this.state.questions) .map(q =>
        <div key={q.id}>
            <div className="badge badge-info">Question </div>
            
            <h3 className="font-weight-normal">
            <span>{q.text}</span></h3>
            <div className="row text-left options">
                {
                    q.answer_set.map(option =>
                        <div key={option.id} className="col-6">
                        <div className="option">
                        <label className="font-weight-normal" htmlFor={option.id}>
                        <input id={option.id} checked={option.selected} type="checkbox" 

                         onChange={() => this.onAnswer(q, option)} />
                        {option.text}
                        </label>
                        </div>
                        </div>
                    )
                }
            </div>
        </div>

    )}
                    <hr/>
  
            <button id="submit" className="btn btn-primary"> Submit</button >
      
      </div>
    )
     
}


}



export default (Quiz);