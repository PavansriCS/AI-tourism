import ListingCard from "../components/ListingCard.jsx";
import MapEmbed from "../components/MapEmbed.jsx";
import useFetch from "../hooks/useFetch.js";

const config = {
  hotels: {
    title: "Hotels",
    subtitle: "Verified hotel listings with ratings, facilities, map navigation, official websites, and external booking redirects.",
    endpoint: "/hotels",
    keys: ["hotels"],
    mapQuery: "Hotels in Ooty Yercaud Goa Chennai Kodaikanal"
  },
  resorts: {
    title: "Resorts",
    subtitle: "Premium resort stays across hill stations and coastal destinations, always booked on official provider pages.",
    endpoint: "/resorts",
    keys: ["resorts"],
    mapQuery: "Resorts in Ooty Yercaud Goa Kodaikanal"
  },
  restaurants: {
    title: "Restaurants",
    subtitle: "Nearby restaurants, cuisine categories, ratings, distance, opening hours, and Google Maps navigation.",
    endpoint: "/restaurants",
    keys: ["restaurants"],
    mapQuery: "Popular restaurants in Ooty Goa Chennai Yercaud Kodaikanal"
  },
  attractions: {
    title: "Tourist Attractions",
    subtitle: "Tourist places with official tourism links, price ranges, directions, and provider booking or information pages.",
    endpoint: "/attractions",
    keys: ["attractions"],
    mapQuery: "Tourist attractions in Ooty Yercaud Goa Chennai Kodaikanal"
  },
  "water-parks": {
    title: "Water Theme Parks",
    subtitle: "Water parks and amusement experiences with real ticketing or official external booking URLs.",
    endpoint: "/water-parks",
    keys: ["waterParks"],
    mapQuery: "Water theme parks Chennai Goa"
  },
  "adventure-parks": {
    title: "Adventure Parks",
    subtitle: "Adventure activities and outdoor experiences with directions, price ranges, and external booking pages.",
    endpoint: "/adventure-parks",
    keys: ["adventureParks"],
    mapQuery: "Adventure activities in Ooty Yercaud Goa Kodaikanal"
  }
};

export default function ListingModule({ module }) {
  const current = config[module];
  const fallback = Object.fromEntries(current.keys.map((key) => [key, []]));
  const { data, loading } = useFetch(current.endpoint, fallback);
  const items = current.keys.flatMap((key) => data?.[key] || []);

  return (
    <section className="page-shell py-10">
      <div className="flex flex-col justify-between gap-4 md:flex-row md:items-end">
        <div>
          <h1 className="section-title">{current.title}</h1>
          <p className="muted mt-2 max-w-3xl">{current.subtitle}</p>
        </div>
        <div className="rounded-lg bg-amber-50 px-4 py-3 text-sm font-semibold text-amber-800">
          External booking only. No internal payments.
        </div>
      </div>
      <div className="mt-7 grid gap-6 xl:grid-cols-[1fr_380px]">
        <div className="grid gap-5 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-2">
          {loading && <p className="rounded-lg bg-white p-6 text-slate-600 md:col-span-2">Loading verified tourism listings...</p>}
          {!loading && <TieredListings items={items} />}
        </div>
        <MapEmbed query={current.mapQuery} className="h-[360px] xl:sticky xl:top-24 xl:h-[540px]" />
      </div>
    </section>
  );
}

const tiers = [
  ["Budget", "Budget Friendly Options"],
  ["Standard", "Standard Options"],
  ["High-Class", "High-Class Options"]
];

function TieredListings({ items }) {
  return (
    <div className="space-y-8 sm:col-span-2 lg:col-span-3 xl:col-span-2">
      {tiers.map(([tier, label]) => {
        const tierItems = items.filter((item) => (item.bookingTier || "Standard") === tier);
        if (!tierItems.length) return null;
        return (
          <section key={tier}>
            <div className="flex flex-wrap items-center justify-between gap-3">
              <h2 className="text-lg font-bold text-ink">{label}</h2>
              <span className="rounded-lg bg-teal-50 px-3 py-2 text-sm font-semibold text-reef">{tierItems.length} booking links</span>
            </div>
            <div className="mt-4 grid gap-5 sm:grid-cols-2 xl:grid-cols-2">
              {tierItems.map((item) => <ListingCard key={item.id} item={item} />)}
            </div>
          </section>
        );
      })}
    </div>
  );
}
