import sys
from models import get_db

if len(sys.argv) != 2:
    print("Usage %s movie_id" % sys.argv[0])
    sys.exit(1)

movie_id = int(sys.argv[1])

db= get_db()
res=db.execute('select * from similarities where movie_id_1=%i or movie_id_2=%i order by similarity_index desc limit 10' % (movie_id, movie_id))

i = 0
rec_count = 10
for r in res:
    i += 1
    if(r[0]!= 111351):
        print(r[0],r[2])
    else:
        print(r[1],r[2])

