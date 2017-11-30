"""
To Fatch Records
"""

from models import Movie, get_db 
db= get_db()
movies= db.query(Movie).limit(10)
for movie in movies:             
print(movie.movie_id)
