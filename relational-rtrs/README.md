# Realtime Recommendation System based on relational databases

This folder contains mysql based real time recommendation system implementation
using python as the programming language.


## Setup

First install mysql:

```bash
sudo apt install mysql-server
```

Follow the instructions and remember the password you set for root. Then secure the installation by
running

```bash
sudo mysql_secure_installation
```

Update the configuration file(s) for mysql so they are optimized.

Make sure mysql is running

```bash
sudo service mysql start
```

Then login into mysql using admin (root)

```bash
sudo mysql -u root -p
```

When asked for password, give password for root that you provided during mysql installation.
After that you're logged into MySQL CLI, create database and user here.

```sql
create database movies_db;
grant all privileges on movies_db.* to anum@localhost identified by 'pakistan';
```

Then press Ctrl+D to exit mysql prompt and confirm that you can login using the new user:

```bash
mysql movies_db -u anum -ppakistan
```

Then press Ctrl+D again to exit

### Loading from an existing database dump

If you have a SQL dump file, you can load data from it using a command like:

```bash
bzcat db_dump.sql.bz2 | mysql -u anum -ppakistan movies_db
```


### Creating tables and loading data from CSV file
Now create tables in the DB by executing the db_setup.sql file against the database.

```bash
mysql movies_db -u anum -ppakistan < db_setup.sql
```
#### For Dataset:

you can download the dataset from the link below:
http://files.grouplens.org/datasets/movielens/ml-20m.zip

and discription of dataset:
https://grouplens.org/datasets/movielens/

After download the dataset, you need to import data from CSV to Sql:

Now to import data:

#### TABLE movies

```bash
LOAD DATA LOCAL INFILE '/home/hduser1/Downloads/ml-20m/movies.csv' INTO TABLE movies FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\r\n' IGNORE 1 ROWS;
```
#### TABLE tags

```bash
LOAD DATA LOCAL INFILE '/home/hduser1/Downloads/ml-20m/tags.csv' INTO TABLE tags FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\r\n' IGNORE 1 ROWS;
```
#### TABLE ratings

```bash
LOAD DATA LOCAL INFILE '/home/hduser1/Downloads/ml-20m/rating.csv' INTO TABLE ratings FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\r\n' IGNORE 1 ROWS;
```
#### TABLE genome_scores

```bash
LOAD DATA LOCAL INFILE '/home/hduser1/Downloads/ml-20m/genome-scores.csv' INTO TABLE genome-scores FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\r\n' IGNORE 1 ROWS;
```
#### TABLE genome_tags

```bash
LOAD DATA LOCAL INFILE '/home/hduser1/Downloads/ml-20m/genome-tags.csv' INTO TABLE genome_tags FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\r\n' IGNORE 1 ROWS;
```
#### TABLE links

```bash
LOAD DATA LOCAL INFILE '/home/hduser1/Downloads/ml-20m/links.csv' INTO TABLE links FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\r\n' IGNORE 1 ROWS;
```

### Creating indexes

For faster lookups, we index most used fields.

```sql
CREATE INDEX movie_titles ON movies(title);
CREATE INDEX movie_genres ON movies(genres);
CREATE INDEX ratings_rating ON ratings(rating);
CREATE INDEX tags_tags ON tags(tags);
```

## Create & Activate a virtual Enviroment:
```bash
source py35env/bin/activate
```
because our project is independent from operating system python version.

## Python to mysql Connectivity:
Need to Install library to access pythom from mysql
```bash
sudo apt install python3-dev
```
```bash
sudo apt-get install libmysqlclient-dev
```
then,
```bash
pip install mysqlclient
```

## Install sqlalchemy:
```bash
pip install sqlalchemy
```
Now to get connectivity to mysql from sqlalchemy

### In Ipython shell:
```bash
from sqlalchemy import create_engine
engine = create_engine('mysql+mysqldb://anum:pakistan@localhost/movies_db')
recs = engine.execute("select * from movies limit 10")
print(recs)
```
### May install another lib:
```bash
pip install pymysql
from sqlalchemy import create_engine
engine = create_engine('mysql+pymysql://anum:pakistan@localhost/movies_db')
recs = engine.execute("select * from movies limit 10")
print(recs)
```
The results are shown in list of lists
"list containing records and each record is a list".

for better solution, we can made class for table.
```bash
Base = declarative_base()


class Movie(Base):
    __tablename__ = 'movies'

    movie_id = Column(Integer, primary_key=True)
    title = Column(Unicode(500))
    genres = Column(Unicode(500))


class Similarity(Base):
    __tablename__ = 'similarities'

    movie_id_1 = Column(Integer, primary_key=True)
    movie_id_2 = Column(Integer, primary_key=True)
    similarity_index = Column(Float)
```
Now we can treat database records as objects.

### For store Results:
we need to store results in a database.
First need to make Table for similarity_index.

3 fields: movie_id_1, movie_id_2, similarity_index

## Calculate similarity between two things (strings, lists, etc):
def jaccard_index(s1, s2):
    set1 = set(s1.split(' '))
    set2 = set(s2.split(' '))

    intersection_cardinality = len(set.intersection(set1, set2))
    union_cardinality = len(set.union(set1, set2))

    return intersection_cardinality/float(union_cardinality)
