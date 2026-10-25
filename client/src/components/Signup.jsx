
import React, { useState } from "react";

function SignUp({ setUser, API_URL }) {
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [passwordConfirmation, setPasswordConfirmation] = useState("");
  const [error, setError] = useState("");

  const isMatch =
    password.length > 0 &&
    password === passwordConfirmation;

  function handleSubmit(e) {
    e.preventDefault();

    if (!isMatch) {
      setError("Passwords do not match!");
      return;
    }

    setError("");

    fetch(`${API_URL}/signup`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        username,
        email,
        password,
        password_confirmation: passwordConfirmation,
      }),
    })
      .then((r) => {
        if (!r.ok) {
          throw new Error("Sign up failed.");
        }
        return r.json();
      })
      .then((user) => setUser(user))
      .catch((err) => setError(err.message));
  }

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <h1>Sign Up</h1>

        <label htmlFor="username">Username</label>
        <input
          type="text"
          id="username"
          autoComplete="username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          required
        />

        <label htmlFor="email">Email</label>
        <input
          type="email"
          id="email"
          autoComplete="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
        />

        <label htmlFor="password">Password</label>
        <input
          type="password"
          id="password"
          autoComplete="new-password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        />

        <label htmlFor="password_confirmation">
          Password Confirmation
        </label>
        <input
          type="password"
          id="password_confirmation"
          autoComplete="new-password"
          value={passwordConfirmation}
          onChange={(e) =>
            setPasswordConfirmation(e.target.value)
          }
          required
        />

        {passwordConfirmation.length > 0 && !isMatch && (
          <p>Passwords do not match!</p>
        )}

        {error && <p role="alert">{error}</p>}

        <button type="submit" disabled={!isMatch}>
          Sign Up
        </button>
      </form>
    </div>
  );
}

export default SignUp;
