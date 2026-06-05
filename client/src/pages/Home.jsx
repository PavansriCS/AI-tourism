import { motion } from "framer-motion";
import { ArrowRight, MapPin, ShieldCheck, Sparkles } from "lucide-react";
import { Link } from "react-router-dom";
import ListingCard from "../components/ListingCard.jsx";
import SearchPanel from "../components/SearchPanel.jsx";
import useFetch from "../hooks/useFetch.js";

export default function Home() {
  const { data } = useFetch("/public/home", { destinations: [], hotels: [], restaurants: [] });

  return (
    <>
      <section className="hero-bg min-h-[620px] text-white sm:min-h-[640px]">
        <div className="page-shell flex min-h-[620px] flex-col justify-center pb-10 pt-10 sm:min-h-[640px] sm:pt-16">
          <motion.div initial={{ opacity: 0, y: 18 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.7 }} className="max-w-3xl">
            <p className="mb-4 inline-flex items-center gap-2 rounded-lg bg-white/15 px-3 py-2 text-sm font-semibold backdrop-blur"><Sparkles size={16} /> AI-powered tourism aggregator</p>
            <h1 className="text-4xl font-extrabold leading-tight tracking-normal sm:text-5xl lg:text-6xl">All Tourism Assistant</h1>
            <p className="mt-5 max-w-2xl text-base leading-7 text-white/88 sm:text-lg sm:leading-8">
              Your Complete AI-Powered Travel and Tourism Companion.
            </p>
          </motion.div>
          <div className="mt-9 max-w-6xl">
            <SearchPanel />
          </div>
        </div>
      </section>

      <section className="page-shell -mt-8 grid gap-4 sm:-mt-12 md:grid-cols-3">
        {[
          ["AI trip planning", "Day-wise routes, time estimates, costs, and nearby attraction sequencing.", Sparkles],
          ["Live navigation", "OpenStreetMap embeds, direction links, and location-aware discovery flows.", MapPin],
          ["Safety guidance", "Hospitals, police stations, weather alerts, emergency contacts, and safer area recommendations.", ShieldCheck]
        ].map(([title, text, Icon]) => (
          <div key={title} className="rounded-lg border border-teal-100 bg-white p-5 shadow-soft">
            <Icon className="text-reef" />
            <h3 className="mt-4 font-bold">{title}</h3>
            <p className="mt-2 text-sm leading-6 text-slate-600">{text}</p>
          </div>
        ))}
      </section>

      <section className="page-shell mt-12 sm:mt-16">
        <div className="mb-7 flex items-end justify-between gap-4">
          <div>
            <h2 className="section-title">Trending Destinations</h2>
            <p className="muted mt-2">Handpicked South India and coastal favorites with official travel pathways.</p>
          </div>
          <Link to="/search" className="btn-secondary hidden sm:inline-flex">Explore all <ArrowRight size={16} /></Link>
        </div>
        <div className="grid gap-5 sm:grid-cols-2 lg:grid-cols-3">
          {data.destinations.map((item) => <ListingCard key={item.slug} item={item} type="destination" />)}
        </div>
      </section>

      <section className="page-shell mt-12 sm:mt-16">
        <h2 className="section-title">Featured Resorts</h2>
        <div className="mt-7 grid gap-5 sm:grid-cols-2 lg:grid-cols-3">
          {data.hotels.map((item) => <ListingCard key={item.id} item={item} />)}
        </div>
      </section>

      <section className="page-shell mt-12 sm:mt-16">
        <h2 className="section-title">Popular Restaurants</h2>
        <div className="mt-7 grid gap-5 sm:grid-cols-2 lg:grid-cols-3">
          {data.restaurants.map((item) => <ListingCard key={item.id} item={item} type="restaurant" />)}
        </div>
      </section>

      <section className="page-shell mt-12 sm:mt-16">
        <h2 className="section-title">Bookable Experiences</h2>
        <p className="muted mt-2">Water parks, adventure activities, and tourist attractions with external provider booking links.</p>
        <div className="mt-7 grid gap-5 sm:grid-cols-2 lg:grid-cols-3">
          {[...(data.waterParks || []), ...(data.adventureParks || []), ...(data.attractions || [])].slice(0, 6).map((item) => <ListingCard key={item.id} item={item} />)}
        </div>
      </section>
    </>
  );
}
