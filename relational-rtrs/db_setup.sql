DROP TABLE IF EXITS movies;
create table movies(
    movie_id int unsigned not null primary key,
    title varchar(500) not null,
    genres varchar(300)
);
DROP TABLE IF EXITS tags;
create table tags(
    user_id int not null, 
    movie_id int not null,
    tags varchar(500) not null,
    timestamp int unsigned not null,
    PRIMARY KEY(user_id, movie_id)
);
DROP TABLE IF EXITS links;
create table links(
    movie_id int unsigned not null primary key,
    imdbid int not null,
    tmdbid int not null
);
DROP TABLE IF EXITS genome_scores;
create table genome_scores(
    movie_id int not null,
    tag_id int not null,
    relevance float not null,
    PRIMARY KEY(movie_id, tag_id)
);
DROP TABLE IF EXITS genome_tags;
create table genome_tags(
    tag_id int not null primary key,
    tag varchar(500) not null
);
DROP TABLE IF EXITS rating;
create table ratings(
    user_id int not null, 
    movie_id int not null, 
    rating float not null, 
    timestamp int unsigned not null, 
    PRIMARY KEY(user_id, movie_id)
); 


