import ListingCard from "../components/ListingCard.jsx";
import MapEmbed from "../components/MapEmbed.jsx";
import useFetch from "../hooks/useFetch.js";

export default function Hotels() {
  const { data } = useFetch("/hotels", { hotels: [], resorts: [] });
  const items = [...data.hotels, ...data.resorts];
  return (
    <section className="page-shell py-10">
      <h1 className="section-title">Hotels and Resorts</h1>
      <p className="muted mt-2">Compare stays, facilities, price ranges, maps, official websites, and provider booking links.</p>
      <div className="mt-7 grid gap-6 lg:grid-cols-[1fr_380px]">
        <div className="grid gap-5 md:grid-cols-2">
          {items.map((item) => <ListingCard key={item.id} item={item} />)}
        </div>
        <MapEmbed query="Hotels and resorts in Tamil Nadu and Goa" className="sticky top-24 h-[540px]" />
      </div>
    </section>
  );
}

