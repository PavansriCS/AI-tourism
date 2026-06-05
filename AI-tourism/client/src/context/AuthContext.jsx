import { createContext, useContext, useEffect, useMemo, useState } from "react";
import api from "../services/api.js";

const AuthContext = createContext(null);

export function AuthProvider({ children }) {
  const [user, setUser] = useState(() => {
    const stored = localStorage.getItem("all_tourism_assistant_user");
    return stored ? JSON.parse(stored) : null;
  });
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    const token = localStorage.getItem("all_tourism_assistant_token");
    if (!token) return;
    api.get("/auth/me").then(({ data }) => {
      setUser(data.user);
      localStorage.setItem("all_tourism_assistant_user", JSON.stringify(data.user));
    }).catch(() => {
      localStorage.removeItem("all_tourism_assistant_token");
      localStorage.removeItem("all_tourism_assistant_user");
      setUser(null);
    });
  }, []);

  const login = async (payload) => {
    setLoading(true);
    try {
      const { data } = await api.post("/auth/login", payload);
      localStorage.setItem("all_tourism_assistant_token", data.token);
      localStorage.setItem("all_tourism_assistant_user", JSON.stringify(data.user));
      setUser(data.user);
      return data;
    } finally {
      setLoading(false);
    }
  };

  const signup = async (payload) => {
    setLoading(true);
    try {
      const { data } = await api.post("/auth/signup", payload);
      localStorage.setItem("all_tourism_assistant_token", data.token);
      localStorage.setItem("all_tourism_assistant_user", JSON.stringify(data.user));
      setUser(data.user);
      return data;
    } finally {
      setLoading(false);
    }
  };

  const logout = () => {
    localStorage.removeItem("all_tourism_assistant_token");
    localStorage.removeItem("all_tourism_assistant_user");
    setUser(null);
  };

  const value = useMemo(() => ({ user, loading, login, signup, logout, isAuthenticated: Boolean(user) }), [user, loading]);
  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
}

export function useAuth() {
  return useContext(AuthContext);
}
