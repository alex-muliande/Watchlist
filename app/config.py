class Config:

       MOVIE_API_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key={}'



class ProdConfig(Config):
     MOVIE_API_KEY = 'c87923da94b6cb0b665d3f7d1f84efe3'
   

class DevConfig(Config):
    DEBUG = True