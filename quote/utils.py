import json
import requests
from json import JSONEncoder


class MyEncoder(JSONEncoder):
    def default(self, obj):
        return obj.__dict__


class Movie():
    def __init__(self, tmdb_id, imdb_id, original_title, overview, poster_path, release_date, title, genres):
        self.tmdb_id = tmdb_id
        self.imdb_id = imdb_id
        self.original_title = original_title
        self.overview = overview
        self.poster_path = poster_path
        self.release_date = release_date
        self.title = title
        self.genres = genres



# fetch data from TMDB api.
def get_tmdb_movie(id):
    url = f'https://api.themoviedb.org/3/movie/{id}?api_key=cde21e835ed34679a10746ce57a3ec54'
    response = requests.get(url=url)
    movie = serializer_tmdb_movie(json.loads(response.content))
    return movie


# serilaize the tmdb json to python dictionary.
def serializer_tmdb_movie(movie):
    _movie = Movie(movie['id'], movie['imdb_id'], movie['original_title'], movie['overview'],
                   movie['poster_path'], movie['release_date'], movie['title'], movie['genres'])
    return _movie.__dict__


# fetch data from TMDB api for every quote's movie_id
def get_quote(data):    
    movie_json = get_tmdb_movie(data["movie_id"])     
    data.update(movie_json)
    return data
    # data = data.copy()
   
def get_all_quotes(data):
    for quote in data:
        movie_json = get_tmdb_movie(quote["movie_id"])
        quote.update(movie_json)
    return data
