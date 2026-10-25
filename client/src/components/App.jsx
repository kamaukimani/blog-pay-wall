import { useState, useEffect } from "react";
import { Routes, Route } from "react-router-dom";
import Article from "./Article";
import NavBar from "./NavBar"
import Home from "./Home";
import Login from "./Login";
import MemberArticles from "./MemberArticle";
import SignUp from "./Signup"

function App() {
  const [user, setUser] = useState(null);

  const API_URL="http://127.0.0.1:5555"

  useEffect(() => {
    fetch(`${API_URL}/check_session`,{
      credentials: "include",
    }).then((response) => {
      if (response.ok) {
        response.json().then((user) => setUser(user));
      }
    });
  }, []);



  return (
    <div className="App">
      <NavBar user={user} setUser={setUser} API_URL={API_URL}/>
      <main>
        {user ? (
            <Routes>
              <Route 
                path="/"
                element={<Home API_URL={API_URL} user={user}/>}
              />
            </Routes>
          ):(
            <Routes>
                <Route 
                  path="/signup"
                  element={<SignUp setUser={setUser} API_URL={API_URL}/>}
                />
                <Route 
                  path="/articles/:id"
                  element={<Article API_URL={API_URL}/>}
                />
                <Route 
                  path="/login"
                  element={<Login setUser={setUser} />}
                />
                <Route
                  path="/members"
                  element={<MemberArticles API_URL={API_URL}/>}
                />
                <Route
                  path="/"
                  element={<Home API_URL={API_URL}/>}
                />
          
              </Routes>
          )
        }
      </main>
     
    </div>
  );
}

export default App;