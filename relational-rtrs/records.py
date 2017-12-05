"""
To Fatch Records
"""

from models import Movie, get_db 
db= get_db()
<<<<<<< HEAD
movies= db.query(Movie).limit(10)
for movie in movies:             
=======
movies= db.query(Movie).limit(10).all()
i = 0

for movie in movies:
>>>>>>> be0eba4ca53bf0ee1e52fcabd4a6099189bf2ca3
    print(movie.movie_id)
    i += 1
    
    for second_movie in movies[i:]:
        print("    %i" % second_movie.movie_id)

