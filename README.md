# Movie Explorer


This web app is built on flask a python web framework for microservices.
Following are the tools and technologies used in this web app
- TMDB API for fetching the movies 
- Wikipedia API for fetching the wiki articles about the movie
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
  
## Issues I faced when working on this project

- I faced issue while fetching the data from wikipedia as it throws an error if movie not found, so I fix this issue by appending (film) at the end of movie name.
- Fetching the poster Image from TMDB as we need to append the domain url, so I faced difficulties by fetching the base domain url for images