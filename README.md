# Full Stack Forum Project – README

## Table of Contents

1. [Tech Stack Justification](#1-tech-stack-justification)  
2. [Setup Backend](#2-setup-backend)  
3. [Setup Frontend](#3-setup-frontend)  
4. [Run Backend Server](#4-run-backend-server)  
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
  * Relational DB ideal for structured data such as users, posts, and roles.  
* **Frontend:** React  
  * Fast, responsive UI for forum users.  
  * Easy integration with Django REST API.  
* **API Testing:** Postman  
  * Allows external developers to interact with the API without using the frontend.

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
macOS / Linux / Windows
cd frontend
npm install
npm start

Frontend runs at: http://localhost:3000

4. Run Backend Server
macOS / Linux
source venv/bin/activate
python manage.py runserver
Windows
venv\Scripts\activate
python manage.py runserver

API will be live at: http://127.0.0.1:8000/

5. Load Dummy Data

Populate the database with pre-created users, posts, and moderators:

python manage.py loaddata forum/dummy_data.json

✅ Ensure dummy_data.json exists in /forum/ and is committed to the repo.

6. Create Moderators Manually (Optional)
python manage.py shell

Then in Python shell:

from forum.models import tUsers
user = tUsers.objects.get(sEmail="mod@gmail.com")
user.sRole = "moderator"
user.save()
7. Public API for 3rd-Party Users

The API allows developers to interact with the forum without the frontend.

7.1 Ensure Backend is Running

Activate backend virtual environment.

Run python manage.py runserver.

7.2 Install Postman

Download Postman (Catalina-compatible for macOS if needed).

Postman sends HTTP requests to your API and receives JSON responses.

7.3 Create Postman Collection

Click New → Collection

Name: Forum Public API

Save. This collection will store all API requests.

7.4 Example Requests
Register

Method: POST

URL: http://127.0.0.1:8000/api/register/

Headers: Content-Type: application/json

Body (JSON):

{
  "username": "yourusername",
  "password": "yourpassword"
}
Login

Method: POST

URL: http://127.0.0.1:8000/api/login/

Headers: Content-Type: application/json

Body (JSON):

{
  "username": "yourusername",
  "password": "yourpassword"
}

Response contains token used for authenticated requests.

Get Posts

Method: GET

URL: http://127.0.0.1:8000/api/posts/

Headers: Authorization: Token YOUR_TOKEN

Create Post

Method: POST

URL: http://127.0.0.1:8000/api/posts/

Headers:

Authorization: Token YOUR_TOKEN

Content-Type: application/json

Body (JSON):

{
  "sTitle": "Post from Postman",
  "sContent": "External app created this"
}
Like Post

Method: POST

URL: http://127.0.0.1:8000/api/posts/<POST_ID>/like/

Headers: Authorization: Token YOUR_TOKEN

Body: empty

Response shows updated like count

Comment Post

Method: POST

URL: http://127.0.0.1:8000/api/posts/<POST_ID>/comments/

Headers:

Authorization: Token YOUR_TOKEN

Content-Type: application/json

Body (JSON):

{
  "sContent": "Your comment here"
}
Flag Post

Method: PATCH

URL: http://127.0.0.1:8000/api/posts/<POST_ID>/flag/

Headers: Authorization: Token YOUR_TOKEN

Body (JSON):

{
  "bFlaggedMisleading": true
}
7.5 Export Postman Collection

Right-click Forum Public API → Export

Choose Collection v2.1

Save as ForumPublicAPI.postman_collection.json

Upload it to GitHub and provide link in section 10 below.

8. Login Page Setup

Add Logo and Company Name:

Example: InStoreForum AI

Login page should be styled with the logo at top and company name prominently displayed above the login form.

9. Comments Feature

Comments are collapsible on the frontend.

Default view shows: View Comments ▼

Click → expands comments

Click again → hides comments

10. Additional Documentation & Diagram

Project Diagram: [Insert Diagram Link Here](https://viewer.diagrams.net/?tags=%7B%7D&lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Untitled%20Diagram.drawio&dark=auto#Uhttps%3A%2F%2Fraw.githubusercontent.com%2Fksandile%2FdbInStoreForumBackend%2Fmain%2FUntitled%2520Diagram.drawio)


Project Documentation / Specs: [Insert Doc Link Here](https://docs.google.com/document/d/1lQilOWOf6zLZh84O7D1t_nnjqi4Cq3UEombg5DWVYvs/edit?usp=sharing)

