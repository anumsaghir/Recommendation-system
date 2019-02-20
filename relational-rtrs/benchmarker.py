"""
Recommandation speed benchmarker.

Run multiple recommendations to more accurately judge recommendation speed.

benchmarker.py 100 25
"""

import sys
import time
import random

from models import Movie, get_db
from recommender import RecommendationEngine


def find_movie_recommendations(title, n_r):
    R = RecommendationEngine()
    R.set_target_movie(title)
    R.number_of_recommendations = n_r

    if not R.target_movie:
        print("Error: could not find target movie")
        sys.exit(1)

    print("{R.movie_id} - {R.title} - {R.genres}".format(R=R.target_movie))
    R.get_title_similarity()
    R.get_genre_similarity()
    R.trim_recommendation_pool(n_r*10)
    # R.get_ratings_similarity()
    R.get_tags_similarity()
    R.update_recommendation_pool()
    R.show_recommendation_pool()


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("%s number_of_movies num_recommendations" % sys.argv[0])
        sys.exit(1)

    random.seed()
    recommendation_times = []
    target_movies = []
    record_numbers = []
    num_movies = int(sys.argv[1])
    num_recommendations = int(sys.argv[2])

    db = get_db()
    res = db.execute("select count(*) from movies").fetchall()
    total_records = res[0][0]
    print("Total movies: %i" % total_records)

    while len(record_numbers) < num_movies:
        rec_pos = random.randint(0, total_records-1)
        if rec_pos not in record_numbers:
            record_numbers.append(rec_pos)

    print("randomly selected record positions: %r" % record_numbers)

    for rn in record_numbers:
        q = "select * from movies limit %i, 1" % rn
        res = db.execute(q).fetchall()
        target_movies.append(res[0])

    print("Target movies selected for recommendation")
    for tm in target_movies:
        print(tm[0], tm[1], tm[2])

    print("\n")

    for tm in target_movies:
        movie_title = tm[1]
        print("\n:> Trying to find recommendations for: %i - %s" % (tm[0], tm[1]))
        ts = time.time()
        find_movie_recommendations(movie_title, num_recommendations)
        te = time.time()
        time_elapsed = te-ts
        print('recommendation took %2.2f seconds' % time_elapsed)
        recommendation_times.append(time_elapsed)

    print("\n\n ====================== Benchmark done ====================")
    print("Total recommendation actions: %i" % num_movies)
    print("Fastest recommendation time: %2.2f seconds" %
          min(recommendation_times))
    print("Slowest recommendation time: %2.2f seconds" %
          max(recommendation_times))
    average_time = sum(recommendation_times) / num_movies
    print("Average recommendation time: %2.2f seconds" % average_time)
    print("Total time: %2.2f seconds" % sum(recommendation_times))
    print("=============================================================")
