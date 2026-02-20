import React from "react";
import "../styles/Header.css";
import logo from "../assets/logo.png";
import { useNavigate, Link } from "react-router-dom";

const Header = ({ user, setUser }) => {
  const navigate = useNavigate();
  const handleLogout = () => {
    setUser(null);
    navigate("/login");
  }
  return (
    <header className="header">
      <div className="header-left">
        <img src={logo} alt="StoreMedia Hub Logo" className="logo" />
      </div>

      <nav className="header-nav">
        {user ? (
          <>
            <Link to="/" className="nav-link">Dashboard</Link>
            <Link to="/posts" className="nav-link">Posts</Link>
            <span className="greeting">
              Welcome, {user.name} ({user.role})
            </span>
            <button className="logout-btn" onClick={handleLogout}>
              Logout
            </button>
          </>
        ) : (
          <>
            <Link to="/login" className="nav-link">Login</Link>
            <Link to="/register" className="nav-link">Register</Link>
          </>
        )}
      </nav>
    </header>
  );
};

export default Header;
