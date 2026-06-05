import { useParams } from "react-router-dom";
import ListingCard from "../components/ListingCard.jsx";
import MapEmbed from "../components/MapEmbed.jsx";
import useFetch from "../hooks/useFetch.js";

export default function DestinationDetails() {
  const { slug } = useParams();
  const { data, loading } = useFetch(`/destinations/${slug}`, null);
  if (loading || !data) return <section className="page-shell py-12"><p className="rounded-lg bg-white p-6">Loading destination intelligence...</p></section>;

  const destination = data.destination;
  return (
    <section className="py-10">
      <div className="page-shell">
        <div className="overflow-hidden rounded-lg bg-white shadow-soft">
          <img src={destination.image} alt={destination.name} className="h-64 w-full object-cover sm:h-[360px]" />
          <div className="p-5 sm:p-7">
            <h1 className="text-3xl font-extrabold sm:text-4xl">{destination.name}</h1>
            <p className="mt-3 max-w-3xl leading-7 text-slate-600">{destination.description}</p>
            <div className="mt-5 flex flex-wrap gap-2">
              {destination.interests.map((item) => <span key={item} className="rounded-lg bg-teal-50 px-3 py-2 text-sm font-semibold text-reef">{item}</span>)}
            </div>
          </div>
        </div>
        <div className="mt-8 grid gap-6 lg:grid-cols-[1fr_0.8fr]">
          <div className="rounded-lg border border-teal-100 bg-white p-6">
            <h2 className="text-2xl font-bold">Top Attractions</h2>
            <div className="mt-4 grid gap-3">
              {(data.attractions || []).slice(0, 6).map((item) => <div key={item.id || item.name} className="rounded-lg bg-slate-50 p-4"><h3 className="font-bold">{item.name}</h3><p className="mt-1 text-sm text-slate-600">{item.description}</p></div>)}
            </div>
          </div>
          <MapEmbed query={destination.name} className="min-h-[420px]" />
        </div>
        <TieredBookings title="Recommended Stay Bookings" items={data.hotels} />
        <h2 className="section-title mt-10">Attractions and Activities</h2>
        <TieredBookings items={[...data.attractions, ...data.waterParks, ...data.adventureParks]} />
      </div>
    </section>
  );
}

const tiers = [
  ["Budget", "Budget Friendly Options"],
  ["Standard", "Standard Options"],
  ["High-Class", "High-Class Options"]
];

function TieredBookings({ title, items }) {
  return (
    <div className={title ? "mt-10" : "mt-5"}>
      {title && <h2 className="section-title">{title}</h2>}
      <div className="mt-5 space-y-8">
        {tiers.map(([tier, label]) => {
          const tierItems = items.filter((item) => (item.bookingTier || "Standard") === tier);
          if (!tierItems.length) return null;
          return (
            <section key={tier}>
              <div className="flex flex-wrap items-center justify-between gap-3">
                <h3 className="text-lg font-bold text-ink">{label}</h3>
                <span className="rounded-lg bg-teal-50 px-3 py-2 text-sm font-semibold text-reef">{tierItems.length} booking links</span>
              </div>
              <div className="mt-4 grid gap-5 sm:grid-cols-2 lg:grid-cols-3">
                {tierItems.map((item) => <ListingCard key={item.id} item={item} />)}
              </div>
            </section>
          );
        })}
      </div>
    </div>
  );
}
