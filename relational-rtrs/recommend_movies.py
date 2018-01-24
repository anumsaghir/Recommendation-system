import sys
from models import Movie, Similarity, get_db


class RecommendationEngine(object):
    """
    Relational database based recommendation engine. Recommendation algorithm steps:

    1. Fetch number of recommendations * 10 records based on title, genres and tags similarity
    2. Find rating similarity for these records with the target movie
    3. List top number of recommendations records that are closest match
    """

    TITLE_SIMILARITY_WEIGHT = 1.0
    GENRES_SIMILARITY_WEIGHT = 0.4

    def __init__(self):
        """
        Constructor - create database connection
        """
        self.db = get_db()

    def recommend(self, target_movie_id, num_recommendations):
        """
        Recommend movies that are similar to target_movie_id.
        """

        self.target_movie = self.db.query(Movie).filter_by(movie_id=target_movie_id).first()
        assert self.target_movie is not None

    def get_movie_recommendation_pool(self, pool_size):
        """
        Get a pool of movies that are similar based on Title, genres and tags (ToDo)
        """

        query = """
        SELECT movie_id_1, movie_id_2, 
            ((title_similarity_index * {tw}) + (genres_similarity_index * {gw})) as similarity
        FROM similarities
        WHERE movie_id_1={movie_id} OR movie_id_2={movie_id}
        ORDER BY similarity DESC LIMIT {pool_size}
        """.format(
            tw=self.TITLE_SIMILARITY_WEIGHT,
            gw=self.GENRES_SIMILARITY_WEIGHT,
            movie_id=self.target_movie.movie_id,
            pool_size=pool_size
        )

        res = self.db.execute(query)

        # recommendation pool list contains elements of form [movie_record, similarity_value]
        self.recommendation_pool = []

        for r in res:
            if r[0] != self.target_movie.movie_id:
                m = self.db.query(Movie).filter_by(movie_id=r[0]).first()
            else:
                m = self.db.query(Movie).filter_by(movie_id=r[1]).first()

            self.recommendation_pool.append([m, r[2]])

    def print_recommendations(self):
        """
        Print the recommended movies nicely
        """

        print("Title: {}, Genres: {}".format(self.target_movie.title, self.target_movie.genres))
        print("="*100)

        for rp in self.recommendation_pool:
            print("Movie: %s - Genres: %s - Similarity: %f" % (rp[0].title, rp[0].genres, rp[1]))

        print("-"*100)


if '__main__' == __name__:

    if len(sys.argv) != 2:
        print("Usage %s movie_id" % sys.argv[0])
        sys.exit(1)

    movie_id = int(sys.argv[1])

    R = RecommendationEngine()
    R.recommend(movie_id, 10)
    R.print_recommendations()
