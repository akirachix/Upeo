import './grading.css';


const data = [
  { Admission:  "256789",   Password:"r2455",  Grade :" Congratulations for revising with Quicksoma"},
  { Admission:  "6789",     Password:"yt455" ,   Grade :" Congratulations for revising with Quicksoma"},
  { Admission:  "25689",    Password:"we455",   Grade :" Congratulations for revising with Quicksoma"},
  { Admission:  "6789",     Password:"qw55" ,    Grade :" Congratulations for revising with Quicksoma"},
  { Admission:  "2589",     Password:"un455",    Grade :" Congratulations for revising with Quicksoma"},
  { Admission:  "2789",     Password:"cvs455",   Grade :" Congratulations for revising with Quicksoma"},
  { Admission:  "2567",     Password:"0pn55",    Grade :" Congratulations for revising with Quicksoma"},
  { Admission:  "256y",     Password:"vd55",     Grade :" Congratulations for revising with Quicksoma"},
  { Admission:  "rt789",    Password:"89455",   Grade :" Congratulations for revising with Quicksoma"},
  { Admission:  "we789",    Password:"0on455",  Grade :" Congratulations for revising with Quicksoma"},
  { Admission:  "259u89",   Password:"12455",  Grade :" Congratulations for revising with Quicksoma"},
  { Admission:  "256419",   Password:"9q455",  Grade :" Congratulations for revising with Quicksoma"},
  { Admission:  "251289",   Password:"17455",  Grade :" Congratulations for revising with Quicksoma"},
]
  
function Grade() {
  return (
    
<div className="App">
 <table id="Upeo">
  <div className='btn'>
    <button>Total Students</button>

  </div>
         <tr>
        <th>Admission</th>
          <th>Password</th>
          <th>Grade</th>
        </tr>
        {data.map((val, key) => {
          return (
            <tr key={key}>
              <td>{val.Admission}</td>
              <td>{val.Password}</td>
              <td>{val.Grade}</td>
             
            </tr>
          )
        })}
       </table>
      
    </div>
    
  );
}
  
export default Grade;