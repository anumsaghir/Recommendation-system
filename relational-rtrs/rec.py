from models import Movie,get_db
db= get_db()
res=db.execute('select movie_id, title from movies')
i = 0
rec_count = 0
for r in res:
    i += 1
    print(movie.title)
    for second_movie in res[i:]:
         print(movie.title)
         print("    %s" % second_movie.title)





