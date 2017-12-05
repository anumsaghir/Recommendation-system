
"""
To Fatch Records
"""

from models import Movie, get_db 
db= get_db()
movies= db.query(Movie).limit(10).all()
i = 0

for movie in movies:
    i += 1
    
    for second_movie in movies[i:]:
        print(movie.title)
        print("    %s" % second_movie.title)

