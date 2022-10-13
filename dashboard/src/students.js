import React from "react";
import logo from "./upeologo.png";
import students from "./stude.png";
import lines from "./lines.png";
import './students.css'


function Main(){
    return(
 
 <div className="container">
  <div className="inner-container">
  <div className='logo'>
   <img src={logo} alt='./upeologo.png' width={140}/>
   </div>
<div className="topnav">
<a href="#Dashboard">Dashboard</a>
<div className='lines'>
   <img src={lines} alt='./lines.png' width={40}/>
   </div>
 <a href="#Students">Students</a>
 <div className='students'>
   <img src={students} alt='./stude.png' width={40}/>
   </div>

 <a href="#Questions">Questions</a>
 <a href="#answers">Answers</a>
 <a href="#Grade">Grading</a>

   <div className='txt-fld'>
    {<label className="form-label">
  <input type="admission" name="admission" placeholder="                                                    Manage Students" />
  <p>Search Students</p>
  <input type="admission" name="admission" placeholder="Admission                                                                                                                          Password" />
  <input type="admission" name="admission" placeholder="22234                                                                                                                              hgety378" />
  <input type="admission" name="admission" placeholder="22235                                                                                                                              wbhgenty37" />
  <input type="admission" name="admission" placeholder="22236                                                                                                                              whgetyx37" />
  <input type="admission" name="admission" placeholder="22237                                                                                                                              whgetvy37" />
  <input type="admission" name="admission" placeholder="22238                                                                                                                              whgetyy37" />

</label> }
</div>


</div>
 </div>

</div>

    );
}
export default Main