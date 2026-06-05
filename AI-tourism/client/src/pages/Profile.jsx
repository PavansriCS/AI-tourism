import { CalendarDays, LogOut, Mail, MapPin } from "lucide-react";
import { useAuth } from "../context/AuthContext.jsx";
import useFetch from "../hooks/useFetch.js";

export default function Profile() {
  const { user, logout } = useAuth();
  const { data } = useFetch("/trips", { trips: [] });

  return (
    <section className="page-shell py-10">
      <div className="rounded-lg border border-teal-100 bg-white p-7 shadow-soft">
        <div className="flex flex-col justify-between gap-5 sm:flex-row sm:items-center">
          <div>
            <h1 className="text-3xl font-extrabold">{user?.name}</h1>
            <p className="mt-2 flex items-center gap-2 text-slate-600"><Mail size={18} /> {user?.email}</p>
            <p className="mt-1 flex items-center gap-2 text-slate-600"><MapPin size={18} /> {user?.homeCity || "Home city not set"}</p>
          </div>
          <button onClick={logout} className="btn-secondary"><LogOut size={18} /> Log out</button>
        </div>
      </div>
      <div className="mt-8">
        <h2 className="section-title">Saved AI Trips</h2>
        <div className="mt-5 grid gap-4">
          {data.trips.length === 0 && <p className="rounded-lg border border-dashed border-teal-200 bg-white p-6 text-slate-600">No saved trips yet. Generate one in the smart planner.</p>}
          {data.trips.map((trip) => (
            <article key={trip.id} className="rounded-lg border border-teal-100 bg-white p-5">
              <h3 className="font-bold">{trip.destination}</h3>
              <p className="mt-2 flex items-center gap-2 text-sm text-slate-600"><CalendarDays size={16} /> {trip.days} days, estimated budget Rs. {trip.estimatedBudget}</p>
            </article>
          ))}
        </div>
      </div>
    </section>
  );
}

