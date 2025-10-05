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
