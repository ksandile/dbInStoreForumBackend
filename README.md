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
