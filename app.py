import json
import logging
import random
from . import create_app
import requests
from requests.exceptions import ConnectionError
import wikipedia

from config import Config
from flask import url_for, request, render_template, flash

app = create_app(Config)


def get_data_from_tmdb(tmdb_id):
    try:
        tmdb_url = f'https://api.themoviedb.org/3/movie/{tmdb_id}?api_key={app.config.get("TMDB_APIKEY")}'
        response = requests.get(tmdb_url)
        if response.status_code == 200:
            response_data = json.loads(response.content)
            genre_list = [genre_dict['name'] for genre_dict in response_data['genres']]
            return {'title': response_data['title'],
                    'overview': response_data['overview'],
                    'genre': ",".join(genre_list),
                    'image_url': f'https://image.tmdb.org/t/p/original/'
                                 f'{response_data["backdrop_path"]}'
                    }
    except ConnectionError:
        logging.error('Error connecting with TMDB!')

@app.route('/')
def home():
    """
    This route will display the movie detail
    :return:
    """
    tmdb_id_list = ['24428', '141052', '157336']
    tmdb_id = random.choice(tmdb_id_list)
    movie_data = get_data_from_tmdb(tmdb_id)
    movie_data['wikipedia_url'] = wikipedia.page(title=f"{movie_data['title']}(film)", auto_suggest=True,
                                                 redirect=True, preload=False)

    return render_template('index.html', **movie_data)


if __name__ == '__main__':
    app.run(template_folder='templates')
