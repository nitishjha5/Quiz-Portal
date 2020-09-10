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
      quiz:[],
      currentpage:1,
      postsPerPage:1,

    }
    
    this.paginate=this.paginate.bind(this)

  }

  static getDerivedStateFromProps (newProps,state){
    
    console.log(newProps)
    if(newProps.Token){
   /* axios.default.headers={
      "Content-Type": "application/json",
      "Authorization": "Token "++newProps.Token
    }
    console.log(axios.default.headers)*/
    const {handle} =newProps.match.params
    axios.get('http://127.0.0.1:8000/api/auth/quizzes/'+handle+'/' ,{
      headers: {
        
      "Authorization": "Token "+newProps.Token


      }

}
      )
    .then(response => {
      console.log(response.data.quiz);
      
      return {
          quiz:response.data.quiz,
          currentpage:1,
      postsPerPage:1,

    };

      
    })
    .catch(error => {
      console.log(error);
    })

   }
return null;

    }
   
    

   
   
    paginate=(pageno)=> {
    
    this.setState({
      currentpage:pageno
    });
  }



  
   onAnswer(question, option) {
    if(option.select===false){
      {
        console.log(option.text)
      option.select=true;
      }
    }
    else{

        console.log(option.text)
      option.select=false;
      
    }
  }
    
    
       

  

  render(){
console.log(this.state.quiz)

 var indexofLastPost=(this.state.currentpage)*(this.state.postsPerPage);
   var indexofFirstPost=indexofLastPost-(this.state.postsPerPage);
  //len=quizs.length;
   var currentPost=(this.state.quiz).slice(indexofFirstPost,indexofLastPost);
    return(

    <div id="quiz" className="container">
    <h2 className="text-center font-weight-normal">Quiz-Questions</h2>
    <hr />
    {currentPost.map(q =>
        <div key={q.id}>
            <div className="badge badge-info">
            
            <h3 className="font-weight-normal">
            <span>{q.qno}. {q.question_set.text}</span></h3>
            <div className="row text-left options">
                {
                    q.options.map(option =>
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
        </div>
    )}
                    <hr/>
   <Pagination postsPerPage={this.state.postsPerPage} totalpost={this.state.quiz.length} paginate={this.paginate}/>
            <button id="submit" className="btn btn-primary" onClick={this.setMode}>Submit Quiz</button >
      
      </div>
    )
     
}


}


const mapStateToProps = state => {
  console.log(state.auth)
    return {
        Token: state.auth.token

    }
}

export default connect(mapStateToProps)(Quiz);

