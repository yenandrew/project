# Movie Explorer


This web app is built on flask a python web framework for microservices.
Following are the tools and technologies used in this web app
- TMDB API for fetching the movies 
- Wikipedia API for fetching the wiki articles about the movie
- Flask-Login provides user session management for Flask. It handles the common tasks of logging in, logging out, and remembering your users’ sessions over extended periods of time
- Flask-SQLAlchemy is an extension for Flask that adds support for SQLAlchemy to your application.
- Boostrap 4 is use in this app to make its html pages to look more attractive


## How to set up movie explorer project?

- First clone the project from git@github.com:csc4350-sp22/project1-ayen4.git
- Create virtual environment (https://docs.python.org/3/library/venv.html)
- Install the dependencies from requirements.txt 
  - pip install -r requirements.txt
- Set up .env  
- run project simply by running the following command
  - python app.py
  - if you want to run using flask run you have to export FLASK_APP=app.py and then run flask run
  - you can also refer to https://flask.palletsprojects.com/en/2.0.x/quickstart/
  
## Issue I faced when working on this project

- Working with Flask Authentication is looks really hard because handling the user state looks really hard in start but As I did some progress things seems very clear to me.
- Working with Flask SQL ALCHEMY is really hard especially when do some changes in the table and it didn't reflect but after do some R&D on it become very easy to work.