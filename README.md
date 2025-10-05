# Organic Advisory System with Photo Recognition for Tribal Farmers

## Objective
AI-powered app for tribal farmers: Crop disease/pest ID via photo, organic solutions, traditional knowledge DB, guides, calendar, weather alerts, forum, tracking, Telugu multimedia, offline PWA, supplier integration.

## Architecture
- Frontend: React.js PWA (offline via Workbox/IndexedDB).
- Backend: FastAPI (Python) with TensorFlow AI.
- DB: PostgreSQL.
- Features: All 11 as specified.

## Quick Setup
1. Backend: `cd backend && python -m venv venv && source venv/bin/activate && pip install -r requirements.txt && psql -f db_schema.sql && psql -f sample_data.sql && uvicorn app.main:app --reload`.
2. AI Train: `cd ai_model_training && python train_model.py` (download dataset first).
3. Frontend: `cd frontend && npm install && npm start`.
4. Test: http://localhost:3000 (frontend), http://localhost:8000/docs (API).

## Deployment
- Backend: Heroku (Python buildpack).
- Frontend: Netlify (PWA auto).
- DB: Supabase PostgreSQL.

## Telugu Support
- Text: react-i18next.
- Voice: Web Speech API ('te-IN').
- Fonts: Add <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+Telugu&display=swap" rel="stylesheet"> to public/index.html.

## Offline
- PWA: Install via browser.
- Cache: Guides/tutorials; queue uploads/posts.

## Sample Test
- Login: farmer1 / pass.
- Upload: Aphid rice image → Neem recommendation in Telugu.
