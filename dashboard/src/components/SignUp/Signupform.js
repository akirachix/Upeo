import React, { useState } from "react";
import './signup.css';
import upeo from '../Images/upeo.png'
import axios from "axios";


function Signup () {
    const[first_name,setName]=useState("")
    const[last_name,setLastName]=useState("")
    const[email, setEmail]=useState("")
    const[password,setPassword]=useState("")
    const[confirm_password,setConfirmPassword]=useState("")

    const signup = {
      first_name:"",
      last_name:"",
      email:"",
      password:"",
      confirm_password:"",
    }
    const postusersignup = () =>{
      signup.first_name=first_name
      signup.last_name=last_name
      signup.email= email
      signup.password = password
      signup.confirm_password = confirm_password
  
  
      console.log(signup)
      axios.post("http://127.0.0.1:8000/api/Signup/",signup)
      .then(res =>{
            console.log(res);
          }).catch (error =>{
                console.log(error)
          })
          
    }


    return (
        <div className="bg">
            <div className="sub-bg">

         <div className="form-bg">
         <form className="form">
             <div className="img">
             <img src={upeo} alt='Images/upeo.png'/>

             </div>
          <div className="sign-header">
          <h2>Sign Up to Upeo</h2>

             </div>

             <div className="upeo">
          <input type="text" required value={first_name} onChange={e => setName(e.target.value)} placeholder="Enter First Name"/> <br/>

          <input type="text" required value={last_name} onChange={e => setLastName(e.target.value)} placeholder="Enter Last Name"/> <br/>

          <input type="email" required value={email} onChange={e => setEmail(e.target.value)} placeholder="Enter Your Email"/> <br/>

          <input type="password" required value={password} onChange={e => setPassword(e.target.value)} placeholder="Enter Password"/> <br/>

          <input type="password" required value={confirm_password} onChange={e => setConfirmPassword(e.target.value)} placeholder="Confirm Password"/> <br/>

          <button className="btn" type="submit" onClick={postusersignup}>Continue</button>
          <p>Already have account?
           <a href="/">Login</a>
          </p>
             </div>
          </form>
         </div>
         
            </div>
            
            </div>


  

    
    )
}
export default Signup;

//imports//