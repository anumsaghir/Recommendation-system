# Recommendation-system
Real-Time Recommendation Final year Project

" i want to do some changes in my Recommendation system"

## Implementations

Recommendation system will be implemented using 3 methods

1. Traditional relational database based using MySQL and Python
2. cKNN based using hadoop for distributed processing
3. Graph database based using ArangoDB

## For Dataset:

you can download the dataset from the link below:
http://files.grouplens.org/datasets/movielens/ml-20m.zip

and discription of dataset:
https://grouplens.org/datasets/movielens/

## Memory Notes

All solutions are optimized for using 4GB of memory to keep consistent results.
MySQL (Relational) and ArangoDB (Graph) configuration file samples provided
with the code are optimized for 4GB.

## Dataset Stats

From the sample dataset we only use data for movies, ratings and tags. The
number of entries/records for each are:


| Item      | Record count |
|-----------|-------------:|
| Movies    | 58098        |
| Ratings   | 27753444     |
| Tags      | 324370       |


## Recommendation Algorithm

Same recommendation methodology is used for all 3 approaches to ensure that
there is no bias within the implementations.

* Select movies based on similarity between movie title and genres and score the title and genre similarity.
* Add similarity score from movie ratings. Ratings given by users that have rated target movie have more weight.
* For target movie find all users that have given tags for the movie and then find all movies that the same users have tagged. Then calculate the tags similarity value.
* Top n movies with the highest combined simillarity index are recommended.
