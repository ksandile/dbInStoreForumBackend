# Full Stack Forum Project – README

## Table of Contents

1. [Tech Stack Justification](#1-tech-stack-justification)
2. [Setup Backend](#2-setup-backend)
3. [Setup Frontend](#3-setup-frontend)
4. [Run Backend Server](#4-run-backend-server)
5. [Load Dummy Data](#5-load-dummy-data)
6. [Create Moderators Manually (Optional)](#6-create-moderators-manually-optional)
7. [Public API for 3rd-Party Users](#7-public-api-for-3rd-party-users)

---

## 1. Tech Stack Justification

* **Backend:** Django + Django REST Framework

  * Provides a robust, secure, and scalable API for handling forum posts, users, and authentication.
* **Database:** PostgreSQL (or SQLite for testing)

  * Relational DB is ideal for structured data such as users, posts, and roles.
* **Frontend:** React

  * Fast, responsive UI for forum users.
  * Easy integration with Django REST API.
* **API Testing:** Postman

  * Allows external developers to interact with the API without using the frontend.

---

## 2. Setup Backend

### macOS / Linux

```bash
# Navigate to backend folder
cd dbInStoreForumBackend

# Activate virtual environment
source venv/bin/activate

# Install dependencies (if not done yet)
pip install -r requirements.txt
```

### Windows

```bash
# Navigate to backend folder
cd dbInStoreForumBackend

# Activate virtual environment
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

---

## 3. Setup Frontend

### macOS / Linux / Windows

```bash
# Open a new terminal and navigate to frontend folder
cd frontend

# Install dependencies (if not done yet)
npm install

# Start frontend development server
npm start
```

The frontend will run at: `http://localhost:3000`

---

## 4. Run Backend Server

### macOS / Linux

```bash
# Ensure virtual environment is activated
source venv/bin/activate

# Run Django server
python manage.py runserver
```

### Windows

```bash
venv\Scripts\activate
python manage.py runserver
```

API will be live at: `http://127.0.0.1:8000/`

---

## 5. Load Dummy Data

This will populate the database with pre-created users and moderators.

```bash
python manage.py loaddata forum/dummy_data.json
```

✅ Make sure the file `dummy_data.json` exists in `/forum/` and is committed to the repo.

---

## 6. Create Moderators Manually (Optional)

```bash
python manage.py shell
```

Then:

```python
from forum.models import tUsers
user = tUsers.objects.get(sEmail="mod@gmail.com")
user.sRole = "moderator"
user.save()
```

---

## 7. Public API for 3rd-Party Users

The API allows developers to interact with the forum without the frontend.

### 7.1 Ensure Django API is running

1. Activate backend virtual environment.
2. Run `python manage.py runserver`.

### 7.2 Install Postman

* Download Postman (Catalina-compatible for macOS if needed).
* Postman sends HTTP requests to your API and receives JSON responses.

### 7.3 Create Postman Collection

* Click **New → Collection**
* Name: `Forum Public API`
* Save. This collection will store all API requests.

### 7.4 Example Requests

#### Register

* **Method:** POST
* **URL:** `http://127.0.0.1:8000/api/register/`
* **Headers:** `Content-Type: application/json`
* **Body (JSON):**

```json
{
  "username": "yourusername",
  "password": "yourpassword"
}
```

#### Login

* **Method:** POST
* **URL:** `http://127.0.0.1:8000/api/login/`
* **Headers:** `Content-Type: application/json`
* **Body (JSON):**

```json
{
  "username": "yourusername",
  "password": "yourpassword"
}
```

* Response contains `token` used for authenticated requests.

#### Get Posts

* **Method:** GET
* **URL:** `http://127.0.0.1:8000/api/posts/`
* **Headers:** `Authorization: Token YOUR_TOKEN`

#### Create Post

* **Method:** POST
* **URL:** `http://127.0.0.1:8000/api/posts/`
* **Headers:**

  * `Authorization: Token YOUR_TOKEN`
  * `Content-Type: application/json`
* **Body (JSON):**

```json
{
  "sTitle": "Post from Postman",
  "sContent": "External app created this"
}
```

### 7.5 Export Postman Collection

1. Right-click `Forum Public API` → **Export**
2. Choose **Collection v2.1**
3. Save as `ForumPublicAPI.postman_collection.json`

This file is **submission-ready**.
