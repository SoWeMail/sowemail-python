# Create a Django app to send email with SoWeMail API

This tutorial explains how we set up a simple Django app to send an email with the SoWeMail Python SDK and how we deploy our app to Heroku.

## Create a Django project

We first create a project folder.

```bash
$ mkdir hello-sowemail
$ cd hello-sowemail
```

We assume you have created and activated a [virtual environment](https://virtualenv.pypa.io/) (See [venv](https://docs.python.org/3/tutorial/venv.html) for Python 3+) for isolated Python environments.

Run the command below to install Django, Gunicorn (a Python WSGI HTTP server), and SoWeMail Python SDK.

```bash
$ pip install django gunicorn sowemail
```

It's a good practice for Python dependency management. We'll pin the requirements with a file `requirements.pip`.

```bash
$ pip freeze > requirements.pip
```

Run the command below to initialize a Django project.

```bash
$ django-admin startproject hello_sowemail
```

The folder structure should look like this:

```
hello-sowemail
├── hello_sowemail
│   ├── hello_sowemail
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   └── manage.py
└── requirements.pip
```

Let's create a page to generate and send an email to a user when you hit the page.

We first create a file `views.py` and put it under the folder `hello_sowemail/hello_sowemail`. Add the minimum needed code below.

```python
import os

from django.http import HttpResponse

from sowemail import SoWeMailAPIClient
from sowemail.helpers.mail import (From, To, PlainTextContent, HtmlContent, Mail)


def index(request):
    sow_client = SoWeMailAPIClient(
        api_key=os.environ.get('SOWEMAIL_API_KEY'))
    from_email = From('test@example.com')
    to_email = To('test@example.com')
    subject = 'Hello from SoWeMail'
    plain_text_content = PlainTextContent(
        'Simple email sending example using python\'s sowerest library'
    )
    html_content = HtmlContent(
        '<strong>Simple email sending example using python\'s sowerest library</strong>'
    )
    message = Mail(from_email, to_email, subject, plain_text_content, html_content)
    response = sow_client.send(message=message)

    return HttpResponse('Email Sent!')
```

**Note:** Don't forget to change your to email from `test@example.com` to your own email, so that you can see the email you receive.

Now the folder structure should look like this:

```
hello-sowemail
├── hello_sowemail
│   ├── hello_sowemail
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── views.py
│   │   └── wsgi.py
│   └── manage.py
└── requirements.pip
```

Next we open the file `urls.py` in order to add the view we have just created to the Django URL dispatcher.

```python
from django.conf.urls import url
from django.contrib import admin

from .views import index


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^sowemail/', index, name='sowemail'),
]
```

These paths allow the URL `/sowemail/` to send the email.

We also assume that you have set up your development environment with your `SOWEMAIL_API_KEY`. If you have not done it yet, please do so. See the section [Setup Environment Variables](https://github.com/sowemail/sowemail-python#setup-environment-variables).

Now we should be able to send an email. Let's run our Django development server to test it.

```
$ cd hello_sowemail
$ python manage.py migrate
$ python manage.py runserver
```

By default, it starts the development server at `http://127.0.0.1:8000/`. To test if we can send email or not, go to `http://127.0.0.1:8000/sowemail/`. If it works, we should see the page says "Email Sent!".

**Note:** If you use `test@example.com` as your from email, it's likely to go to your spam folder. To have the emails show up in your inbox, try using an email address at the domain you registered your SoWeMail account.

## Deploy to Heroku

There are different deployment methods we can choose. In this tutorial, we choose to deploy our app using the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli). Therefore, let's install it before we go further.

Once you have the Heroku CLI installed, run the command below to log in to your Heroku account if you haven't already.

```
$ heroku login
```

Before we start the deployment, let's create a Heroku app by running the command below. This tutorial names the Heroku app `hello-sowemail`.

```bash
$ heroku create hello-sowemail
```

**Note:** If you see Heroku reply with "Name is already taken", please add a random string to the end of the name.

We also need to do a couple things:

1. Add `'*'` or your Heroku app domain to `ALLOWED_HOSTS` in the file `settings.py`. It will look like this:
```python
ALLOWED_HOSTS = ['*']
```

2. Add `Procfile` with the code below to declare what commands are run by your application's dynos on the Heroku platform.
```
web: cd hello_sowemail && gunicorn hello_sowemail.wsgi --log-file -
```

The final folder structure looks like this:

```
hello-sowemail
├── hello_sowemail
│   ├── hello_sowemail
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── views.py
│   │   └── wsgi.py
│   └── manage.py
├── Procfile
└── requirements.pip
```

Go to the root folder then initialize a Git repository.

```
$ git init
$ heroku git:remote -a hello-sowemail
```

**Note:** Change `hello-sowemail` to your new Heroku app name you created earlier.

Add your `SOWEMAIL_API_KEY` as one of the Heroku environment variables.

```
$ heroku config:set SOWEMAIL_API_KEY=<YOUR_SOWEMAIL_API_KEY>
```

Since we do not use any static files, we will disable `collectstatic` for this project.

```
$ heroku config:set DISABLE_COLLECTSTATIC=1
```

Commit the code to the repository and deploy it to Heroku using Git.

```
$ git add .
$ git commit -am "Create simple Hello Email Django app using SoWeMail's SDK"
$ git push heroku master
```

After that, let's verify if our app is working or not by accessing the root domain of your Heroku app. You should see the page says "Email Sent!" and on the Activity Feed page in the SoWeMail dashboard, you should see a new feed with the email you set in the code.