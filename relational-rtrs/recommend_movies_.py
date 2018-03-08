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
    RATING_SIMILARITY_WEIGHT = 0.2

    def __init__(self):
        """
        Constructor - create database connection
        """
        self.db = get_db()

    def get_movie_recommendation_pool(self, pool_size):
        """
        Get a pool of movies that are similar based on Title, genres and tags (ToDo)
        """

        print(" - Getting movies recommendation pool")

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

    def get_ratings_similarity(self):
        """
        Get ratings similarity between movies in the movie recommendation pool and the
        target movie.
        """

        # Get average rating of the target movie
        query_1 = "SELECT AVG(rating) FROM ratings WHERE movie_id=%i" % self.target_movie.movie_id
        res = self.db.execute(query_1).fetchall()
        target_movie_average_rating = res[0][0]

        pmids = []
        for rm in self.recommendation_pool:
            pmids.append(rm[0].movie_id)

        # rating_similarity dict contains movie_ids as keys and difference in rating as value
        self.rating_similarity = {}
        query_2 = """
        SELECT movie_id, ABS(({tmr} - AVG(rating))) as rating_difference
        FROM ratings r
        WHERE movie_id IN ({pool_movie_ids})
        GROUP BY movie_id
        """.format(
            tmr=target_movie_average_rating,
            pool_movie_ids=str(pmids)[1:-1]
        )
        print(query_2)

        res = self.db.execute(query_2).fetchall()
        for rec in res:
            self.rating_similarity[rec[0]] = rec[1]

    def recommend(self, target_movie_id, num_recommendations):
        """
        Recommend movies that are similar to target_movie_id.
        """
        

        print(" - Getting target movie record")
        self.target_movie = self.db.query(Movie).filter_by(movie_id=target_movie_id).first()
        assert self.target_movie is not None

        self.get_movie_recommendation_pool(num_recommendations * 10)
        self.get_ratings_similarity()
        
        self.final_ratings = {}
        for r in self.recommendation_pool:
            # r[0] is the movie object, so r[0].movie_id gives you the movie ID
            # r[1] contains the rating similarity value
            pool_movie_id = r[0].movie_id
            similarity = r[1] 

            # self.rating_similarity[pool_movie_id]
            self.final_ratings[pool_movie_id] = similarity - (self.rating_similarity.get(pool_movie_id, 2.5) * self.RATING_SIMILARITY_WEIGHT)
        
            print(self.final_ratings)



 # """def print_recommendations(self):
  #      """
   #     Print the recommended movies nicely
    #    """

     #   print("Title: {}, Genres: {}".format(self.target_movie.title, self.target_movie.genres))
      #  print("="*100)

       # for rp in self.recommendation_pool:
        #    print("Movie: %s - Genres: %s - Similarity: %f" % (rp[0].title, rp[0].genres, rp[1]))

        #print("-"*100)
        #print(self.rating_similarity)
        #print(self.final_ratings)
        #print("-"*100) 


    def print_recommendations(self):
        """
        Print the recommended movies nicely
        """
        print("Title: {}, Genres: {}".format(self.target_movie.title, self.target_movie.genres))
        print("="*100)

        # print(type(self.final_ratings))
        # print(self.final_ratings)

        # for rp in self.final_ratings:
        for k,v in self.final_ratings.items():
            # print("Movie: %s - Genres: %s - Similarity: %f" % (rp[0].title, rp[0].genres, rp[1]))
            # print(type(rp))
            # print(rp)
            # print("Movie: %s - Genres: %s - Similarity: %f" % (rp[0].title, rp[0].genres, 'test'))
            m = self.db.query(Movie).filter_by(movie_id=k).first()
            # print("Movie: %s - Genres: %s - Similarity: %f").format(k, v, 'test'))

            print("Movie: {} - Genres: {} - Similarity: {}".format(m.title, m.genres, v))

        # for k,v in self.final_ratings.items():
            # print(k,"=",v)

        print("-"*100)
        print(self.rating_similarity)
        print(self.final_ratings)
        print("-"*100) 

if '__main__' == __name__:

    if len(sys.argv) != 2:
        print("Usage %s movie_id" % sys.argv[0])
        sys.exit(1)

    movie_id = int(sys.argv[1])

    R = RecommendationEngine()
    R.recommend(movie_id, 10)
    R.print_recommendations()
