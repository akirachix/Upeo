// import logo from './logo.svg';
import './App.css';
import{BrowserRouter as Router,Route, Routes } from 'react-router-dom';
import Login from './components/Login/Login';
import Signup from './components/SignUp/Signupform';
// import Main from './components/students/students';
import Dash from './components/Admin/Admin';
import Answer from './components/Answers/Answers';
// import Signup from './components/SignUp/Signupform';
function App() {
  return (
    <div className="App">
        {/* <Signup/> */}
        <Router>
          <Routes>
          <Route exact path="/" element= {<Login/>}/>
            <Route exact path="/Signup" element = {<Signup/>}/>
            {/* <Route exact path="/" element= {<Login/>}/> */}
            <Route exact path="/Dash" element = {<Dash/>}/>
            <Route exact path="/Answer" element = {<Answer/>}/>

          </Routes>
        </Router>
    </div>
  );
}
export default App;