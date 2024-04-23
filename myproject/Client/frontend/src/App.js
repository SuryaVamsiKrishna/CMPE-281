import React from "react";


import {
  BrowserRouter as Router,
  Routes,
  Route,
} from "react-router-dom";

import AppFooter from "./components/Footer/Footer";
import AppHeader from "./components/Header/Header";
import HomePage from "./pages/HomePage/HomePage";
import Login from "./components/Login/Login";

const App = () => {
 
    return (
      <div style={{ display: 'flex', flexDirection: 'column', minHeight: '100vh' }}>
        <AppHeader />
        <div style={{ flex: 1, marginTop: '10vh' }}> {/* Added marginTop */}
          <Router>
            <Routes>
              <Route path="/" element={<HomePage />} />
              {/* <Route path="/join" element={<RoomJoinPage />} />
              <Route path="/create" element={<CreateRoomPage />} /> */}
              <Route path="/login" element={<Login />} />
            </Routes>
          </Router>
        </div>
        <AppFooter style={{
          flexShrink: 0,
          backgroundColor: '#f1f1f1',
          padding: '20px',
          textAlign: 'center',
        }} />
      </div>
    );
  }

export default App;
