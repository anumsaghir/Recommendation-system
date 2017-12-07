
"""
To Fatch Records
"""

from models import Movie, Similarity, get_db
from similarity import jaccard_index

db = get_db()
movies = db.query(Movie).all()

i = 0
rec_count = 0

for movie in movies:
    i += 1
    print(movie.movie_id)

    rec_count = 0
    for second_movie in movies[i:]:
        # print(movie.title)
        # print("    %s" % second_movie.title)
        s_val = jaccard_index(movie.title, second_movie.title)
        # print(s_val)
        r = Similarity()
        r.movie_id_1 = movie.movie_id
        r.movie_id_2 = second_movie.movie_id
        r.similarity_index = s_val
        db.add(r)

        rec_count += 1
        # insert records in a batch of 100 per commit to speed up insertions
        if rec_count % 100 == 0:
            db.commit()

    if rec_count % 100 != 0:
        db.commit()
