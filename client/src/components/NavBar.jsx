import React from "react";
import { Link } from "react-router-dom";


const API_URL="http://127.0.0.1:5555"
function NavBar({ user, setUser }) {
  function handleLogoutClick() {
    fetch(`${API_URL}/logout`, { method: "DELETE" }).then((r) => {
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
            <Link to="/login">Login</Link>
          </>
        )}
      </div>
    </header>
  );
}

export default NavBar;