
import './students.css';

const data = [
  { First_Name: "Faith",     Last_Name: "Mutua",  Admission_Number: "256789",    Password:"r2455"},
  { First_Name: "Mercy",     Last_Name: "Chiri",  Admission_Number: "6789",    Password:"yt455"},
  { First_Name: "Nakayiza",  Last_Name: "Julliet",  Admission_Number: "25689",    Password:"we455"},
  { First_Name: "Esher",     Last_Name: "Nalenyi",  Admission_Number: "6789",    Password:"qw55"},
  { First_Name: "Gumato",    Last_Name: "Robba",  Admission_Number: "2589",    Password:"un455"},
  { First_Name: "Mwende",    Last_Name: "Evelyne",  Admission_Number: "2789",    Password:"cvs455"},
  { First_Name: "Joy",       Last_Name: "Wambui",  Admission_Number: "2567",    Password:"0pn55"},
  { First_Name: "Lorna",     Last_Name: "Mweshny",  Admission_Number: "256y",    Password:"vd55"},
  { First_Name: "Jane",      Last_Name: "Nyambura",  Admission_Number: "rt789",    Password:"89455"},
  { First_Name: "Mary",      Last_Name: "Wangare",  Admission_Number: "we789",    Password:"0on455"},
  { First_Name: "Maria",     Last_Name: "Kimani",  Admission_Number: "259u89",    Password:"12455"},
  { First_Name: "Samuel",    Last_Name: "Mutiso",  Admission_Number: "256419",    Password:"9q455"},
  { First_Name: "Fay",       Last_Name: "Mwash",  Admission_Number: "251289",    Password:"17455"},
]
  
function Main() {
  return (
    
<div className="App">
 <table id="Upeo">
      
         <tr>
        <th>First Name</th>
          <th>Last_Name</th>
          <th>Admission_Number</th>
          <th>Password</th>
         
        </tr>
        {data.map((val, key) => {
          return (
            <tr key={key}>
              <td>{val.First_Name}</td>
              <td>{val.Last_Name}</td>
              <td>{val.Admission_Number}</td>
              <td>{val.Pin}</td>
             
            </tr>
          )
        })}
       </table>
      
    </div>
    
  );
}
  
export default Main;