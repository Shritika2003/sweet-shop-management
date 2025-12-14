Overview
The Sweet Shop Management System is a full-stack web application designed to manage sweets in a shop. 
It allows users to register and log in, view available sweets, search and filter them, purchase sweets, and manage inventory.
Admin users can add, update, restock, or delete sweets. The project follows clean coding practices and RESTful API design.
Tech Stack
Backend: Python, FastAPI
Database: SQLite
Authentication: JWT (JSON Web Tokens)
Frontend: React
Version Control: Git & GitHub
Features
User registration and login with JWT authentication
View all available sweets
Search sweets by name, category, or price
Purchase sweets (quantity decreases automatically)
Admin-only operations: add, update, delete, and restock sweets
Simple and clean React UI
How to Run the Project Locally
Backend
Navigate to the backend folder
Activate virtual environment
Run the server: uvicorn app.main:app --port 8001
API documentation available at:http://127.0.0.1:8001/docs
Frontend
Navigate to the frontend folder
Install dependencies:npm install
Start the frontend: npm start
Open in browser:http://localhost:3000
My AI Usage
I used ChatGPT as an AI assistant during development.
It helped me understand API design, debug errors, structure FastAPI routes, and improve code readability.
All final implementation decisions, logic, and debugging were done by me.
AI helped speed up development and learning, but I ensured I fully understood and owned the code.
