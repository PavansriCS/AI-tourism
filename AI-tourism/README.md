# All Tourism Assistant

AI-powered tourism aggregator platform with a React/Tailwind frontend and Flask/MongoDB backend.

## Apps

- `client/` - React, Tailwind CSS, React Router, Axios, Vercel-ready.
- `server/` - Flask REST API, JWT auth, MongoDB Atlas, Grok/xAI integration, Render-ready.

## Quick Start

### Backend

```bash
cd server
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
python app.py
```

The API runs on `http://127.0.0.1:5000`.

### Frontend

```bash
cd client
npm install
copy .env.example .env
npm run dev
```

The frontend runs on `http://localhost:5173`.

## Tourism Collections

MongoDB collections used by the platform:

- `users`
- `destinations`
- `hotels`
- `resorts`
- `restaurants`
- `tourist_attractions`
- `water_theme_parks`
- `adventure_parks`
- `trips`
- `chatbot_history`
- `notifications`

Bookable listing modules are exposed at `/hotels`, `/resorts`, `/restaurants`, `/attractions`, `/water-parks`, and `/adventure-parks`.

## Required Environment Variables

Backend:

- `MONGO_URI` - MongoDB Atlas connection string.
- `JWT_SECRET_KEY` - production JWT signing secret.
- `GROK_API_KEY` - enables live Grok AI responses through xAI.
- `GROK_MODEL` - Grok model name, for example `grok-3-mini`.
- `GROK_BASE_URL` - xAI OpenAI-compatible API base URL.
- `CLIENT_ORIGIN` - frontend origin, for example `https://all-tourism-assistant.vercel.app`.

Frontend:

- `VITE_API_BASE_URL` - Flask API URL.
- `VITE_MAP_PROVIDER` - set to `openstreetmap` for OpenStreetMap embeds/navigation.

## Booking Flow

All Tourism Assistant is an aggregator. It does not process payments. Every `Book Now` action uses:

```js
window.open(bookingUrl, "_blank");
```

and redirects the user to the official provider website.

## Deployment

Use [DEPLOYMENT.md](DEPLOYMENT.md) for the public launch path:

- Deploy `server/` to Render with `gunicorn app:app --bind 0.0.0.0:$PORT`.
- Deploy `client/` to Vercel with `npm run build` and `dist` output.
- Set MongoDB Atlas, Grok/xAI, OpenStreetMap, JWT, CORS, and API URL environment variables in the hosting dashboards.

The app is designed to become publicly accessible at your Vercel URL, backed by the Render API and MongoDB Atlas.

## PWA

All Tourism Assistant includes a production PWA setup:

- `client/public/manifest.webmanifest`
- `client/public/service-worker.js`
- `client/public/offline.html`
- PNG and SVG app icons in `client/public/icons/`

The service worker caches the app shell and provides a basic offline fallback. Mobile installation is available when served from Vercel over HTTPS.
