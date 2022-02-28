import os
from dotenv import load_dotenv

load_dotenv()
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    TMDB_APIKEY = os.getenv('TMDB_APIKEY')

