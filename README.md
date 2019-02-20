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
| Tags      | 324370       |


## Recommendation Algorithm

Same recommendation methodology is used for all 3 approaches to ensure that
there is no bias within the implementations.

1. Split movie title into words.
  a. Ignore the year present at the end of movie title.
  b. Ignore any common words in movie title (in, at, of, the, and, etc).
  c. Fetch all movies where title contains any of the remaining title words.
     This makes up the recommendation pool used for further processing.
  d. Calculate title similarity between the movies.

2. Split genres into words and find all movies in the recommendation pool that
   have at least one genre match with the target movie.
   a. Calculate genre similarity among the results and add to overall movie
      similarity score.

3. For target movie find all users that have given tags for the movie and then
   find all movies within the recommendation pool that the same users have
   tagged. Then calculate the tags similarity value.

4. Top n movies with the highest combined similarity index are recommended.
