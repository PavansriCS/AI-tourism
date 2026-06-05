import ListingCard from "../components/ListingCard.jsx";
import MapEmbed from "../components/MapEmbed.jsx";
import useFetch from "../hooks/useFetch.js";

export default function Restaurants() {
  const { data } = useFetch("/restaurants", { restaurants: [] });
  return (
    <section className="page-shell py-10">
      <h1 className="section-title">Restaurant Discovery</h1>
      <p className="muted mt-2">Nearby restaurants, cuisine categories, ratings, opening hours, distance cues, and OpenStreetMap navigation.</p>
      <div className="mt-7 grid gap-6 lg:grid-cols-[1fr_380px]">
        <div className="grid gap-5 md:grid-cols-2">
          {data.restaurants.map((item) => <ListingCard key={item.id} item={item} type="restaurant" />)}
        </div>
        <MapEmbed query="Popular restaurants in Ooty Goa Chennai Yercaud Kodaikanal" className="sticky top-24 h-[540px]" />
      </div>
    </section>
  );
}
