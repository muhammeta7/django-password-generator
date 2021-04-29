# django-password-generator

### Why Django?
* **Ridiculously fast:** Designed to help developers take applications from concept to completion as quickly as possible.<br />
  [Docs](https://docs.djangoproject.com/en/3.1/intro/overview/)
* **Reassuringly Secure:** Very secure and helps developers avoid common security mistakes.<br />
  [Docs](https://docs.djangoproject.com/en/3.1/topics/security/)
* **Exceedingly scalable:** Busiest sites on the web leverage ability to quickly and flexibly scale.<br />
  [Docs](https://docs.djangoproject.com/en/3.1/faq/general/#does-django-scale)

### Getting Started
* `pip install django` installs Django.
* `django-admin --version` checks to see whether Django is installed.
* `django-admin startproject project_name` creates a new Django project.
* `python manage.py startapp appname` to create apps withing your project.
* `python manage.py runserver` will run the server for your project.<br /><br />
project: *describes a Django web application and all it’s parts.*<br />
app: *refers to a submodule of a project, and it is reusable, so you can use it within other projects without modifications.*<br /> 


### Files & Details
* **urls** creates paths for routing for when users navigate throughout your app.
* **templates** Generates HTML dynamically. Usually contains static and dynamic HTML. Similar to Jinja
Django has a template search path, which allows you to minimize redundancy among templates.
* **manage.py:** runs server, not meant to be edited
* password_generator project folder
    * asgi/wsgi used for deploying your apps
* **settings.py:** includes apps, points code to html templates, and database configurations.


### Project & Apps
The project itself contains apps which are just creating modularity within your Django project.<br />
* `python manage.py startapp appname` within your project directory to create a new app
* Once you create an app, make sure to go to **settings.py** to add your new app to the INSTALLED_APPS list

