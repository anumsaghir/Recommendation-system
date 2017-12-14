from models import get_db
db= get_db()
res=db.execute('select * from similarities where movie_id_1=111351 or movie_id_2=111351 order by similarity_index desc limit 10')
i = 0
rec_count = 10
for r in res:
    i += 1
    if(r[0]!= 111351):
        print(r[0],r[2])
    else:
        print(r[1],r[2])
    
    
   




