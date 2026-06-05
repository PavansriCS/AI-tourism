export const mapProvider = import.meta.env.VITE_MAP_PROVIDER || "openstreetmap";

export function mapsEmbedUrl(latitude, longitude, zoom = 13) {
  const lat = Number(latitude);
  const lon = Number(longitude);
  const delta = zoom >= 14 ? 0.018 : 0.04;
  const bbox = [
    lon - delta,
    lat - delta,
    lon + delta,
    lat + delta
  ].join(",");
  return `https://www.openstreetmap.org/export/embed.html?bbox=${bbox}&layer=mapnik&marker=${lat},${lon}`;
}

export async function geocodePlace(place) {
  const query = encodeURIComponent(place);
  const response = await fetch(`https://nominatim.openstreetmap.org/search?format=json&limit=1&q=${query}`);
  if (!response.ok) throw new Error("Unable to load OpenStreetMap location");
  const results = await response.json();
  if (!results.length) throw new Error("OpenStreetMap location not found");
  return { latitude: results[0].lat, longitude: results[0].lon };
}

export function openNavigation(place) {
  window.open(`https://www.openstreetmap.org/search?query=${encodeURIComponent(place)}`, "_blank", "noopener,noreferrer");
}
