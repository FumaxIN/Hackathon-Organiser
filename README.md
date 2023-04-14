# Hackathon Organiser

Backend design for creatiion, enrollment and submission of Hackathons built on Django-Rest-Framework 


### Features

* User authentication and JWT Tokenisation.
* SSL protocol.
* Hackathon creation by staff members.
* Hacktons listing. Already started hackathons aren't included in the list.
* Users can enroll to a particular Hackathon.
* Submission based on submission_type specified in Hackathon's detail. User has to first enroll and then submit.
* List of enrollments and submissions by user.

## Requirements

* [Python](https://www.python.org/downloads/) 3.8 or above
* [pip](https://pip.pypa.io/en/stable/installing/) 20.1 or above
* [Django](https://pypi.org/project/Django/)
* [Django-Rest-Framework](https://pypi.org/project/djangorestframework/k)
* [DJ-Rest-Auth](https://pypi.org/project/dj-rest-auth/)
* [SimpleJWT](https://pypi.org/project/djangorestframework-simplejwt/)
* [Django-Allauth](https://pypi.org/project/django-allauth/)
* [Django-SSL-Serevr](https://pypi.org/project/django-sslserver/)
* [MySQL Client](https://pypi.org/project/mysqlclient/)

## Running

After succefully installing the above dependencies, proceed to the below instructions.
Firstly login to mySql and create a database with name `hackathon`.
Now, navigate to `socialMedia > settings.py`and edit the `NAME`, `USER` and `PASSWORD` in `DATABASES` section to match with your data.

Next step is to perform migrations, i.e. giving structure to the Database to incorprate all the fields required to store data.
Navigate to the main folder, and run the following instruction in console/terminal.
To dig and update last N no of tweets,

```shell
python manage.py make migrations
python manage.py migrate
```

Finally, its time to run the Server.
To dig and update last N no of tweets,

```shell
python manage.py runsslserver
```

## Endpoints

`dj-rest-auth/signup` to create account.
`dj-rest-auth/login` to login.
(Hackathons can only be created by Staff Users)

`api/hackathons` to get the list of upcoming hackathons. Expired or started hackathons won't be listed.

`api/hackathons/<int:hackathonID>/enrol/` to enroll in a particular Hackathon. User need to supply 'mail'.

`api/enrollments/` to get the list of enrollments by the current logged in user. 

`api/hackathons/<int:hackathonID>/submission/` submission as per the submission_type of Hackathon. User has to enrol first

`api/submissions/` to get the list of submissions by the current logged in user.

