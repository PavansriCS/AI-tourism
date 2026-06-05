import { Send } from "lucide-react";
import { useEffect, useRef, useState } from "react";
import api from "../services/api.js";

export default function ChatbotPage() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("I am visiting Ooty for 3 days. Suggest a safe family itinerary.");
  const [loading, setLoading] = useState(false);
  const endRef = useRef(null);

  useEffect(() => {
    api.get("/ai/chat/history").then(({ data }) => setMessages(data.history || []));
  }, []);

  useEffect(() => {
    endRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  const send = async (event) => {
    event.preventDefault();
    if (!input.trim()) return;
    const userMessage = { role: "user", content: input };
    setMessages((current) => [...current, userMessage]);
    setInput("");
    setLoading(true);
    try {
      const { data } = await api.post("/ai/chat", { message: userMessage.content });
      setMessages((current) => [...current, { role: "assistant", content: data.reply }]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <section className="page-shell py-10">
      <h1 className="section-title">AI Tourism Assistant</h1>
      <p className="muted mt-2">All Tourism Assistant: Your Complete AI-Powered Travel and Tourism Companion.</p>
      <div className="mt-7 grid min-h-[620px] overflow-hidden rounded-lg border border-teal-100 bg-white shadow-soft lg:grid-cols-[280px_1fr]">
        <aside className="border-b border-teal-100 bg-teal-50 p-5 lg:border-b-0 lg:border-r">
          <h2 className="font-bold">Assistant Context</h2>
          <p className="mt-3 text-sm leading-6 text-slate-600">All Tourism Assistant responds as a 24/7 tourism concierge using platform data, OpenAI when configured, and safety-first travel guidance.</p>
        </aside>
        <div className="flex min-h-[620px] flex-col">
          <div className="flex-1 space-y-4 overflow-y-auto p-5">
            {messages.length === 0 && <p className="rounded-lg bg-slate-50 p-4 text-slate-600">Start a travel question to build your conversation history.</p>}
            {messages.map((message, index) => (
              <div key={`${message.role}-${index}`} className={`flex ${message.role === "user" ? "justify-end" : "justify-start"}`}>
                <div className={`max-w-[78%] rounded-lg px-4 py-3 text-sm leading-6 ${message.role === "user" ? "bg-reef text-white" : "bg-slate-100 text-slate-800"}`}>{message.content}</div>
              </div>
            ))}
            {loading && <p className="text-sm font-semibold text-reef">Thinking through the safest travel answer...</p>}
            <div ref={endRef} />
          </div>
          <form onSubmit={send} className="grid gap-3 border-t border-teal-100 p-4 sm:grid-cols-[1fr_auto]">
            <input className="input" value={input} onChange={(e) => setInput(e.target.value)} placeholder="Ask All Tourism Assistant..." />
            <button className="btn-primary" disabled={loading}><Send size={18} /> Send</button>
          </form>
        </div>
      </div>
    </section>
  );
}
