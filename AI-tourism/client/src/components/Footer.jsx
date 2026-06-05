import { Link } from "react-router-dom";

export default function Footer() {
  return (
    <footer className="mt-16 border-t border-teal-100 bg-white">
      <div className="page-shell grid gap-8 py-10 md:grid-cols-[1.4fr_1fr_1fr_1fr]">
        <div>
          <h2 className="text-lg font-extrabold text-reef">All Tourism Assistant</h2>
          <p className="mt-3 max-w-sm text-sm leading-6 text-slate-600">
            Your Complete AI-Powered Travel and Tourism Companion.
          </p>
        </div>
        <div>
          <h3 className="font-bold">Explore</h3>
          <Link className="mt-3 block text-sm text-slate-600" to="/search">Destinations</Link>
          <Link className="mt-2 block text-sm text-slate-600" to="/hotels">Hotels and resorts</Link>
          <Link className="mt-2 block text-sm text-slate-600" to="/attractions">Tourist attractions</Link>
          <Link className="mt-2 block text-sm text-slate-600" to="/water-parks">Water theme parks</Link>
          <Link className="mt-2 block text-sm text-slate-600" to="/adventure-parks">Adventure parks</Link>
          <Link className="mt-2 block text-sm text-slate-600" to="/restaurants">Restaurants</Link>
        </div>
        <div>
          <h3 className="font-bold">AI Tools</h3>
          <Link className="mt-3 block text-sm text-slate-600" to="/planner">Trip planner</Link>
          <Link className="mt-2 block text-sm text-slate-600" to="/chatbot">Tourism assistant</Link>
          <Link className="mt-2 block text-sm text-slate-600" to="/safety">Safety hub</Link>
        </div>
        <div>
          <h3 className="font-bold">Aggregator Notice</h3>
          <p className="mt-3 text-sm leading-6 text-slate-600">Bookings are completed on official provider websites. All Tourism Assistant does not collect travel payments.</p>
        </div>
      </div>
    </footer>
  );
}
