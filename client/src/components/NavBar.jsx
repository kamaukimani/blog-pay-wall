import React from "react";
import { Link } from "react-router-dom";


function NavBar({ user, setUser, API_URL }) {
  function handleLogoutClick() {
    fetch(`${API_URL}/logout`, 
      { 
        method: "DELETE",
        credentials: "include",
      }).then((r) => {
      if (r.ok) {
        setUser(null);
      }
    });
  }

  return (
    <header>
      <div>
        <Link to="/">Home</Link>
      </div>
      <p>
        <Link to="/members">Click here for exclusive member-only content!</Link>
      </p>
      <div>
        {user ? (
            <div>
                <p>Welcome, {user.username}!</p>
                <button onClick={handleLogoutClick}>Logout</button>
            </div>
          
        ) : (
          <>
            <Link to="/signup">Signup</Link>
            <br/>
            <Link to="/login">Login</Link>
          </>
        )}
      </div>
    </header>
  );
}

export default NavBar;