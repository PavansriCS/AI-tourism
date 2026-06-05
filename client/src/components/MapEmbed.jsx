import { mapsEmbedUrl } from "../services/maps.js";

export default function MapEmbed({ query, className = "" }) {
  return (
    <div className={`overflow-hidden rounded-lg border border-teal-100 bg-white ${className}`}>
      <iframe
        title={`Map for ${query}`}
        src={mapsEmbedUrl(query)}
        className="h-full min-h-[320px] w-full"
        loading="lazy"
        referrerPolicy="no-referrer-when-downgrade"
      />
    </div>
  );
}

