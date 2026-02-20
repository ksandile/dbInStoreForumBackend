import React, { useState } from "react";
import { useNavigate, Link } from "react-router-dom";
import axios from "../api/axios";
import "../styles/Login.css";

const Login = ({ setUser }) => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const res = await axios.post("/login/", { email, password });
  
      localStorage.setItem("user", JSON.stringify(res.data));
  
      setUser(res.data);
      navigate("/"); 
    } catch (err) {
      console.error(err);
      alert("Invalid email or password");
    }
  };

  return (
    <div className="login-page">
      <h2>Login</h2>
      <form onSubmit={handleSubmit}>
        <input 
          type="email" 
          placeholder="Email" 
          value={email} 
          onChange={(e) => setEmail(e.target.value)} 
          required 
        />
        <input 
          type="password" 
          placeholder="Password" 
          value={password} 
          onChange={(e) => setPassword(e.target.value)} 
          required 
        />
        <button type="submit">Login</button>
      </form>

      <p>
        Don't have an account?{" "}
        <Link to="/register" style={{ color: "blue", textDecoration: "underline" }}>
          Register here
        </Link>
      </p>
    </div>
  );
};

export default Login;
