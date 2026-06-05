import { Lock, Mail } from "lucide-react";
import { useState } from "react";
import { Link, useLocation, useNavigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext.jsx";

export default function Login() {
  const [form, setForm] = useState({ email: "", password: "" });
  const [error, setError] = useState("");
  const { login, loading } = useAuth();
  const navigate = useNavigate();
  const location = useLocation();

  const submit = async (event) => {
    event.preventDefault();
    setError("");
    try {
      await login(form);
      navigate(location.state?.from?.pathname || "/profile", { replace: true });
    } catch (err) {
      setError(err.response?.data?.message || "Login failed");
    }
  };

  return (
    <section className="page-shell grid min-h-[72vh] place-items-center py-12">
      <form onSubmit={submit} className="w-full max-w-md rounded-lg border border-teal-100 bg-white p-7 shadow-soft">
        <h1 className="text-2xl font-extrabold">Welcome back</h1>
        <p className="muted mt-2">All Tourism Assistant: Your Complete AI-Powered Travel and Tourism Companion.</p>
        {error && <p className="mt-4 rounded-lg bg-red-50 p-3 text-sm font-semibold text-red-700">{error}</p>}
        <label className="mt-6 block">
          <span className="mb-1 block text-sm font-semibold">Email</span>
          <div className="relative"><Mail className="absolute left-3 top-3.5 text-slate-400" size={18} /><input className="input pl-10" type="email" required value={form.email} onChange={(e) => setForm({ ...form, email: e.target.value })} /></div>
        </label>
        <label className="mt-4 block">
          <span className="mb-1 block text-sm font-semibold">Password</span>
          <div className="relative"><Lock className="absolute left-3 top-3.5 text-slate-400" size={18} /><input className="input pl-10" type="password" required value={form.password} onChange={(e) => setForm({ ...form, password: e.target.value })} /></div>
        </label>
        <button className="btn-primary mt-6 w-full" disabled={loading}>{loading ? "Signing in..." : "Sign in"}</button>
        <p className="mt-4 text-center text-sm text-slate-600">New here? <Link className="font-bold text-reef" to="/signup">Create an account</Link></p>
      </form>
    </section>
  );
}
