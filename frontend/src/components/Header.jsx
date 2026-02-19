import React from "react";

const Header = ({ user }) => {
  return (
    <header className="header">
      <h1>StoreMedia Hub</h1>
      {user ? <p>Welcome, {user.name} ({user.role})</p> : <p>Please log in</p>}
    </header>
  );
};

export default Header;
