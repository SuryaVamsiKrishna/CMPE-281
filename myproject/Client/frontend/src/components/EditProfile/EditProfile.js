import React, { useState } from "react";
import { Link, useLocation, useNavigate } from "react-router-dom";


const EditProfile = () => {
  const location = useLocation();
  const { userDetails } = location.state;
  const [formData, setFormData] = useState({
    email: userDetails.user.email,
    password: userDetails.user.password,
    license_number: userDetails.license_number || "",
    vehicle_color: userDetails.vehicle_color || "",
    model_number: userDetails.model_number || "",
    sensor_info: userDetails.sensor_info || "",
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prevData) => ({
      ...prevData,
      [name]: value,
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    const updatedUserDetails = {
      user: {
        ...userDetails.user,
        email: formData.email,
        password: formData.password,
      },
      ...(userDetails.user.user_type === "driver"
        ? {
            license_number: formData.license_number,
            vehicle_color: formData.vehicle_color,
            model_number: formData.model_number,
            sensor_info: formData.sensor_info,
          }
        : {}),
    };
    console.log(updatedUserDetails);
    // You can perform further actions like sending updatedUserDetails to the server here
  };

  return (
    <div>
      <h2>Edit Profile</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Email:</label>
          <input
            type="email"
            name="email"
            value={formData.email}
            onChange={handleChange}
            required
          />
        </div>
        <div>
          <label>Password:</label>
          <input
            type="password"
            name="password"
            value={formData.password}
            onChange={handleChange}
            required
          />
        </div>
        {userDetails.user.user_type === "driver" && (
          <>
            <div>
              <label>License Number:</label>
              <input
                type="text"
                name="license_number"
                value={formData.license_number}
                onChange={handleChange}
              />
            </div>
            <div>
              <label>Vehicle Color:</label>
              <input
                type="text"
                name="vehicle_color"
                value={formData.vehicle_color}
                onChange={handleChange}
              />
            </div>
            <div>
              <label>Model Number:</label>
              <input
                type="text"
                name="model_number"
                value={formData.model_number}
                onChange={handleChange}
              />
            </div>
            <div>
              <label>Sensor Info:</label>
              <input
                type="text"
                name="sensor_info"
                value={formData.sensor_info}
                onChange={handleChange}
              />
            </div>
          </>
        )}
        <button type="submit">Submit</button>
      </form>
    </div>
  );
};

export default EditProfile;
