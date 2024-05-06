import React, { useState, useEffect } from "react";

const ViewProfile = ({ location }) => {
  const [userDetails, setUserDetails] = useState(null);
  const username = location.state.username;

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
        </div>
      )}
    </div>
  );
};

export default ViewProfile;
