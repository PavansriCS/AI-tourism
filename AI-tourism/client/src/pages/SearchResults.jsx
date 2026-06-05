import { useSearchParams } from "react-router-dom";
import ListingCard from "../components/ListingCard.jsx";
import SearchPanel from "../components/SearchPanel.jsx";
import api from "../services/api.js";
import { useEffect, useState } from "react";

export default function SearchResults() {
  const [params] = useSearchParams();
  const [data, setData] = useState({ destinations: [], hotels: [], resorts: [], restaurants: [], attractions: [], waterParks: [], adventureParks: [], recommendations: null });
  const [loading, setLoading] = useState(true);
  const query = params.toString();

  useEffect(() => {
    setLoading(true);
    api.get(`/search?${query}`).then(({ data }) => setData(data)).finally(() => setLoading(false));
  }, [query]);

  return (
    <section className="page-shell py-10">
      <h1 className="section-title">Explore Tourism Options</h1>
      <div className="mt-6"><SearchPanel compact /></div>
      {loading ? <p className="mt-8 rounded-lg bg-white p-6 text-slate-600">Finding premium stays, restaurants, routes, and AI recommendations...</p> : (
        <div className="mt-8 space-y-12">
          {data.recommendations && (
            <div className="rounded-lg border border-teal-100 bg-white p-6 shadow-soft">
              <h2 className="text-xl font-bold">AI Recommendation Engine</h2>
              <div className="mt-4 grid gap-4 md:grid-cols-3">
                {["places", "activities", "budgetTips"].map((key) => (
                  <div key={key} className="rounded-lg bg-teal-50 p-4">
                    <h3 className="font-bold capitalize">{key.replace(/([A-Z])/g, " $1")}</h3>
                    <ul className="mt-3 space-y-2 text-sm text-slate-700">
                      {(data.recommendations[key] || []).map((item) => <li key={item}>{item}</li>)}
                    </ul>
                  </div>
                ))}
              </div>
            </div>
          )}
          <ResultBlock title="Destinations" items={data.destinations} type="destination" />
          <TieredResultBlock title="Hotel Bookings" items={data.hotels} />
          <TieredResultBlock title="Resort Bookings" items={data.resorts} />
          <ResultBlock title="Water Theme Parks" items={data.waterParks} />
          <ResultBlock title="Adventure Parks" items={data.adventureParks} />
          <TieredResultBlock title="Tourist Attraction Bookings" items={data.attractions} />
          <TieredResultBlock title="Restaurant Bookings" items={data.restaurants} type="restaurant" />
        </div>
      )}
    </section>
  );
}

const tierOrder = [
  ["Budget", "Budget Friendly Options"],
  ["Standard", "Standard Options"],
  ["High-Class", "High-Class Options"]
];

function TieredResultBlock({ title, items, type }) {
  if (!items.length) return <ResultBlock title={title} items={items} type={type} />;

  return (
    <div>
      <h2 className="text-2xl font-bold">{title}</h2>
      <div className="mt-5 space-y-8">
        {tierOrder.map(([tier, label]) => {
          const tierItems = items.filter((item) => (item.bookingTier || "Standard") === tier);
          if (!tierItems.length) return null;
          return (
            <section key={tier}>
              <div className="flex flex-wrap items-center justify-between gap-3">
                <h3 className="text-lg font-bold text-ink">{label}</h3>
                <span className="rounded-lg bg-teal-50 px-3 py-2 text-sm font-semibold text-reef">{tierItems.length} booking links</span>
              </div>
              <div className="mt-4 grid gap-5 sm:grid-cols-2 lg:grid-cols-3">
                {tierItems.map((item) => <ListingCard key={item.id || item.slug} item={item} type={type} />)}
              </div>
            </section>
          );
        })}
      </div>
    </div>
  );
}

function ResultBlock({ title, items, type }) {
  return (
    <div>
      <h2 className="text-2xl font-bold">{title}</h2>
      <div className="mt-5 grid gap-5 sm:grid-cols-2 lg:grid-cols-3">
        {items.map((item) => <ListingCard key={item.id || item.slug} item={item} type={type} />)}
      </div>
    </div>
  );
}
