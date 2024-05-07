// import React from "react";
// import { useLocation } from "react-router-dom";

// const Dashboard = () => {
//   const location = useLocation();
//   const username = location.state?.username || 'Guest';

//   return (
//     <div>
//       <h1>Welcome, {username}</h1>
//     </div>
//   );
// };

// export default Dashboard;


import React from "react";
import { Link, useLocation } from "react-router-dom";
import { useNavigate } from "react-router-dom";


const Dashboard = () => {
  const location = useLocation();
  const username = location.state?.username || 'Guest';
  const navigate = useNavigate();

  const handleClick = () => {
    navigate("/view-profile", { state: { username: username } });
  };

  return (
    <div>
      <h1>Welcome, {username}</h1>
      <button onClick={handleClick}>View Profile</button>
    </div>
  );

  // return (
  //   <div>
  //     <h1>Welcome, {username}</h1>
  //     <Link to={{
  //       pathname: "/view-profile",
  //       state: { username: username }
  //     }}>
  //       <button>View Profile</button>
  //     </Link>
  //   </div>
  // );
};

export default Dashboard;
