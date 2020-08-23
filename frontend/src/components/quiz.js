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

selectOption = (i,index) => () =>
  {
    
    const { quiz } =this.state;
    quiz[i].selectedAnswer=index;
    this.setState({
      ...this.state,
      quiz:quiz
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
        <h1> Quiz question(s)</h1>  
        
          {currentPost.map((item) => 

              (<div> 
                  <div><span>{item.qno}) </span> {item.text}
                  <div id='questions'>
                    {item.options.map((items,index)=> {
                      return (
                        <div > 
                          <div>
                          <h6>                  
    <label key={index}>
        <input type="radio" 
                 
                value={items.id} 
                key={index}
                
                />
                {items.text}
        </label>
                          </h6>

                          </div>
                        </div>
                      )
                    })}
                    </div>

                  </div>

                  <hr/>     
              </div>

              ))
            }
            <Pagination postsPerPage={this.state.postsPerPage} totalpost={this.state.quiz.length} paginate={this.paginate}/>
            
      <Button variant="danger">End Quiz</Button>
      </div>
    );
  }
}
export default Quiz;