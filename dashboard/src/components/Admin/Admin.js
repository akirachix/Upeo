import React from "react";
import './Admin.css'


function Dash() {

  return (
    <div className="all">
      <h3 className="header">Upeo Team</h3>

      <table className="Tables">
        <tr className="widgetLgTr">
          <th className="widgetLgTh">Number</th>
          <th className="widgetLgTh">Full Names</th>
          <th className="widgetLgTh">Emails</th>
          <th className="widgetLgTh">Access level</th>
        </tr>

        <tr className="widgetLgTr">
           <td className="widgetLgUser">
            <span className="widgetLgNumber">1</span>
            </td>
            <td className="widgetLgName">Faith Mutua</td>
            <td className="widgetLgName">faithmutua@gmail.com</td>
            <td className="widgetLgName">Admin</td>
        </tr>
        <tr className="widgetLgTr">
          <td className="widgetLgUser">
            <span className="widgetLgNumber">2</span>
          </td>
          <td className="widgetLgName">Esther Nalenyi</td>
          <td className="widgetLgName">esthernalenyi@gmail.com</td>
          <td className="widgetLgName">Admin</td>
        </tr>
        <tr className="widgetLgTr">
          <td className="widgetLgUser">
            <span className="widgetLgNumber">3</span>
          </td>
          <td className="widgetLgName">Mercy Jepchirchir</td>
          <td className="widgetLgName">mjepchirchir@gmail.com</td>
          <td className="widgetLgName">Admin</td>
        </tr>
        <tr className="widgetLgTr">
          <td className="widgetLgUser">
            <span className="widgetLgNumber">4</span>
          </td>
          <td className="widgetLgName">Respah Nafula</td>
          <td className="widgetLgName">respahnafula@gmail.com</td>
          <td className="widgetLgName">Admin</td>
        </tr>
        <tr className="widgetLgTr">
          <td className="widgetLgUser">
            <span className="widgetLgNumber">5</span>
          </td>
          <td className="widgetLgName">Juliet Nakayiza</td>
          <td className="widgetLgName">julietnakayiza@gmail.com</td>
          <td className="widgetLgName">Admin</td>
        </tr>
        </table>
    </div>
  );
}
export default Dash;
