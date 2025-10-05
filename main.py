### Complete Project Code Archive

Since this is a text-based response, I can't deliver an actual downloadable file (e.g., ZIP), but I've compiled **all the code** from the project into a single, self-contained structure below. This mimics the contents of a ZIP file or GitHub repository. You can:

1. **Create the Project Locally**:
   - Make a root folder: `organic-advisory-system/`.
   - Copy each code block into the specified file path (e.g., create folders like `backend/app/` and paste into `main.py`).
   - Use a text editor (VS Code) or terminal commands to create files: e.g., `mkdir -p backend/app/ai_model_training && touch backend/app/main.py`.

2. **Total Files**: ~20 key files (backend, frontend, DB, AI training). Full codebase is production-prototype ready.
3. **Setup After Copying**:
   - Follow the "Setup and Deployment Instructions" from the first response (e.g., install deps, run SQL, train AI, `npm start` / `uvicorn`).
   - Git Init: `git init`, add all, commit for version control.
   - If you need a ZIP: Copy this into a Markdown file, or use tools like GitHub Gist/Repo to host.

**Assumptions**: 
- i18n JSON files have basic keys (expand as needed).
- Missing minor files (e.g., App.css): Add basic CSS like `body { font-family: 'Noto Sans Telugu', sans-serif; }` for Telugu support.
- AI Dataset: Download to `ai_model_training/data/` before training.
- Env: Create `.env` in backend with keys.

---

#### **Root Files**

**README.md** (Project Overview and Setup):
```markdown
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
```

---

#### **Backend Files**

**backend/requirements.txt**:
```
fastapi==0.104.1
uvicorn==0.24.0
sqlalchemy==2.0.23
psycopg2-binary==2.9.9
tensorflow==2.14.0
pillow==10.1.0
python-jose[cryptography]==3.3.0
passlib[bcrypt]==1.7.4
python-multipart==0.0.6
requests==2.31.0
numpy==1.24.3
```

**backend/.env.example** (Copy to .env and fill):
```
DATABASE_URL=postgresql://username:password@localhost/organic_advisory
WEATHER_API_KEY=your_openweathermap_key
SECRET_KEY=your_jwt_secret_key_here
```

**backend/db_schema.sql**:
```sql
CREATE DATABASE organic_advisory;

\c organic_advisory;

-- Users
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    profile JSONB,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Predictions
CREATE TABLE predictions (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    image_url VARCHAR(255),
    prediction VARCHAR(100),
    confidence FLOAT,
    recommendation JSONB,
    treatment_outcome JSONB,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Solutions
CREATE TABLE solutions (
    id SERIAL PRIMARY KEY,
    issue VARCHAR(100),
    crop VARCHAR(50),
    solution_type VARCHAR(50),
    description TEXT,
    local_materials JSONB,
    steps JSONB
);

-- Seasonal Advisory
CREATE TABLE seasonal_advisory (
    id SERIAL PRIMARY KEY,
    crop VARCHAR(50),
    season VARCHAR(50),
    month INTEGER,
    treatment VARCHAR(100),
    preventive_guide JSONB
);

-- Posts (Forum)
CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    title VARCHAR(200),
    content TEXT,
    replies JSONB DEFAULT '[]',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Suppliers
CREATE TABLE suppliers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    location VARCHAR(100),
    products JSONB,
    contact VARCHAR(100),
    availability JSONB
);

-- Tutorials
CREATE TABLE tutorials (
    id SERIAL PRIMARY KEY,
    title VARCHAR(200),
    language VARCHAR(10) DEFAULT 'te',
    type VARCHAR(50),
    content JSONB,
    topic VARCHAR(100)
);
```

