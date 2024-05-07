// import React, { useState, useEffect } from "react";
// import { Link, useLocation } from "react-router-dom";

// const ViewProfile = () => {
//   const [userDetails, setUserDetails] = useState(null);
//   const location = useLocation();
//   const username = location.state?.username || 'Guest';

//   useEffect(() => {
//     const fetchUserDetails = async () => {
//       try {
//         const response = await fetch(`http://127.0.0.1:8000/accounts/get-user-details/${username}/`);
//         if (!response.ok) {
//           throw new Error('Failed to fetch user details');
//         }
//         const data = await response.json();
//         setUserDetails(data);
//       } catch (error) {
//         console.error(error);
//       }
//     };

//     fetchUserDetails();
//   }, [username]);

//   return (
//     <div>
//       {userDetails && (
//         <div>
//           <h2>User Details</h2>
//           <p>Username: {userDetails.user.username}</p>
//           <p>Email: {userDetails.user.email}</p>
//           <p>User Type: {userDetails.user.user_type}</p>
//           {userDetails.license_number && (
//             <div>
//               <p>License Number: {userDetails.license_number}</p>
//               <p>Vehicle Color: {userDetails.vehicle_color}</p>
//               <p>Model Number: {userDetails.model_number}</p>
//               <p>Sensor Info: {userDetails.sensor_info}</p>
//             </div>
//           )}
//         </div>
//       )}
//     </div>
//   );
// };

// export default ViewProfile;


import React, { useState, useEffect } from "react";
import { Link, useLocation, useNavigate } from "react-router-dom";

const ViewProfile = () => {
  const [userDetails, setUserDetails] = useState(null);
  const location = useLocation();
  const username = location.state?.username || 'Guest';
  const navigate = useNavigate();

  useEffect(() => {
    const fetchUserDetails = async () => {
      try {
        const response = await fetch(`http://127.0.0.1:8000/accounts/get-user-details/${username}/`);
        if (!response.ok) {
          throw new Error('Failed to fetch user details');
        }
        const data = await response.json();
        setUserDetails(data);
      } catch (error) {
        console.error(error);
      }
    };

    fetchUserDetails();
  }, [username]);

  const handleEditProfile = () => {
    navigate("/edit-profile", { state: { userDetails: userDetails } });
  };

  return (
    <div>
      {userDetails && (
        <div>
          <h2>User Details</h2>
          <p>Username: {userDetails.user.username}</p>
          <p>Email: {userDetails.user.email}</p>
          <p>User Type: {userDetails.user.user_type}</p>
          {userDetails.license_number && (
            <div>
              <p>License Number: {userDetails.license_number}</p>
              <p>Vehicle Color: {userDetails.vehicle_color}</p>
              <p>Model Number: {userDetails.model_number}</p>
              <p>Sensor Info: {userDetails.sensor_info}</p>
            </div>
          )}
          <button onClick={handleEditProfile}>Edit Profile</button>
        </div>
      )}
    </div>
  );
};

export default ViewProfile;
