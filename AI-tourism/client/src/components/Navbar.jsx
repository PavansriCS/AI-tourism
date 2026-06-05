import { Bell, Bot, LogOut, Menu, ShieldCheck, UserRound, X } from "lucide-react";
import { useState } from "react";
import { Link, NavLink } from "react-router-dom";
import { useAuth } from "../context/AuthContext.jsx";
import InstallButton from "./InstallButton.jsx";

const links = [
  ["Explore", "/search"],
  ["Hotels", "/hotels"],
  ["Resorts", "/resorts"],
  ["Attractions", "/attractions"],
  ["Water Parks", "/water-parks"],
  ["Adventure", "/adventure-parks"],
  ["Restaurants", "/restaurants"],
  ["Planner", "/planner"],
  ["Safety", "/safety"]
];

export default function Navbar() {
  const [open, setOpen] = useState(false);
  const { user, logout } = useAuth();

  return (
    <header className="sticky top-0 z-40 border-b border-white/70 bg-white/90 backdrop-blur-xl">
      <nav className="page-shell flex h-16 items-center justify-between">
        <Link to="/" className="flex min-w-0 items-center gap-2 font-extrabold text-reef">
          <span className="grid h-10 w-10 shrink-0 place-items-center rounded-lg bg-reef text-white">T</span>
          <span className="truncate">All Tourism Assistant</span>
        </Link>
        <div className="hidden items-center gap-5 xl:flex">
          {links.map(([label, path]) => (
            <NavLink key={path} to={path} className={({ isActive }) => `text-sm font-semibold ${isActive ? "text-reef" : "text-slate-600 hover:text-reef"}`}>
              {label}
            </NavLink>
          ))}
        </div>
        <div className="hidden items-center gap-2 xl:flex">
          <InstallButton className="px-3 py-2" />
          <Link to="/chatbot" className="btn-secondary px-3 py-2" title="AI assistant"><Bot size={18} /></Link>
          <Link to="/notifications" className="btn-secondary px-3 py-2" title="Notifications"><Bell size={18} /></Link>
          {user ? (
            <>
              <Link to="/profile" className="btn-secondary px-3 py-2" title="Profile"><UserRound size={18} /></Link>
              <button onClick={logout} className="btn-secondary px-3 py-2" title="Log out"><LogOut size={18} /></button>
            </>
          ) : (
            <Link to="/login" className="btn-primary py-2">Sign in</Link>
          )}
        </div>
        <button className="btn-secondary px-3 py-2 xl:hidden" onClick={() => setOpen((value) => !value)} aria-label="Toggle menu">
          {open ? <X size={20} /> : <Menu size={20} />}
        </button>
      </nav>
      {open && (
        <div className="max-h-[calc(100vh-4rem)] overflow-y-auto border-t border-slate-100 bg-white xl:hidden">
          <div className="page-shell grid gap-3 py-4 sm:grid-cols-2">
            {links.map(([label, path]) => <Link key={path} to={path} onClick={() => setOpen(false)} className="flex min-h-12 items-center rounded-lg px-3 font-semibold text-slate-700 hover:bg-teal-50">{label}</Link>)}
            <Link to="/chatbot" onClick={() => setOpen(false)} className="flex min-h-12 items-center gap-2 rounded-lg px-3 font-semibold text-slate-700 hover:bg-teal-50"><Bot size={18} /> AI Assistant</Link>
            <Link to="/notifications" onClick={() => setOpen(false)} className="flex min-h-12 items-center gap-2 rounded-lg px-3 font-semibold text-slate-700 hover:bg-teal-50"><Bell size={18} /> Notifications</Link>
            <Link to="/safety" onClick={() => setOpen(false)} className="flex min-h-12 items-center gap-2 rounded-lg px-3 font-semibold text-slate-700 hover:bg-teal-50"><ShieldCheck size={18} /> Safety Hub</Link>
            <InstallButton className="w-full sm:col-span-2" />
            {user ? <button onClick={logout} className="btn-secondary sm:col-span-2">Log out</button> : <Link to="/login" className="btn-primary sm:col-span-2">Sign in</Link>}
          </div>
        </div>
      )}
    </header>
  );
}
