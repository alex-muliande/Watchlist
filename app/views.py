from flask import render_template
from app import app

# Views
@app.route('/movie/<int:movie_id>')
def movie(movie_id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    return render_template('movie.html',id = movie_id)
def index():
    '''
    View root page function that returns the index page and its data
    '''

    title = 'Home - welcome to the best movie Review website Online'
    return render_template('insex.html', title = title) 