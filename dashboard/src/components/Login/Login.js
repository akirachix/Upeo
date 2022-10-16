import React, { useState } from "react";
import upeo from '../Images/upeo.png'
import './login.css';
import axios from 'axios'

function Login () {                          
  const[email, setEmail]=useState("")
  const[password, setPassword]=useState("")
  const[confirmPass, setConfirmPass]=useState("")

  const handleSubmit = async (e) => {
    e.preventDefault();
    console.log(email, password, confirmPass);
    try {
      const res = await axios.post("http://127.0.0.1:8000/api/Button", {
        email,
        password,
        confirmPass,
      });
    } catch (error) {
      console.log(error);
    }
  };


    return (
        <div className="bg">
            <div className="sub-bg">
          <form className="forms" onSubmit={handleSubmit}>
          <div className="image">
             <img src={upeo} alt='Images/upeo.png'/>
             </div>
          <div className="sign-header">

           <h3>Manage all students</h3>
           </div>

          <input type="email" required value={email} onChange={e => setEmail(e.target.value)} placeholder="Enter Your Email"/> <br/>


          <input type="password" required value={password} onChange={e => setPassword(e.target.value)} placeholder="Enter Password"/> <br/>

          <input type="password" required value={confirmPass} onChange={e => setConfirmPass(e.target.value)} placeholder="Confirm Password"/> <br/>


          <button className="btn" type="submit" >Login</button>
          <p>Dont have an account? 
            <a href="/signup">Signup up here</a>
          </p>

          </form>
         
          {/* <button className="btn">Cancel</button> */}
          
          {/* <img className="Upeo" src= {upeoo}/> */}
            </div>
            
            </div>


  

    
    )
}
export default Login;