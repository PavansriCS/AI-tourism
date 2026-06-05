import { ExternalLink, Headphones, MapPin, Navigation, Star } from "lucide-react";
import { useState } from "react";
import { Link } from "react-router-dom";
import { openNavigation } from "../services/maps.js";

export default function ListingCard({ item, type = "hotel" }) {
  const [expanded, setExpanded] = useState(false);
  const location = `${item.name}, ${item.destination || item.city || ""}`;
  const officialUrl = item.officialWebsite;
  const bookingUrl = item.bookingUrl || item.officialWebsite;
  const contactUrl = item.providerHelpUrl || item.providerContact || item.officialWebsite;
  const imageFallback = "https://images.unsplash.com/photo-1566073771259-6a8506099945?auto=format&fit=crop&w=1200&q=80";
  const bookNow = () => bookingUrl && window.open(bookingUrl, "_blank", "noopener,noreferrer");
  const openOfficial = () => officialUrl && window.open(officialUrl, "_blank", "noopener,noreferrer");
  const openContact = () => contactUrl && window.open(contactUrl, "_blank", "noopener,noreferrer");

  return (
    <article className="overflow-hidden rounded-lg border border-teal-100 bg-white shadow-sm transition hover:-translate-y-1 hover:shadow-soft">
      <img
        src={item.image || imageFallback}
        alt={item.name}
        onError={(event) => {
          event.currentTarget.src = imageFallback;
        }}
        className="aspect-[4/3] w-full object-cover sm:aspect-[16/10]"
      />
      <div className="p-4 sm:p-5">
        <div className="mb-2 flex items-start justify-between gap-3">
          <div>
            <h3 className="text-lg font-bold text-ink">{item.name}</h3>
            <p className="mt-1 flex items-center gap-1 text-sm text-slate-600"><MapPin size={15} /> {item.location || item.destination}</p>
          </div>
          <span className="flex shrink-0 items-center gap-1 rounded-lg bg-amber-50 px-2 py-1 text-sm font-bold text-amber-700"><Star size={15} fill="currentColor" /> {item.rating}</span>
        </div>
        <p className="line-clamp-3 min-h-[72px] text-sm leading-6 text-slate-600">{item.description}</p>
        <div className="mt-4 grid gap-2 rounded-lg bg-slate-50 p-3 text-sm text-slate-700">
          <p><strong>Booking tier:</strong> {item.bookingTier || "Standard"}</p>
          <p><strong>Booking site:</strong> {item.bookingProvider || "Official provider"}</p>
          <p><strong>Price range:</strong> {item.priceRange || "Check official site"}</p>
          {item.distance && <p><strong>Distance:</strong> {item.distance}</p>}
          {item.openingHours && <p><strong>Opening hours:</strong> {item.openingHours}</p>}
        </div>
        <div className="mt-4 flex flex-wrap gap-2">
          {(item.facilities || item.categories || []).slice(0, 4).map((feature) => (
            <span key={feature} className="rounded-lg bg-teal-50 px-2 py-1 text-xs font-semibold text-reef">{feature}</span>
          ))}
        </div>
        {expanded && (
          <div className="mt-4 rounded-lg bg-slate-50 p-3 text-sm leading-6 text-slate-700">
            <p><strong>Location:</strong> {item.location || item.destination}</p>
            <p><strong>Destination:</strong> {item.destination || item.city}</p>
          </div>
        )}
        <div className="mt-5 grid gap-2 sm:grid-cols-2">
          {type === "destination" ? (
            <Link to={`/destinations/${item.slug}`} className="btn-secondary py-2">View Details</Link>
          ) : (
            <button onClick={() => setExpanded((value) => !value)} className="btn-secondary py-2">View Details</button>
          )}
          {type !== "destination" && <button onClick={() => openNavigation(location)} className="btn-secondary py-2"><Navigation size={16} /> Navigate</button>}
          <button onClick={openOfficial} disabled={!officialUrl} className="btn-secondary py-2"><ExternalLink size={16} /> Official Website</button>
          <button onClick={openContact} disabled={!contactUrl} className="btn-secondary py-2"><Headphones size={16} /> Contact</button>
          <button onClick={bookNow} disabled={!bookingUrl} className="btn-primary py-2">Book Now</button>
        </div>
      </div>
    </article>
  );
}
