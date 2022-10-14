import React from "react";
import StudentReview from "../StudentReview/StudentReview";
import Grades from "../Updates/Updates";
import "./RightSide.css";

const RightSide = () => {
  return (
    <div className="RightSide">
      
      <div>
        <h3>Grades</h3>
        <StudentReview />
      </div>
    </div>
  );
};

export default RightSide;
