
"""
To Fatch Records
"""

from models import Movie, get_db
from similarity import jaccard_index 
from models import Similarity
db= get_db()
movies= db.query(Movie).limit(10).all()
i = 0

for movie in movies:
    i += 1
    
    for second_movie in movies[i:]:
        print(movie.title)
        print("    %s" % second_movie.title)
        from similarity import jaccard_index
        s_val = jaccard_index(movie.title, second_movie.title)
        print(s_val)
        from models import Similarity
        r=Similarity()
        r.movie_id_1=movie.movie_id
        r.movie_id_2=second_movie.movie_id
        r.similarity_index=s_val
        db.add(r)
        db.commit()