**backend/sample_data.sql**:
```sql
-- Users
INSERT INTO users (username, email, password_hash, profile) VALUES 
('farmer1', 'farmer1@example.com', '$2b$12$examplehashedpass', '{"crops": ["rice"], "location": "Andhra Pradesh"}');  -- Use bcrypt hash in prod

-- Solutions
INSERT INTO solutions (issue, crop, solution_type, description, local_materials, steps) VALUES 
('aphid_pest', 'rice', 'pesticide', 'Neem-based spray for aphids using local materials', '["neem leaves", "water", "soap"]', 
 '[{"step":1, "desc":"Grind 500g neem leaves"}, {"step":2, "desc":"Mix with 5L water and soap"}, {"step":3, "desc":"Spray weekly"}]'),
('nitrogen_deficiency', 'tomato', 'fertilizer', 'Cow dung compost with traditional method', '["cow dung", "green leaves"]', 
 '[{"step":1, "desc":"Mix 1kg cow dung with greens"}, {"step":2, "desc":"Compost for 2 weeks"}, {"step":3, "desc":"Apply to soil base"}]');

-- Seasonal Advisory
INSERT INTO seasonal_advisory (crop, season, month, treatment, preventive_guide) VALUES 
('rice', 'kharif', 6, 'Soil preparation with organic manure', '{"guide": "Apply cow dung before planting", "alert": "Monitor rain for drainage"}');

-- Posts
INSERT INTO posts (user_id, title, content) VALUES 
(1, 'How to handle rice blight organically?', 'Any tips using local tribal herbs?');

-- Suppliers
INSERT INTO suppliers (name, location, products, contact, availability) VALUES 
('Local Organic Farm', 'Tribal Village, AP', '["neem oil", "vermicompost"]', '+91-1234567890', '{"in_stock": true}');

-- Tutorials
INSERT INTO tutorials (title, language, type, content, topic) VALUES 
('Neem Pesticide Preparation Guide', 'te', 'video', '{"url": "https://www.youtube.com/embed/dQw4w9WgXcQ", "script": "నీమ్ ఆకులు గ్రైండ్ చేసి నీటిలో కలపండి. సోప్ జోడించి స్ప్రే చేయండి. (Telugu script for TTS)"}', 'prepare_neem_pesticide');
```

