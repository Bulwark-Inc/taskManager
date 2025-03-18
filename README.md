# TaskManager App

A simple, responsive task management web application built with Django and TailwindCSS. Users can register, create tasks, manage their profiles, and organize their workload with ease.

## 🚀 Features
- User Registration, Login, Password Reset
- Profile View & Edit
- Create, Update, Delete Tasks
- Task Status (Complete/Incomplete)
- Task Filtering (Active/Completed)
- Task Priorities & Due Dates (Upcoming Feature)
- Email Notifications & Reminders (Upcoming Feature)

## ⚙️ Tech Stack
- Backend: Django 4+
- Frontend: TailwindCSS 3+, AOS, Alpine.js, Lucide
- Database: SQLite (Dev), PostgreSQL (Prod Ready)
- Deployment: Render (Live), AWS (Planned)


## 🛠️ Local Setup
1. Clone the repository  
   `git clone https://github.com/Bulwark-Inc/taskManager.git`  
2. Change into the directory  
   `cd taskmanager`  
3. Create and activate a virtual environment  
   `python -m venv env`  
   `source env/bin/activate`  
4. Install dependencies  
   `pip install -r requirements.txt`  
5. Run migrations  
   `python manage.py migrate`  
6. Start the server  
   `python manage.py runserver`

7. Visit `http://127.0.0.1:8000/`  

## 🚀 Deployment

The app is currently deployed on Render:  
👉 [Live Demo](https://taskmanager-pqvt.onrender.com/)