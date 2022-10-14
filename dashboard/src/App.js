import './App.css'
import MainDash from './components/MainDash/MainDash';
import RightSide from './components/RightSide/RightSide';
import Sidebar from './components/Sidebar';


function App() {
  return (
    <div className="App">
      <div className="AppGlass">
        <MainDash/>
        {/* <Sidebar/> */}
        <RightSide/>
       
      </div>
    </div>
  );
}
 
export default App;