**backend/app/main.py** (Full Backend – Complete from Previous):
```python
from fastapi import FastAPI, UploadFile, File, Depends, HTTPException, status, Form
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine, Column, Integer, String, Float, Text, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel
from jose import JWTError, jwt
from passlib.context import CryptContext
import tensorflow as tf
from PIL import Image
import io
import os
import requests
from datetime import datetime, timedelta
from typing import List, Optional
import json
import numpy as np
from passlib.hash import bcrypt

app = FastAPI(title="Organic Advisory System API")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "https://*.netlify.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# DB Setup
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:pass@localhost/organic_advisory")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# DB Models
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    profile = Column(JSON)

class Prediction(Base):
    __tablename__ = "predictions"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    image_url = Column(String(255))
    prediction = Column(String(100))
    confidence = Column(Float)
    recommendation = Column(JSON)
    treatment_outcome = Column(JSON)
    created_at = Column(Text, default=str(datetime.now()))

class Solution(Base):
    __tablename__ = "solutions"
    id = Column(Integer, primary_key=True)
    issue = Column(String(100))
    crop = Column(String(50))
    solution_type = Column(String(50))
    description = Column(Text)
    local_materials = Column(JSON)
    steps = Column(JSON)

class SeasonalAdvisory(Base):
    __tablename__ = "seasonal_advisory"
    id = Column(Integer, primary_key=True)
    crop = Column(String(50))
    season = Column(String(50))
    month = Column(Integer)
    treatment = Column(String(100))
    preventive_guide = Column(JSON)

class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    title = Column(String(200))
    content = Column(Text)
    replies = Column(JSON, default=list)
    created_at = Column(Text, default=str(datetime.now()))

class Supplier(Base):
    __tablename__ = "suppliers"
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    location = Column(String(100))
    products = Column(JSON)
    contact = Column(String(100))
    availability = Column(JSON)

class Tutorial(Base):
    __tablename__ = "tutorials"
    id = Column(Integer, primary_key=True)
    title = Column(String(200))
    language = Column(String(10), default='te')
    type = Column(String(50))
    content = Column(JSON)
    topic = Column(String(100))

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Auth
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
SECRET_KEY = os.getenv("SECRET_KEY", "your_secret_key_change_me")
ALGORITHM = "HS256"

class UserIn(BaseModel):
    username: str
    email: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class PostIn(BaseModel):
    title: str
    content: str

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

@app.post("/register", response_model=Token)
def register(user: UserIn, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    hashed_password = get_password_hash(user.password)
    new_user = User(username=user.username, email=user.email, password_hash=hashed_password, profile={})
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(data={"sub": user.username}, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/token", response_model=Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == form_data.username).first()
    if not user or not verify_password(form_data.password, user.password_hash):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")
    access_token_expires = timedelta(minutes=30)
    access_token = create_access_token(data={"sub": user.username}, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}

async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate credentials")
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = db.query(User).filter(User.username == username).first()
    if user is None:
        raise credentials_exception
    return user

# AI Model
MODEL_PATH = os.path.join(os.path.dirname(__file__), "ai_model", "plant_model.h5")
labels = ['healthy', 'bacterial_blight', 'aphid_pest', 'nitrogen_deficiency', 'powdery_mildew']

if os.path.exists(MODEL_PATH):
    model = tf.keras.models.load_model(MODEL_PATH)
else:
    model = None  # Train first
    print("Warning: Model not loaded. Run training script.")

@app.post("/predict")
async def predict_disease(
    file: UploadFile = File(...),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    if not file.content_type.startswith('image/'):
        raise HTTPException(status_code=400, detail="File must be an image")
    
    content = await file.read()
    image_url = f"uploads/{file.filename}"
    os.makedirs("uploads", exist_ok=True)
    with open(image_url, "wb") as buffer:
        buffer.write(content)
    
    if model is None:
        raise HTTPException(status_code=500, detail="AI Model not available")
    
    image = Image.open(io.BytesIO(content)).resize((224, 224))
    image_array = np.array(image) / 255.0
    image_array = np.expand_dims(image_array, axis=0)
    
    predictions = model.predict(image_array)
    predicted_class_idx = np.argmax(predictions[0])
    predicted_class = labels[predicted_class_idx]
    confidence = float(predictions[0][predicted_class_idx])
    
    solution = db.query(Solution).filter(Solution.issue == predicted_class).first()
    recommendation = {
        "description": solution.description if solution else "Consult local expert for organic treatment",
        "steps": solution.steps if solution else [],
        "local_materials": solution.local_materials if solution else []
    }
    
    pred = Prediction(
        user_id=current_user.id,
        image_url=image_url,
        prediction=predicted_class,
        confidence=confidence,
        recommendation=recommendation
    )
    db.add(pred)
    db.commit()
    
    return {"prediction": predicted_class, "confidence": confidence, "recommendation": recommendation}

# Weather
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
@app.get("/weather/{location}")
def get_weather_alerts(location: str, crop: str = "rice", db: Session = Depends(get_db)):
    if not WEATHER_API_KEY:
        raise HTTPException(status_code=400, detail="Weather API key not set")
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={WEATHER_API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code != 200:
        raise HTTPException(status_code=400, detail="Weather data unavailable")
    data = response.json()
    temp = data['main']['temp']
    rain = data['weather'][0]['main'] == 'Rain'
    
    advisory = db.query(SeasonalAdvisory).filter(SeasonalAdvisory.crop == crop).first()
    alert = f"Temperature: {temp}°C. {'Rain expected - apply preventive organic treatment.' if rain else 'Dry weather - ensure irrigation.'}"
    if advisory:
        alert += f" Seasonal Advisory: {advisory.treatment}"
    
    return {"alert": alert, "recommendations": advisory.preventive_guide if advisory else {}}

# Community
@app.get("/posts", response_model=List[dict])
def get_posts(db: Session = Depends(get_db)):
    posts = db.query(Post).all()
    return [p.__dict__ for p in posts]

@app.post("/posts")
def create_post(post: PostIn, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    new_post = Post(user_id=current_user.id, title=post.title, content=post.content)
    db.add(new_post)
    db.commit()
   
