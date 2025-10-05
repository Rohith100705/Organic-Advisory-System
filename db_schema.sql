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
