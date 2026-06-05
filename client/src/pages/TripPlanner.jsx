import { Calendar, IndianRupee, MapPinned, Sparkles } from "lucide-react";
import { useState } from "react";
import api from "../services/api.js";

export default function TripPlanner() {
  const [form, setForm] = useState({ destination: "Goa", budget: "35000", days: "4", interests: "Beaches, food, nightlife" });
  const [plan, setPlan] = useState(null);
  const [loading, setLoading] = useState(false);

  const generate = async (event) => {
    event.preventDefault();
    setLoading(true);
    try {
      const { data } = await api.post("/ai/trip-plan", form);
      setPlan(data.plan);
    } finally {
      setLoading(false);
    }
  };

  return (
    <section className="page-shell py-10">
      <h1 className="section-title">Smart AI Trip Planner</h1>
      <p className="muted mt-2">Generate day-wise schedules with routes, time estimates, budget calculation, nearby attractions, and safety notes.</p>
      <form onSubmit={generate} className="mt-7 grid gap-4 rounded-lg border border-teal-100 bg-white p-4 shadow-soft sm:grid-cols-2 sm:p-5 lg:grid-cols-5">
        <input className="input" value={form.destination} onChange={(e) => setForm({ ...form, destination: e.target.value })} placeholder="Destination" />
        <input className="input" type="number" value={form.budget} onChange={(e) => setForm({ ...form, budget: e.target.value })} placeholder="Budget" />
        <input className="input" type="number" value={form.days} onChange={(e) => setForm({ ...form, days: e.target.value })} placeholder="Days" />
        <input className="input md:col-span-1" value={form.interests} onChange={(e) => setForm({ ...form, interests: e.target.value })} placeholder="Interests" />
        <button className="btn-primary sm:col-span-2 lg:col-span-1" disabled={loading}><Sparkles size={18} /> {loading ? "Planning..." : "Generate"}</button>
      </form>
      {plan && (
        <div className="mt-8 grid gap-5">
          <div className="rounded-lg border border-teal-100 bg-white p-6 shadow-soft">
            <div className="grid gap-4 sm:grid-cols-3">
              <Info icon={MapPinned} label="Destination" value={plan.destination} />
              <Info icon={Calendar} label="Duration" value={`${plan.days} days`} />
              <Info icon={IndianRupee} label="Budget" value={`Rs. ${plan.estimatedBudget}`} />
            </div>
          </div>
          {plan.schedule.map((day) => (
            <article key={day.day} className="rounded-lg border border-teal-100 bg-white p-6">
              <h2 className="text-xl font-bold">Day {day.day}: {day.theme}</h2>
              <div className="mt-4 grid gap-3">
                {day.items.map((item) => (
                  <div key={item.time + item.activity} className="rounded-lg bg-slate-50 p-4">
                    <p className="text-sm font-bold text-reef">{item.time} - {item.duration}</p>
                    <h3 className="mt-1 font-bold">{item.activity}</h3>
                    <p className="mt-1 text-sm text-slate-600">{item.route}</p>
                  </div>
                ))}
              </div>
            </article>
          ))}
        </div>
      )}
    </section>
  );
}

function Info({ icon: Icon, label, value }) {
  return <div className="flex items-center gap-3"><Icon className="text-reef" /><div><p className="text-xs font-bold uppercase tracking-wider text-slate-500">{label}</p><p className="font-bold">{value}</p></div></div>;
}
