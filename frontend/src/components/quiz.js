import React,{Component} from 'react';
//import Quizdata from './questionbank.json';
import 'bootstrap/dist/css/bootstrap.css';
import axios from 'axios';
class Quiz extends Component{
  constructor(props) {
    super(props);
    this.state = {
      quiz:[],
    }
  }
  componentDidMount(){
    axios.get('http://127.0.0.1:8000/api/question/')
    .then(response => {
      this.setState({quiz:response.data})
      console.log(response);
    })
    .catch(error => {
      console.log(error);
    })
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
    //const {quiz}=this.stste
    return(
      <div className="App">
        <h1><badge class="badge badge-success m-6"> Quiz question(s)</badge></h1>  
        

          {this.state.quiz.map((item, questionNumber) =>             
              (<div key={questionNumber} id="Questions"> 
                  <div><span>{questionNumber+1}) </span> {item.text}</div>
                  <div>
                    {item.options.map((items,index )=> {
                      return (
                        <div key={index}> 
                          <div>
                          <h6>                  
                            <input id="radioBtn" 
                            type='radio' value={items} onClick={this.selectOption(questionNumber,items)} 
                             />
                             {items.text}
                          </h6>
                          </div>
                        </div>
                      )
                    })}
                    
                  </div>
                  <hr />     
              </div>)
        )};

        
      </div>
    );
  }
}
export default Quiz;