// import logo from './logo.svg';
import './App.css';
import{BrowserRouter as Router,Route, Routes } from 'react-router-dom';
import Login from './components/Login/Login';
import Signup from './components/SignUp/Signupform';
// import Signup from './components/SignUp/Signupform';

function App() {
  return (
    <div className="App">
     
        {/* <Signup/> */}

        <Router>
          <Routes>
          <Route exact path="/" element= {<Login/>}/>
            <Route exact path="/Signup" element = {<Signup/>}/>
            <Route exact path="/" element= {<Login/>}/>
            

          </Routes>
        </Router>
    </div>
  );
}

export default App;
