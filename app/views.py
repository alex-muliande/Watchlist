from flask import render_template
from app import app

#Views
@app.route('/movie/<int:movie_id>')
def movie(movie_id):
    '''
    View movie page function that returns the index page and its data
    '''
    message = 'Hello Alex'
    return render_template('index.html',message = message)