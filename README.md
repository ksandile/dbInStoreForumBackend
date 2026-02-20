# How To Run Backend For macOS 10.15.8

#### Activate the virtual enviroment(macOS):
source venv/bin/activate

Your terminal will change to: (venv) cash@Nicole dbInStoreForumBackend %

#### Then type the below default Python 2:
python manage.py runserver

# How to Run FrontEnd On macOS

First Add A New Terminal.

#### Then type the below command to navigate to Frontnend folder:
cd frontend
Then your terminal will look like: (venv) cash@Nicole frontend %

#### Then to start the application type:
npm start


# How to create moderators manually.

### Use Django shell
python manage.py shell

Then write: from forum.models import tUsers
            user = tUsers.objects.get(sMail="mod@gmail.com)
            user.sRole = "moderator"
            user.save()



# PUBLIC API FOR 3RD-PARTY USERS — EXPLANATION

The goal is to allow external developers to interact with my forum system without using my React frontend. This is done by exposing my Django REST API.

## 1. Ensure Django API is Running
1.1 Open terminal in vscode
1.2 Navigate to my backend folder by typing: cd dbInStoreForumBackend
1.3 Activate virtual enviroment by typing: 
source venv/bin/activate  (Linux/macOS)
or
venv\Scripts\activate     (Windows)
1.4 Run the server by typing: python manage.py runserver

API will now be live at: http://127.0.0.1:8000/

## 2. Install Postman.
2.1 Download the Postman Desktop App (Catalina-compatible version).
2.2 Open Postman.
2.3 Postman acts like a 3rd-party application: it sends requests to your API and receives JSON responses.

## 3. Create a Postman Collection.
3.1 Click New → Collection
3.2 Name it:
Forum Public API
3.3 Save - (this will hold all API requests: Register, Login, Get Posts, Create Post.)

## 4. Add Requests
4.1 Register

Method: POST

URL:

http://127.0.0.1:8000/api/register/

Headers:

Content-Type: application/json

Body → raw → JSON:

{
  "username": "yourusername",
  "password": "yourpassword"
}

Click Send → you should get a success message or user ID.

4.2 Login

Method: POST

URL:

http://127.0.0.1:8000/api/login/

Headers:

Content-Type: application/json

Body → raw → JSON:

{
  "username": "yourusername",
  "password": "yourpassword"
}

Click Send → you will receive a Token:

{
  "token": "abc123xyz"
}

This token is needed for authenticated requests (Get Posts, Create Post).

4.3 Get Posts

Method: GET

URL:

http://127.0.0.1:8000/api/posts/

Headers:

Authorization: Token YOUR_TOKEN

Click Send → you should get all posts as JSON.

4.4 Create Post

Method: POST

URL:

http://127.0.0.1:8000/api/posts/

Headers:

Authorization: Token YOUR_TOKEN
Content-Type: application/json

Body → raw → JSON:

{
  "sTitle": "Post from Postman",
  "sContent": "External app created this"
}

Click Send - new post is created and saved in PostgreSQL.

## 5. Export Postman Collection

5.1 Right-click Forum Public API → Export

5.2 Choose Collection v2.1

5.3 Save as:

ForumPublicAPI.postman_collection.json

This is submission-ready Postman collection.






















