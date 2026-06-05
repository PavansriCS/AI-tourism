export const mapsKey = import.meta.env.VITE_GOOGLE_MAPS_API_KEY || "";

export function mapsEmbedUrl(place) {
  const query = encodeURIComponent(place);
  if (!mapsKey || mapsKey.includes("replace-with")) {
    return `https://maps.google.com/maps?q=${query}&output=embed`;
  }
  return `https://www.google.com/maps/embed/v1/place?key=${mapsKey}&q=${query}`;
}

export function openNavigation(place) {
  window.open(`https://www.google.com/maps/dir/?api=1&destination=${encodeURIComponent(place)}`, "_blank");
}

