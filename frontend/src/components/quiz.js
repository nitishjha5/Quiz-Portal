import React,{Component} from 'react';
//import Quizdata from './questionbank.json';
import 'bootstrap/dist/css/bootstrap.css';
import axios from 'axios';
import Pagination from './pagination';
import {Button} from 'react-bootstrap'
class Quiz extends Component{
  constructor(props) {
    super(props);
    this.state = {
      quiz:[],
      currentpage:1,
      postsPerPage:1,

    }
    this.paginate=this.paginate.bind(this)

  }
  componentDidMount(){
    axios.get('http://127.0.0.1:8000/api/auth/question/')
    .then(response => {
      this.setState({quiz:response.data})
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
    
    setMode=(e)=>{
      e.preventDefault();
      console.log(this.state.quiz);
      axios.post('http://127.0.0.1:8000/api/auth/question/',this.state.quiz)
    .then(response => {
      
      console.log(response);
    })
    .catch(error => {
      console.log(error);
    })


    }
        /*let quiz = JSON.parse(JSON.stringify(this.props.quiz));
        let q = quiz.questions.find(x => x.id === question.id);
        if (q.questionTypeId === 1) {
            q.options.forEach((x) => { x.selected = false; });
        }
        q.options.find(x => x.id === option.id).selected = true;
        this.props.onAnswer(quiz);*/
    


  

  render(){

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
            <span>{q.qno}. {q.text}</span></h3>
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

export default Quiz;
