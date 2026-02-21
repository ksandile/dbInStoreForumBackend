# Full Stack Forum Project – README

## Table of Contents

1. [Tech Stack Justification](#1-tech-stack-justification)  
2. [Setup Backend](#2-setup-backend)  
3. [Setup Frontend](#3-setup-frontend)  
4. [How to Run the Project (macOS)](#4-how-to-run-the-project-macos)  
5. [How to Run the Project (Windows)](#5-how-to-run-the-project-windows)  
6. [Load Dummy Data](#6-load-dummy-data)  
7. [Create Moderators Manually (Optional)](#7-create-moderators-manually-optional)  
8. [Public API for 3rd-Party Users](#8-public-api-for-3rd-party-users)  
9. [Login Page Setup](#9-login-page-setup)  
10. [Comments Feature](#10-comments-feature)  
11. [Additional Documentation & Diagram](#11-additional-documentation--diagram)

---

## 1. Tech Stack Justification

**Backend:** Django + Django REST Framework  
Provides secure and scalable API development.

**Database:** PostgreSQL  
Relational database for structured forum data.

**Frontend:** React  
Fast and responsive user interface.

**API Testing:** Postman  
Used for third-party API interaction.

---

## 2. Setup Backend

### macOS / Linux

```bash
cd dbInStoreForumBackend
source venv/bin/activate
pip install -r requirements.txt
Windows
cd dbInStoreForumBackend
venv\Scripts\activate
pip install -r requirements.txt
3. Setup Frontend
cd frontend
npm install

Frontend runs on:

http://localhost:3000

4. How to Run the Project (macOS)
Step 1 – Run Backend

Open Terminal:

cd dbInStoreForumBackend
source venv/bin/activate
python manage.py runserver

Backend will run at:

http://127.0.0.1:8000/

Step 2 – Open Second Terminal (Important)

Open a new terminal window:

cd dbInStoreForumBackend
source venv/bin/activate
cd frontend
npm start

Frontend will run at:

http://localhost:3000/

Keep both terminals open while using the application.

5. How to Run the Project (Windows)
Step 1 – Run Backend

Open Command Prompt or PowerShell:

cd dbInStoreForumBackend
venv\Scripts\activate
python manage.py runserver

Backend will run at:

http://127.0.0.1:8000/

Step 2 – Open Second Command Prompt
cd dbInStoreForumBackend
venv\Scripts\activate
cd frontend
npm start

Frontend will run at:

http://localhost:3000/

Keep both terminals open while using the system.

6. Load Dummy Data
python manage.py loaddata forum/dummy_data.json

Ensure:

/forum/dummy_data.json

exists and is committed.

7. Create Moderators Manually (Optional)
python manage.py shell

Inside shell:

from forum.models import tUsers
user = tUsers.objects.get(sEmail="mod@gmail.com")
user.sRole = "moderator"
user.save()
8. Public API for 3rd-Party Users

Ensure backend is running before testing.

Example Endpoints

Register
POST
http://127.0.0.1:8000/api/register/

Login
POST
http://127.0.0.1:8000/api/login/

Get Posts
GET
http://127.0.0.1:8000/api/posts/

Header:

Authorization: Token YOUR_TOKEN

Create Post
POST
http://127.0.0.1:8000/api/posts/

Like Post
POST
http://127.0.0.1:8000/api/posts/<POST_ID>/like/

Comment Post
POST
http://127.0.0.1:8000/api/posts/<POST_ID>/comments/

Flag Post
PATCH
http://127.0.0.1:8000/api/posts/<POST_ID>/flag/

9. Login Page Setup

Login page includes:

Application logo

Company name displayed prominently

Example:

InStoreForum AI

10. Comments Feature

Comments are collapsible.

Default display:

View Comments ▼

Click to expand.
Click again to collapse.

11. Additional Documentation & Diagram

Project Diagram:
https://viewer.diagrams.net/?tags=%7B%7D&lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Untitled%20Diagram.drawio&dark=auto#Uhttps%3A%2F%2Fraw.githubusercontent.com%2Fksandile%2FdbInStoreForumBackend%2Fmain%2FUntitled%2520Diagram.drawio

Project Documentation:
https://docs.google.com/document/d/1lQilOWOf6zLZh84O7D1t_nnjqi4Cq3UEombg5DWVYvs/edit?usp=sharing
