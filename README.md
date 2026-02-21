# Full Stack Forum Project – README

## Table of Contents

1. [Tech Stack Justification](#1-tech-stack-justification)  
2. [Setup Backend](#2-setup-backend)  
3. [Setup Frontend](#3-setup-frontend)  
4. [How to Run the Project (macOS)](#4-how-to-run-the-project-macos)  
5. [Load Dummy Data](#5-load-dummy-data)  
6. [Create Moderators Manually (Optional)](#6-create-moderators-manually-optional)  
7. [Public API for 3rd-Party Users](#7-public-api-for-3rd-party-users)  
8. [Login Page Setup](#8-login-page-setup)  
9. [Comments Feature](#9-comments-feature)  
10. [Additional Documentation & Diagram](#10-additional-documentation--diagram)

---

## 1. Tech Stack Justification

* **Backend:** Django + Django REST Framework  
  * Provides a robust, secure, and scalable API for handling forum posts, users, and authentication.  

* **Database:** PostgreSQL  
  * Relational database ideal for structured data such as users, posts, likes, comments, and roles.  

* **Frontend:** React  
  * Fast and responsive UI.  
  * Seamless integration with Django REST API.  

* **API Testing:** Postman  
  * Enables third-party developers to interact with the API independently of the frontend.

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

Frontend will run on:

http://localhost:3000

4. How to Run the Project (macOS)
Step 1: Run the Backend

Open Terminal and navigate to the backend folder:

cd dbInStoreForumBackend

Activate the virtual environment:

source venv/bin/activate

Run the Django server:

python manage.py runserver

Backend will be available at:

http://127.0.0.1:8000/

Step 2: Open a Second Terminal

Open a new terminal window.

Navigate again to the backend folder:

cd dbInStoreForumBackend

Activate the virtual environment again:

source venv/bin/activate
Step 3: Run the Frontend

From the second terminal:

cd frontend
npm start

Frontend will be available at:

http://localhost:3000/

Important

Backend must be running before starting the frontend.

Keep both terminal windows open while using the application.

5. Load Dummy Data

Populate the database with pre-created users, posts, and moderators:

python manage.py loaddata forum/dummy_data.json

Ensure dummy_data.json exists inside:

/forum/

and is committed to the repository.

6. Create Moderators Manually (Optional)
python manage.py shell

Then inside the shell:

from forum.models import tUsers
user = tUsers.objects.get(sEmail="mod@gmail.com")
user.sRole = "moderator"
user.save()
7. Public API for 3rd-Party Users

The API allows developers to interact with the forum without using the frontend.

7.1 Ensure Backend is Running
python manage.py runserver
7.2 Install Postman

Download Postman and use it to send HTTP requests to:

http://127.0.0.1:8000/

7.3 Create Postman Collection

Click New → Collection

Name it: Forum Public API

Save

7.4 Example API Requests
Register

POST
http://127.0.0.1:8000/api/register/

Headers:

Content-Type: application/json

Body:

{
  "username": "yourusername",
  "password": "yourpassword"
}
Login

POST
http://127.0.0.1:8000/api/login/

Body:

{
  "username": "yourusername",
  "password": "yourpassword"
}

Response returns a token.

Get Posts

GET
http://127.0.0.1:8000/api/posts/

Headers:

Authorization: Token YOUR_TOKEN
Create Post

POST
http://127.0.0.1:8000/api/posts/

Headers:

Authorization: Token YOUR_TOKEN
Content-Type: application/json

Body:

{
  "sTitle": "Post from Postman",
  "sContent": "External app created this"
}
Like Post

POST
http://127.0.0.1:8000/api/posts/<POST_ID>/like/

Headers:

Authorization: Token YOUR_TOKEN
Comment Post

POST
http://127.0.0.1:8000/api/posts/<POST_ID>/comments/

Body:

{
  "sContent": "Your comment here"
}
Flag Post (Moderator Only)

PATCH
http://127.0.0.1:8000/api/posts/<POST_ID>/flag/

Body:

{
  "bFlaggedMisleading": true
}
7.5 Export Postman Collection

Right-click Forum Public API

Click Export

Choose Collection v2.1

Save as:

ForumPublicAPI.postman_collection.json

Upload it to GitHub.

8. Login Page Setup

The login page includes:

Application logo

Company name displayed prominently

Example:

InStoreForum AI

9. Comments Feature

Comments are collapsible on the frontend.

Default display:

View Comments ▼

Click to expand comments

Click again to hide comments

10. Additional Documentation & Diagram

Project Diagram:
https://viewer.diagrams.net/?tags=%7B%7D&lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Untitled%20Diagram.drawio&dark=auto#Uhttps%3A%2F%2Fraw.githubusercontent.com%2Fksandile%2FdbInStoreForumBackend%2Fmain%2FUntitled%2520Diagram.drawio

Project Documentation / Specs:
https://docs.google.com/document/d/1lQilOWOf6zLZh84O7D1t_nnjqi4Cq3UEombg5DWVYvs/edit?usp=sharing
