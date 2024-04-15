# Introduction

The aim of this project is to provide a movie list display and display the details of the movie and be able to filter the list based on name. 

Template is written with django 5.0.4 and python 3 in mind.

![Default Home View](__screenshots/image.png?raw=true "Title")

![Detail View](__screenshots/image_2.png?raw=true "Title")

![Admin View](__screenshots/image_3.png?raw=true "Title")

# Getting Started

First clone the repository from Bitbucket and switch to the new directory:

    $ git clone git@bitbucket.org:irfanmaulana126/movie_list.git
    $ cd {{ project_name }}
    
Activate the virtualenv for your project.
    
Install project dependencies:

    $ pip install -r requirements/local.txt
    
    
Then simply apply the migrations:

    $ python manage.py migrate
    

You can now run the development server:

    $ python manage.py runserver

You can login admin panel with url and account:

    (http://127.0.0.1:8000/admin/)
    username : core
    password : qweasd