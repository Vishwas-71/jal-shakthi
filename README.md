# Jalshakti – Civic Water Issue Reporting System

Jalshakti is a full-stack web application that allows citizens to report water-related issues such as flooding, drainage blockages, water leakage, and infrastructure damage. The platform helps authorities track and manage reported issues efficiently.

## Features
- User Registration and Login using JWT Authentication
- Report water-related issues with images and location
- Interactive map integration using Leaflet
- Dashboard to view submitted reports
- Image upload support
- Admin management through Django Admin Panel

## Tech Stack
Frontend:
- React
- TypeScript
- Tailwind CSS
- Axios
- React Router
- Leaflet Maps

Backend:
- Django
- Django REST Framework
- JWT Authentication (SimpleJWT)

Database:
- SQLite

## Project Structure
Backend – Django REST API  
Frontend – React Application  

## Installation and Setup

### Backend
cd Backend  
python -m venv venv  
venv\Scripts\activate  
pip install -r requirements.txt  
python manage.py migrate  
python manage.py runserver  

Backend runs at:  
http://127.0.0.1:8000

### Frontend
cd Frontend  
npm install  
npm run dev  

Frontend runs at:  
http://localhost:8080

## Author
Vishwas B  
B.Tech Computer Science – Presidency University

## Note
This project was developed as a learning project to demonstrate full-stack development using React and Django REST Framework.
