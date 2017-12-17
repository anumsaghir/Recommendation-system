import sys
from models import Movie, Similarity, get_db

if len(sys.argv) != 2:
    print("Usage %s movie_id" % sys.argv[0])
    sys.exit(1)

movie_id = int(sys.argv[1])

db= get_db()
res = db.query(Movie).filter_by(movie_id=111351).first()
print(res.title)

i = 0
rec_count = 10      
for r in res:
    i += 1
    if(r[0]!= movie_id):
        m = db.query(Movie).filter_by(movie_id=r[0]).first()
    else:
        m = db.query(Movie).filter_by(movie_id=r[1]).first()

    print("Movie: %s similarity: %f" % (m.title, r[2]))
