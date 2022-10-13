import React from "react";
import logo from "./logoupeo.png";
import students from "./stude-removebg-preview.png";
import lines from "./lines-removebg-preview.png";
import questions from "./query-removebg-preview.png";
import answers from "./answrs-removebg-preview.png";
import grading from "./grade-removebg-preview.png";
import './grading.css'


function Main(){
  <div className="cards">
  <h1>Admission</h1>
  <h1>Password</h1>
  <h1>Grade</h1>

</div>

    return(
      
      
 
 <div className="container">
  <div className="inner-container">
  <div className='logo'>
   <img src={logo} alt='./logoupeo.png' width={140}/>
   </div>
<div className="topnav">
<a href="#Dashboard">Dashboard</a>
<div className='lines'>
   <img src={lines} alt='./lines-removebg-preview.png' width={70}/>
</div>
 <a href="#Students">Students</a>
 <div className='students'>
   <img src={students} alt='./stude-removebg-preview.png' width={50}/>
   </div>

 <a href="#Questions">Questions</a>
 <div className="questions">
   <img src={questions} alt='./query-removebg-preview.png' width={50}/>
 </div>

 <a href="#answers">Answers</a>
  <div className="answers">
  <img src={answers} alt='./answrs-removebg-preview.png' width={50}/>
  </div>
 <a href="#Grade">Grading</a>
  <div className="grading">
    <img src={grading} alt='./grade-removebg-preview.png' width={50}/>

  </div>

 


   <div className='txt-fld'>
    {<label className="form-label">
  <input type="admission" name="admission" placeholder="                                                    Grade Students" />
  <p>Search Students</p>
  <input type="admission" name="admission" placeholder="Admission                         Password                                                            Grade" />


  <input type="admission" name="admission" placeholder="22234                             hgety378                            Congratulations for revising with Quicksoma.</br>To continue revising,</br> press 0 to go back to revision questions"/>                                           

  <input type="admission" name="admission" placeholder="22235                                                                                             wbhgenty37" />
  <input type="admission" name="admission" placeholder="22236                                                                                             whgetyx37" />
  <input type="admission" name="admission" placeholder="22237                                                                                             whgetvy37" />
  <input type="admission" name="admission" placeholder="22238                                                                                             whgetyy37" />

</label> }
</div>



</div>
 </div>


</div>

    );
}
export default Main