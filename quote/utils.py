import json
import requests
from json import JSONEncoder


class MyEncoder(JSONEncoder):
    def default(self, obj):
        return obj.__dict__    

class Movie():
    def __init__(self, id, imdb_id, original_title, overview, poster_path, release_date, title, genres):
        self.id = id
        self.imdb_id = imdb_id
        self.original_title = original_title
        self.overview = overview
        self.poster_path = poster_path
        self.release_date = release_date
        self.title = title
        self.genres = genres


def get_tmdb_movie(id):
    url = f'https://api.themoviedb.org/3/movie/{id}?api_key=cde21e835ed34679a10746ce57a3ec54'
    response = requests.get(url=url)
    movie=serializer_tmdb_movie(json.loads(response.content))
    return movie

def serializer_tmdb_movie(movie):
    _movie = Movie(movie['id'],movie['imdb_id'],movie['original_title'],movie['overview'],movie['poster_path'],movie['release_date'],movie['title'],movie['genres'])
    return _movie.__dict__