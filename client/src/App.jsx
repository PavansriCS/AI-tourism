import { Navigate, Route, Routes } from "react-router-dom";
import Navbar from "./components/Navbar.jsx";
import Footer from "./components/Footer.jsx";
import FloatingChatbot from "./components/FloatingChatbot.jsx";
import ProtectedRoute from "./components/ProtectedRoute.jsx";
import Home from "./pages/Home.jsx";
import Login from "./pages/Login.jsx";
import Signup from "./pages/Signup.jsx";
import Profile from "./pages/Profile.jsx";
import SearchResults from "./pages/SearchResults.jsx";
import DestinationDetails from "./pages/DestinationDetails.jsx";
import ListingModule from "./pages/ListingModule.jsx";
import TripPlanner from "./pages/TripPlanner.jsx";
import ChatbotPage from "./pages/ChatbotPage.jsx";
import Safety from "./pages/Safety.jsx";
import Notifications from "./pages/Notifications.jsx";

export default function App() {
  return (
    <div className="min-h-screen bg-[#f5faf8] text-ink">
      <Navbar />
      <main>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/login" element={<Login />} />
          <Route path="/signup" element={<Signup />} />
          <Route path="/search" element={<SearchResults />} />
          <Route path="/destinations/:slug" element={<DestinationDetails />} />
          <Route path="/hotels" element={<ListingModule module="hotels" />} />
          <Route path="/resorts" element={<ListingModule module="resorts" />} />
          <Route path="/restaurants" element={<ListingModule module="restaurants" />} />
          <Route path="/attractions" element={<ListingModule module="attractions" />} />
          <Route path="/water-parks" element={<ListingModule module="water-parks" />} />
          <Route path="/adventure-parks" element={<ListingModule module="adventure-parks" />} />
          <Route path="/planner" element={<ProtectedRoute><TripPlanner /></ProtectedRoute>} />
          <Route path="/chatbot" element={<ProtectedRoute><ChatbotPage /></ProtectedRoute>} />
          <Route path="/safety" element={<Safety />} />
          <Route path="/notifications" element={<ProtectedRoute><Notifications /></ProtectedRoute>} />
          <Route path="/profile" element={<ProtectedRoute><Profile /></ProtectedRoute>} />
          <Route path="*" element={<Navigate to="/" replace />} />
        </Routes>
      </main>
      <FloatingChatbot />
      <Footer />
    </div>
  );
}
