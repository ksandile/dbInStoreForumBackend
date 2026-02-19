import React, { useState } from "react";
import { BrowserRouter as Router, Routes, Route, Navigate } from "react-router-dom";
import Header from "./components/Header";
import Dashboard from "./pages/Dashboard";
import Login from "./pages/Login";

function App() {
  const [user, setUser] = useState(null);

  return (
    <Router>
      <Header user={user} />
      <Routes>
        <Route 
          path="/login" 
          element={<Login setUser={setUser} />} 
        />
        <Route 
          path="/" 
          element={user ? <Dashboard user={user} /> : <Navigate to="/login" />} 
        />
      </Routes>
    </Router>
  );
}

export default App;
