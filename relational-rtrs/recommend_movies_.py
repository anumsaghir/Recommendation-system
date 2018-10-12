import sys
from pprint import pprint
from collections import OrderedDict
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
    TAGS_SIMILARITY_WEIGHT = 1.0

    def __init__(self):
        """
        Constructor - create database connection
        """
        self.db = get_db()



    def get_tags_count_(self, m_id, u_id=None):

        query = """
        select tags, count(tags) from tags
        where movie_id={movie_id} group by tags
        """.format(movie_id=m_id,)

        if u_id is not None:
            query = """
            select tags, count(tags) from tags
            where movie_id={movie_id} and user_id={user_id}
            group by tags
            """.format(movie_id=m_id, user_id=u_id)

        res = self.db.execute(query).fetchall()

        tags_occured = dict()
        for row in res:
            tags_occured[row[0]] = row[1]

        print(tags_occured)

        return tags_occured

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
        self.recommendation_pool_tags_count = dict()

        for r in res:
            if r[0] != self.target_movie.movie_id:
                m = self.db.query(Movie).filter_by(movie_id=r[0]).first()
            else:
                m = self.db.query(Movie).filter_by(movie_id=r[1]).first()
            self.recommendation_pool_tags_count[m.movie_id] = self.get_tags_count_(m.movie_id)

            self.recommendation_pool.append([m, r[2]])

        print('self.recommendation_pool_tags_count')
        print(self.recommendation_pool_tags_count)
        print('self.recommendation_pool_tags_count')

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

        res = self.db.execute(query_2).fetchall()
        for rec in res:
            self.rating_similarity[rec[0]] = rec[1]

    def tags_jaccard_index(self, d1, d2):

        set1 = set(d1.keys())
        set2 = set(d2.keys())

        common_tags = set.intersection(set1, set2)
        common_tags_count = 0
        all_tags_count = sum(d1.values()) + sum(d2.values())

        for k, v in d1.items():
            if k in common_tags:
                common_tags_count += v

        for k, v in d2.items():
            if k in common_tags:
                common_tags_count += v

        intersection_cardinality = len(set.intersection(set1, set2))
        union_cardinality = len(set.union(set1, set2))

        tags_similarity = intersection_cardinality/float(union_cardinality)

        final_tag_similarity = ((common_tags_count / all_tags_count) * 10) * tags_similarity

        return(final_tag_similarity)

    def get_tags_similarity(self):
        """
        Get tags similarity between movies in the movie recommendation pool and
        the target movie.
        """

        target_movie_tags = self.get_tags_count_(self.target_movie.movie_id)
        print("get_tags_similarity: target_movie_tags: %r" % target_movie_tags)

        tags_similarity = {}

        users_query = "select distinct user_id from tags where movie_id=%i" % \
                      self.target_movie.movie_id
        user_records = self.db.execute(users_query).fetchall()
        print("get_tags_similarity: %i users have tagged this movie"
              % len(user_records))

        for urec in user_records:
            user_id = urec[0]
            print("get_tags_similarity: Processing user: %i" % user_id)

            movie_ids_query = """
                SELECT distinct movie_id
                FROM tags
                WHERE movie_id != %i
                AND user_id=%i
            """ % (self.target_movie.movie_id, user_id)
            res = self.db.execute(movie_ids_query).fetchall()

            print("get_tags_similarity: User has tagget %i movies" % len(res))
            if res:
                for mid_rec in res:
                    movie_id = mid_rec[0]
                    print(
                        "get_tags_similarity: -> Processing movie: %i" %
                        movie_id
                    )

                    movie_tags = self.get_tags_count_(movie_id, user_id)
                    tags_similarity[movie_id] = self.tags_jaccard_index(
                                target_movie_tags, movie_tags)

        return tags_similarity

    def recommend(self, target_movie_id, num_recommendations):
        """
        Recommend movies that are similar to target_movie_id.
        """


        print(" - Getting target movie record")
        self.target_movie = self.db.query(Movie).filter_by(movie_id=target_movie_id).first()
        assert self.target_movie is not None

        self.get_movie_recommendation_pool(num_recommendations * 10)
        self.get_ratings_similarity()
        tags_similarity = self.get_tags_similarity()
        print(" ** TAGS SIMILARITY **")
        print(tags_similarity)

        self.final_ratings = {}
        for r in self.recommendation_pool:
            # r[0] is the movie object, so r[0].movie_id gives you the movie ID
            # r[1] contains the rating similarity value
            pool_movie_id = r[0].movie_id
            similarity = r[1]

            # self.rating_similarity[pool_movie_id]
            self.final_ratings[pool_movie_id] = similarity - (self.rating_similarity.get(pool_movie_id, 2.5) * self.RATING_SIMILARITY_WEIGHT)

            # tags similarity addition to final ratings
            for m_id, tag_similarity in tags_similarity.items():
                if m_id not in self.final_ratings:
                    self.final_ratings[m_id] = 0.0

                self.final_ratings[m_id] += tag_similarity * self.TAGS_SIMILARITY_WEIGHT

    def sort_ratings(self):
        self.final_ratings = OrderedDict(sorted(self.final_ratings.items(), key=lambda kv: kv[1], reverse=True))


    def print_recommendations(self, n=10):
        """
        Print the top n recommended movies nicely
        """
        print("Title: {}, Genres: {}".format(self.target_movie.title, self.target_movie.genres))
        print("="*120)

        r_count = 0
        print('{} {} {}'.format('Similarity'.ljust(12), 'Movie'.ljust(60), 'Genres'))
        print('-'*120)
        for k, v in self.final_ratings.items():
            m = self.db.query(Movie).filter_by(movie_id=k).first()

            print('{} {} {}'.format(str(round(v, 5)).ljust(12), m.title.ljust(60), m.genres))
            r_count += 1
            if r_count > n:
                break


if '__main__' == __name__:

    if len(sys.argv) != 2:
        print("Usage %s movie_id" % sys.argv[0])
        sys.exit(1)

    movie_id = int(sys.argv[1])

    R = RecommendationEngine()
    tags_count = R.get_tags_count_(movie_id)
    print("tags_count")
    print(tags_count)
    print("tags_count")
    for tag, count in tags_count.items():
        print(tag+'    '+str(count))

    R.recommend(movie_id, 10)
    R.sort_ratings()
    R.print_recommendations(10)
