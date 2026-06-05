import { Search, Sparkles } from "lucide-react";
import { useState } from "react";
import { useNavigate } from "react-router-dom";

const interests = ["Beaches", "Hills", "Food", "Culture", "Adventure", "Wellness", "Family"];

export default function SearchPanel({ compact = false }) {
  const navigate = useNavigate();
  const [form, setForm] = useState({ destination: "", budget: "25000", days: "4", interests: "Beaches" });

  const update = (key, value) => setForm((current) => ({ ...current, [key]: value }));
  const submit = (event) => {
    event.preventDefault();
    const params = new URLSearchParams(form);
    navigate(`/search?${params.toString()}`);
  };

  return (
    <form onSubmit={submit} className={`glass grid gap-3 rounded-xl p-3 shadow-soft sm:p-4 ${compact ? "sm:grid-cols-2 lg:grid-cols-5" : "sm:grid-cols-2 lg:grid-cols-[1.4fr_1fr_1fr_1fr_auto]"}`}>
      <label className="block">
        <span className="mb-1 block text-xs font-bold uppercase tracking-wider text-slate-500">Destination</span>
        <input className="input" placeholder="Goa, Ooty, Chennai..." value={form.destination} onChange={(e) => update("destination", e.target.value)} />
      </label>
      <label className="block">
        <span className="mb-1 block text-xs font-bold uppercase tracking-wider text-slate-500">Budget</span>
        <input className="input" type="number" min="1000" value={form.budget} onChange={(e) => update("budget", e.target.value)} />
      </label>
      <label className="block">
        <span className="mb-1 block text-xs font-bold uppercase tracking-wider text-slate-500">Days</span>
        <select className="input" value={form.days} onChange={(e) => update("days", e.target.value)}>
          {[2, 3, 4, 5, 6, 7, 10].map((day) => <option key={day} value={day}>{day} days</option>)}
        </select>
      </label>
      <label className="block">
        <span className="mb-1 block text-xs font-bold uppercase tracking-wider text-slate-500">Interest</span>
        <select className="input" value={form.interests} onChange={(e) => update("interests", e.target.value)}>
          {interests.map((interest) => <option key={interest} value={interest}>{interest}</option>)}
        </select>
      </label>
      <button className="btn-primary w-full self-end sm:col-span-2 lg:col-span-1">
        {compact ? <Search size={18} /> : <Sparkles size={18} />}
        Search
      </button>
    </form>
  );
}
