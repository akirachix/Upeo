import React, { useState } from "react";
import './signup.css';
import upeo from '../Images/upeo.png'

function Signup () {
    const[firstName, setName]=useState("")
    const[lastName, setLastName]=useState("")
    const[email, setEmail]=useState("")
    const[password, setPassword]=useState("")
    const[confirmPass, setConfirmPass]=useState("")

    function handleSubmit(){


        const data ={
            firstName: firstName,
            lastName: lastName,
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

         <div className="form-bg">
         <form className="form" onSubmit={handleSubmit}>
             <div className="img">
             <img src={upeo} alt='Images/upeo.png'/>

             </div>
          <div className="sign-header">
          <h2>Sign Up to Upeo</h2>

             </div>

             <div className="upeo">

          <input type="text" required value={firstName} onChange={e => setName(e.target.value)} placeholder="Enter First Name"/> <br/>

          <input type="text" required value={lastName} onChange={e => setLastName(e.target.value)} placeholder="Enter Last Name"/> <br/>


          <input type="email" required value={email} onChange={e => setEmail(e.target.value)} placeholder="Enter Your Email"/> <br/>


          <input type="password" required value={password} onChange={e => setPassword(e.target.value)} placeholder="Enter Password"/> <br/>

          <input type="password" required value={confirmPass} onChange={e => setConfirmPass(e.target.value)} placeholder="Confirm Password"/> <br/>


          <button className="btn" type="submit" >Continue</button>
          <p>Already have account?
           <a href="/">Login</a>
          </p>

         
             </div>



          </form>
         </div>
         
          
          {/* <button className="btn">Cancel</button> */}
          
          {/* <img className="Upeo" src= {upeoo}/> */}
            </div>
            
            </div>


  

    
    )
}
export default Signup;