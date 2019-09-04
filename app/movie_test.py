import unittest
from models import movie
Movie = movie.movie

class MovieTest(unittest.TestCase):
    '''
    Test class to test the behaviour of the Movie class 
    '''

    def setUp(self):
        '''
        set up method that will run before every Test
        '''