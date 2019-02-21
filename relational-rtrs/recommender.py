"""
Movie Recommender.

Recommend movies similar to provided movie name.
"""

import sys
# from pprint import pprint
from collections import OrderedDict
from sqlalchemy import or_  # pylint: disable=E0401
from models import Movie, get_db


def jaccard_index(s1, s2, sep=' '):
    """Find similarity between 2 strings using jaccard."""
    set1 = set(s1.split(sep))
    set2 = set(s2.split(sep))

    intersection_cardinality = len(set.intersection(set1, set2))
    union_cardinality = len(set.union(set1, set2))

    return intersection_cardinality/float(union_cardinality)


def tags_jaccard_index(d1, d2):
    """Find jaccard similarity between 2 dicts of tags with their counts."""
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

    final_tag_similarity = ((common_tags_count / all_tags_count) * 10) \
        * tags_similarity

    return final_tag_similarity


def string_cleanup(s, garbage=":,-()&"):
    """Clean string by removing characters present in garbage list."""
    s_new = ''
    for x in s:
        if x not in garbage:
            s_new += x

    return s_new


class RecommendationEngine(object):
    """
    Relational database based recommendation engine.

    Recommendation algorithm steps:

    1. Fetch number of recommendations * 10 records based on title,
       genres and tags similarity
    2. List top number of recommendations records that are closest match
    """

    TITLE_SIMILARITY_WEIGHT = 1.0
    GENRES_SIMILARITY_WEIGHT = 0.3
    TAGS_SIMILARITY_WEIGHT = 0.4

    def __init__(self):
        """Create recommendation engine."""
        self.db = get_db()
        self.target_movie = None
        self.number_of_recommendations = 10
        self.recommendation_pool = OrderedDict({})

    def set_target_movie(self, movie_title):
        """Set target movie by searching by movie title."""
        self.target_movie = self.db.query(Movie).filter_by(
            title=movie_title).first()

    def trim_recommendation_pool(self, n):
        """
        Trim reccommendation pool.

        Keeping only top n movies by final_similarity score.
        """
        # {k:v for k, v in list(d.items())[:2]}
        self.recommendation_pool = {
            k: v for k, v in list(self.recommendation_pool.items())[:n]}

    def update_recommendation_pool(self):
        """Update overall similarity index of recommendation pool."""
        for k in self.recommendation_pool.keys():
            self.recommendation_pool[k]['final_similarity'] = 0.0

            if 'title_similarity' in self.recommendation_pool[k]:
                self.recommendation_pool[k]['final_similarity'] += \
                    self.recommendation_pool[k]['title_similarity']

            if 'genres_similarity' in self.recommendation_pool[k]:
                self.recommendation_pool[k]['final_similarity'] += \
                    self.recommendation_pool[k]['genres_similarity']

            if 'tags_similarity' in self.recommendation_pool[k]:
                self.recommendation_pool[k]['final_similarity'] += \
                    self.recommendation_pool[k]['tags_similarity']

        self.recommendation_pool = OrderedDict(
            sorted(
                self.recommendation_pool.items(),
                key=lambda x: x[1]['final_similarity'],
                reverse=True
            )
        )

    def show_recommendation_pool(self, top_n=None):
        """Print the recommendation pool in a friendly way."""
        i = 0
        if top_n is None:
            top_n = self.number_of_recommendations

        for _, rdata in self.recommendation_pool.items():
            print("\n{R.movie_id} - {R.title} - {R.genres}".format(
                R=rdata['movie_obj']))

            if 'title_similarity' in rdata:
                print("  Title Similarity: {} - ({})".format(
                    rdata['title_similarity'], rdata['movie_obj'].title))

            if 'genres_similarity' in rdata:
                print("  Genres Similarity: {} - ({})".format(
                    rdata['genres_similarity'], rdata['movie_obj'].genres))

            if 'tags_similarity' in rdata:
                print("  Tags Similarity: {} - ({})".format(
                    rdata['tags_similarity'], rdata['tags']))

            if 'final_similarity' in rdata:
                print(" -> Final Similarity: {}".format(
                    rdata['final_similarity']))

            i += 1
            if top_n and i >= top_n:
                break

    def get_title_similarity(self):
        """Fetch movies that are similar in title."""
        title_words = []
        ignore_words = ['the', 'and', 'or', 'to', 'at', 'on', 'of']
        for w in self.target_movie.title.split(' '):
            w = w.strip('- ,:(){}[]')
            if w.lower() not in ignore_words:
                title_words.append(w)

        # if last word is a number then it's an year and should be ignored.
        if len(title_words) > 1 and title_words[-1].isdigit():
            title_words = title_words[:-1]

        print(title_words)
        res = self.db.query(Movie).filter(
            Movie.movie_id != self.target_movie.movie_id).filter(or_(
                Movie.title.ilike(r'%' + tw + r'%') for tw in title_words
            )).all()

        target_clean_title = string_cleanup(self.target_movie.title)

        print("%i records from partial title match" % len(res))
        TSW = self.TITLE_SIMILARITY_WEIGHT
        for rec in res:
            mc_title = string_cleanup(rec.title)
            smid = rec.movie_id
            if smid not in self.recommendation_pool:
                self.recommendation_pool[smid] = {
                    'movie_obj': rec,
                    'title_similarity': jaccard_index(
                        target_clean_title, mc_title, ' ') * TSW
                }

            else:
                self.recommendation_pool[smid]['title_similarity'] = \
                    jaccard_index(
                        target_clean_title, mc_title, ' ') * TSW

    def get_genre_similarity(self):
        """Fetch movies that are similar in genre."""
        genre_words = []
        for w in self.target_movie.genres.split('|'):
            w = w.strip('- ,:(){}[]')
            genre_words.append(w)

        print(genre_words)

        res = self.db.query(Movie).filter(
            Movie.movie_id != self.target_movie.movie_id).filter(
                Movie.movie_id.in_(self.recommendation_pool.keys())
            ).filter(or_(
                Movie.genres.ilike(r'%' + gw + r'%') for gw in genre_words
            )).all()

        print("%i records from partial genres match" % len(res))
        GSW = self.GENRES_SIMILARITY_WEIGHT
        for rec in res:
            smid = rec.movie_id
            self.recommendation_pool[smid]['genres_similarity'] = \
                jaccard_index(self.target_movie.genres, rec.genres, '|') * GSW

    def get_tags_similarity(self):
        """Get tags similarity."""
        target_movie_tags = self.get_tags_count(self.target_movie.movie_id)
        print("GTS: target_movie_tags: %r" % target_movie_tags)

        tags_similarity = {}

        users_query = "select distinct user_id from tags where movie_id=%i" % \
                      self.target_movie.movie_id
        user_records = self.db.execute(users_query).fetchall()
        user_ids = [u[0] for u in user_records]
        print("GTS: %i users have tagged this movie"
              % len(user_ids))

        rmids = list(self.recommendation_pool.keys())
        if len(user_ids) == 0 or len(rmids) == 0:
            return tags_similarity

        movie_ids_query = """
            SELECT distinct movie_id
            FROM tags
            WHERE movie_id IN (%s)
            AND user_id IN (%s)
        """ % (str(rmids)[1:-1], str(user_ids)[1:-1])
        res = self.db.execute(movie_ids_query).fetchall()

        print("GTS: Same users have tagged %i movies from top %i movies" %
              (len(res), len(rmids)) +
              " in the recommendation pool")

        TSW = self.TAGS_SIMILARITY_WEIGHT
        for rec in res:
            movie_id = rec[0]
            movie_tags = self.get_tags_count(movie_id)

            # Since we only process tags for movies in the recommendation
            # pool; we won't have cases where movie record is not already
            # present in the recommendation pool.
            self.recommendation_pool[movie_id]['tags_similarity'] = \
                tags_jaccard_index(target_movie_tags, movie_tags) * TSW
            self.recommendation_pool[movie_id]['tags'] = movie_tags

        return tags_similarity

    def get_tags_count(self, m_id, u_id=None):
        """
        Get aggregate tags count for a movie.

        Get overall tags count for given movie and optionally only by a
        single user.
        """
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

        # print(tags_occured)

        return tags_occured


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('%s "movie title" number_of_recommendations' % sys.argv[0])
        sys.exit(1)

    title = sys.argv[1]
    num_recommendations = int(sys.argv[2])

    R = RecommendationEngine()
    R.set_target_movie(title)
    R.number_of_recommendations = num_recommendations

    if not R.target_movie:
        print("Error: could not find target movie")
        sys.exit(1)

    print("{R.movie_id} - {R.title} - {R.genres}".format(R=R.target_movie))
    R.get_title_similarity()
    R.get_genre_similarity()
    R.trim_recommendation_pool(num_recommendations*10)
    R.get_tags_similarity()
    R.update_recommendation_pool()
    R.show_recommendation_pool()
