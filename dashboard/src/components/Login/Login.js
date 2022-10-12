import React, { useState } from "react";
import './login.css';

function Login () {
    const[email, setEmail]=useState("")
    const[password, setPassword]=useState("")
    const[confirmPass, setConfirmPass]=useState("")

    function handleSubmit(){
        const data ={
            email: email,
            password: password,
            confirmPass : confirmPass,

        }
        console.log(data);

        alert(data);


    }


    return (
        <div className="bg">
            <div className="sub-bg">
                <div className="sign-header">

                    <h2>Login to Upeo</h2>
                </div>



          <form className="form" onSubmit={handleSubmit}>

          <label for="name">Email</label> <br/>
          <input type="email" required value={email} onChange={e => setEmail(e.target.value)} placeholder="Enter Your Email"/> <br/>


          <label for="name">Password</label> <br/>
          <input type="password" required value={password} onChange={e => setPassword(e.target.value)} placeholder="Enter Password"/> <br/>

          <label for="name">Confirm Password</label> <br/>
          <input type="password" required value={confirmPass} onChange={e => setConfirmPass(e.target.value)} placeholder="Confirm Password"/> <br/>


          <button className="btn" type="submit" >Login</button>

         


          </form>
          <p>Dont have an account? 
            <a href="/">Login</a>
          </p>
          {/* <button className="btn">Cancel</button> */}
          
          {/* <img className="Upeo" src= {upeoo}/> */}
            </div>
            
            </div>


  

    
    )
}
export default Login;