export default {
  content: ["./index.html", "./src/**/*.{js,jsx}"],
  theme: {
    extend: {
      fontFamily: {
        sans: ["Inter", "ui-sans-serif", "system-ui", "Segoe UI", "sans-serif"]
      },
      colors: {
        ink: "#10201f",
        reef: "#0f766e",
        lagoon: "#0ea5a4",
        sun: "#f59e0b",
        coral: "#f97363"
      },
      boxShadow: {
        soft: "0 18px 60px rgba(15, 118, 110, 0.16)"
      }
    }
  },
  plugins: []
};

