import React, { useState } from "react";
import upeo from '../Images/upeo.png'
import './login.css';
import axios from 'axios'

function Login () {                         
  const[email, setEmail]=useState("")
  const[password, setPassword]=useState("")
  
  
  const Login = {
    email:"",
    password:""
  }
  const postuser = () =>{
    Login.email=email
    Login.password=password


    console.log(Login)
    axios.post("http://127.0.0.1:8000/api/Login/",Login)
    .then(res =>{
          console.log(res);
        }).catch (error =>{
              console.log(error)
        })
        
  }
    return (
        <div className="bg">
            <div className="sub-bg">
          <form className="forms">
          <div className="image">
             <img src={upeo} alt='Images/upeo.png'/>
             </div>
          <div className="sign-header">
  
           <h3>Manage all students</h3>
           </div>
          <input type="email" required value={email} onChange={e => setEmail(e.target.value)} placeholder="Enter Your Email"/> <br/>
  
          <input type="password" required value={password} onChange={e => setPassword(e.target.value)} placeholder="Enter Password"/> <br/>
  
          <button className="buttonn" type="button" onClick={postuser}>Login</button>
          <p>Dont have an account?
            <a href="/signup">Signup up here</a>
          </p>
  
          </form>
            </div>
           
            </div>
   
    )
 }
 export default Login;