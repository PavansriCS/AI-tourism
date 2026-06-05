import { Bot } from "lucide-react";
import { Link } from "react-router-dom";
import { useAuth } from "../context/AuthContext.jsx";

export default function FloatingChatbot() {
  const { isAuthenticated } = useAuth();
  return (
    <Link
      to={isAuthenticated ? "/chatbot" : "/login"}
      className="fixed bottom-[calc(1.25rem+env(safe-area-inset-bottom))] right-4 z-50 grid h-14 w-14 place-items-center rounded-full bg-reef text-white shadow-soft transition hover:scale-105 sm:right-5"
      title="Open AI tourism assistant"
    >
      <Bot size={24} />
    </Link>
  );
}
