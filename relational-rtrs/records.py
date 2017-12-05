"""
To Fatch Records
"""

from models import Movie, get_db 
db= get_db()
movies= db.query(Movie).limit(10).all()
i = 0

for movie in movies:
    print(movie.movie_id)
    i += 1
    
    for second_movie in movies[i:]:
print("    %i" % second_movie.movie_id))

