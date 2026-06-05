# All Tourism Assistant Deployment Guide

This project is ready for a public deployment with:

- Frontend: Vercel
- Backend: Render
- Database: MongoDB Atlas

## 1. MongoDB Atlas

1. Create an Atlas cluster.
2. Create a database user with read/write permissions.
3. Allow Render outbound access. For a quick launch, add `0.0.0.0/0` in Network Access, then tighten it later.
4. Copy your connection string and set the database name to `all_tourism_assistant`.

Example:

```env
MONGO_URI=mongodb+srv://USER:PASSWORD@cluster.mongodb.net/all_tourism_assistant?retryWrites=true&w=majority
MONGO_DB_NAME=all_tourism_assistant
```

The API seeds these collections when empty:

- `destinations`
- `hotels`
- `resorts`
- `restaurants`
- `tourist_attractions`
- `water_theme_parks`
- `adventure_parks`
- `notifications`

User-created data goes into:

- `users`
- `trips`
- `chatbot_history`

## 2. Backend on Render

Create a Render Web Service from the repository.

Recommended settings:

- Root directory: `server`
- Build command: `pip install -r requirements.txt`
- Start command: `gunicorn app:app --bind 0.0.0.0:$PORT`

Render environment variables:

```env
FLASK_ENV=production
MONGO_URI=mongodb+srv://USER:PASSWORD@cluster.mongodb.net/all_tourism_assistant?retryWrites=true&w=majority
MONGO_DB_NAME=all_tourism_assistant
JWT_SECRET_KEY=use-a-long-random-production-secret-at-least-32-characters
GROK_API_KEY=xai-...
GROK_MODEL=grok-3-mini
GROK_BASE_URL=https://api.x.ai/v1
CLIENT_ORIGIN=https://your-all-tourism-assistant.vercel.app
```

After deploy, verify:

```text
https://your-all-tourism-assistant-api.onrender.com/api/health
```

Expected response:

```json
{ "status": "ok", "service": "All Tourism Assistant API" }
```

## 3. Frontend on Vercel

Create a Vercel project from the repository.

Recommended settings:

- Root directory: `client`
- Framework preset: Vite
- Build command: `npm run build`
- Output directory: `dist`

Vercel environment variables:

```env
VITE_API_BASE_URL=https://your-all-tourism-assistant-api.onrender.com/api
VITE_MAP_PROVIDER=openstreetmap
```

Deploy, then copy the Vercel production URL back into Render as `CLIENT_ORIGIN`.

## 4. OpenStreetMap

All Tourism Assistant uses OpenStreetMap for map embeds and navigation links. No browser map API key is required.

Map embeds geocode places through the public OpenStreetMap Nominatim endpoint and render an OpenStreetMap iframe.

## 5. Grok / xAI

Set `GROK_API_KEY` on Render. If the key is missing, All Tourism Assistant uses a local tourism fallback so the app remains usable, but live Grok responses require the key.

## 6. Booking Flow

All Tourism Assistant is an aggregator and does not process payments.

All listing cards use:

```js
window.open(item.bookingUrl, "_blank");
```

Every hotel, resort, restaurant, attraction, water park, and adventure listing includes a `bookingUrl` field.

## 7. Final Public URLs

Once deployed, your public app will be:

```text
Frontend: https://your-all-tourism-assistant.vercel.app
Backend:  https://your-all-tourism-assistant-api.onrender.com
Health:   https://your-all-tourism-assistant-api.onrender.com/api/health
```
