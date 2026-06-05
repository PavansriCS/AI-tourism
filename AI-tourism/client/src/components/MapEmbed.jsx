import { useEffect, useState } from "react";
import { geocodePlace, mapsEmbedUrl, openNavigation } from "../services/maps.js";

export default function MapEmbed({ query, className = "" }) {
  const [src, setSrc] = useState("");

  useEffect(() => {
    let active = true;
    setSrc("");
    geocodePlace(query)
      .then(({ latitude, longitude }) => {
        if (active) setSrc(mapsEmbedUrl(latitude, longitude));
      })
      .catch(() => {
        if (active) setSrc("");
      });
    return () => {
      active = false;
    };
  }, [query]);

  return (
    <div className={`overflow-hidden rounded-lg border border-teal-100 bg-white ${className}`}>
      {src ? (
        <iframe
          title={`OpenStreetMap for ${query}`}
          src={src}
          className="h-full min-h-[320px] w-full"
          loading="lazy"
          referrerPolicy="no-referrer-when-downgrade"
        />
      ) : (
        <button
          type="button"
          onClick={() => openNavigation(query)}
          className="flex h-full min-h-[320px] w-full items-center justify-center bg-slate-50 p-6 text-sm font-semibold text-reef"
        >
          Open {query} in OpenStreetMap
        </button>
      )}
    </div>
  );
}
