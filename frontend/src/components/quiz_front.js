import React,{Component} from 'react';
//import Quizdata from './questionbank.json';
import 'bootstrap/dist/css/bootstrap.css';
import {Link} from 'react-router-dom';
import axios from 'axios';
import Pagination from './pagination';
import {Button,Card} from 'react-bootstrap'
class QuizHome extends Component{
  constructor(props) {
    super(props);
    this.state = {
      quiz:[],
      currentpage:1,
      postsPerPage:3,
    }
    this.paginate=this.paginate.bind(this)

  }
  componentDidMount(){
    axios.get('http://127.0.0.1:8000/api/auth/quiz/')
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



  

  render(){
    var indexofLastPost=(this.state.currentpage)*(this.state.postsPerPage);
   var indexofFirstPost=indexofLastPost-(this.state.postsPerPage);
  //len=quizs.length;
   var currentPost=(this.state.quiz).slice(indexofFirstPost,indexofLastPost);
    //const {quiz}=this.stste
    return(
      <div className="quizs">
        <h1>  All Quizs</h1>  
        
          {currentPost.map((item) =>             
              (<div> 
                  <Card>
  <Card.Header as="h5">{item.title}</Card.Header>
  <Card.Body>
    <Card.Title>Total Question: {item.no_of_ques}<br/> Total Marks:
    {item.full_marks}</Card.Title>
    <Card.Text>
      Start Time: {item.start_time} <br/> End Time: {item.end_time}
    </Card.Text>
    <Button variant="primary"><Link to="/quiz">Start Quiz</Link></Button>
  </Card.Body>
</Card>
   
              </div>
              ))}
            <Pagination postsPerPage={this.state.postsPerPage} totalpost={this.state.quiz.length} paginate={this.paginate}/>
      
      </div>
    );
  }
}
export default QuizHome;