import { CloudSun, Hospital, Phone, ShieldCheck } from "lucide-react";
import MapEmbed from "../components/MapEmbed.jsx";
import useFetch from "../hooks/useFetch.js";

export default function Safety() {
  const { data } = useFetch("/safety", { emergency: [], alerts: [], safeAreas: [] });
  return (
    <section className="page-shell py-10">
      <h1 className="section-title">Safety Hub</h1>
      <p className="muted mt-2">Emergency contacts, nearby hospitals, police stations, weather alerts, and safer area recommendations.</p>
      <div className="mt-7 grid gap-6 lg:grid-cols-[1fr_420px]">
        <div className="grid gap-5">
          <Panel title="Emergency Contacts" icon={Phone} items={data.emergency} />
          <Panel title="Weather and Travel Alerts" icon={CloudSun} items={data.alerts} />
          <Panel title="Safe Area Recommendations" icon={ShieldCheck} items={data.safeAreas} />
          <Panel title="Nearby Hospitals and Police" icon={Hospital} items={data.nearbyHelp} />
        </div>
        <MapEmbed query="nearby hospitals and police stations" className="sticky top-24 h-[620px]" />
      </div>
    </section>
  );
}

function Panel({ title, icon: Icon, items = [] }) {
  return (
    <div className="rounded-lg border border-teal-100 bg-white p-6 shadow-sm">
      <h2 className="flex items-center gap-2 text-xl font-bold"><Icon className="text-reef" /> {title}</h2>
      <div className="mt-4 grid gap-3">
        {items.map((item) => <div key={item.title || item.name} className="rounded-lg bg-slate-50 p-4"><h3 className="font-bold">{item.title || item.name}</h3><p className="mt-1 text-sm leading-6 text-slate-600">{item.description || item.phone || item.address}</p></div>)}
      </div>
    </div>
  );
}

