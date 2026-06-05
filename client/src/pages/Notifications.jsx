import { BellRing } from "lucide-react";
import useFetch from "../hooks/useFetch.js";

export default function Notifications() {
  const { data } = useFetch("/notifications", { notifications: [] });
  return (
    <section className="page-shell py-10">
      <h1 className="section-title">Travel Notifications</h1>
      <p className="muted mt-2">Travel alerts, recommendation notifications, booking reminders, and safety notifications.</p>
      <div className="mt-7 grid gap-4">
        {data.notifications.map((item) => (
          <article key={item.id} className="flex gap-4 rounded-lg border border-teal-100 bg-white p-5 shadow-sm">
            <BellRing className="mt-1 text-reef" />
            <div>
              <p className="text-xs font-bold uppercase tracking-wider text-slate-500">{item.type}</p>
              <h2 className="mt-1 font-bold">{item.title}</h2>
              <p className="mt-1 text-sm leading-6 text-slate-600">{item.message}</p>
            </div>
          </article>
        ))}
      </div>
    </section>
  );
}

