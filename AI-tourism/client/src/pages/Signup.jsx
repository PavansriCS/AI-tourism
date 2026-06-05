import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext.jsx";

export default function Signup() {
  const [form, setForm] = useState({ name: "", email: "", password: "", homeCity: "" });
  const [error, setError] = useState("");
  const { signup, loading } = useAuth();
  const navigate = useNavigate();

  const submit = async (event) => {
    event.preventDefault();
    setError("");
    try {
      await signup(form);
      navigate("/profile");
    } catch (err) {
      setError(err.response?.data?.message || "Signup failed");
    }
  };

  return (
    <section className="page-shell grid min-h-[72vh] place-items-center py-12">
      <form onSubmit={submit} className="w-full max-w-lg rounded-lg border border-teal-100 bg-white p-7 shadow-soft">
        <h1 className="text-2xl font-extrabold">Create your All Tourism Assistant profile</h1>
        <p className="muted mt-2">Your Complete AI-Powered Travel and Tourism Companion.</p>
        {error && <p className="mt-4 rounded-lg bg-red-50 p-3 text-sm font-semibold text-red-700">{error}</p>}
        <div className="mt-6 grid gap-4 sm:grid-cols-2">
          <label><span className="mb-1 block text-sm font-semibold">Name</span><input className="input" required value={form.name} onChange={(e) => setForm({ ...form, name: e.target.value })} /></label>
          <label><span className="mb-1 block text-sm font-semibold">Home city</span><input className="input" value={form.homeCity} onChange={(e) => setForm({ ...form, homeCity: e.target.value })} /></label>
        </div>
        <label className="mt-4 block"><span className="mb-1 block text-sm font-semibold">Email</span><input className="input" type="email" required value={form.email} onChange={(e) => setForm({ ...form, email: e.target.value })} /></label>
        <label className="mt-4 block"><span className="mb-1 block text-sm font-semibold">Password</span><input className="input" type="password" required minLength="6" value={form.password} onChange={(e) => setForm({ ...form, password: e.target.value })} /></label>
        <button className="btn-primary mt-6 w-full" disabled={loading}>{loading ? "Creating..." : "Create account"}</button>
        <p className="mt-4 text-center text-sm text-slate-600">Already have an account? <Link className="font-bold text-reef" to="/login">Sign in</Link></p>
      </form>
    </section>
  );
}
