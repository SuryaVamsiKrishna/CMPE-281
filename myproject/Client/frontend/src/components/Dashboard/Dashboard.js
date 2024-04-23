import React from "react";
import { useLocation } from "react-router-dom";

const Dashboard = () => {
  const location = useLocation();
  const username = location.state?.username || 'Guest';

  return (
    <div>
      <h1>Welcome, {username}</h1>
    </div>
  );
};

export default Dashboard;
