"""
To Fatch Records
"""

"""
To print Title
"""

from models import Movie, get_db 
db= get_db()
movies= db.query(Movie).limit(10)
for movie in movies:             
   ...:     print(movie.title)


"""
To Print movie ID
"""

from models import Movie, get_db 
db= get_db()
movies= db.query(Movie).limit(10)
for movie in movies:             
   ...:     print(movie.movie_id)
