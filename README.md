# 📝 Django Task Manager

A simple task management web app built with Django, TailwindCSS, and deployed on Render.

## 🚀 Features
- User authentication (Login, Register, Logout)
- Create, update, delete tasks
- Task status badges (complete/incomplete)
- Filters and search
- Profile management
- Upcoming task reminders

## 🛠️ Tech Stack
- Django (Backend)
- TailwindCSS (Frontend)
- PostgreSQL (Production)
- Render (Hosting)

## Setup Instructions
```bash
git clone https://github.com/Bulwark-Inc/taskManager.git
cd taskManager
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```