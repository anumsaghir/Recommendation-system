"""
    def get_tags_similarity(self):
        """
        Get tags similarity between movies in the movie recommendation pool and the
        target movie.
        """

        # Get tags of the target movie
        query_3 = """
        SELECT * FROM tags 
        WHERE user_id IN (select user_id from tags where movie_id={movie_id})
        """.format(
            movie_id = self.target_movie.movie_id,
        );
        res = self.db.execute(query_3).fetchall()
        

        """Target movie all tags"""
        """Tagret movie tagger -> tagged which other movies"""

        if res:
            print("Target movied tagged by these USER:")
            #print("USER_ID    tags")
            users =  []
            for row in res:
                print(row)
                print("{}    {}".format(row[0], row[2]))
                users.append(row[0])

            print("TAGGED WHICH OTHER MOVIES BY TARGET MOVIE TAGGER")        
            #print("USER_ID    movie_id")
            
            self.tags_similarity = {}
            for user in users: 
                query4 = """SELECT * from tags
                WHERE user_id = {user_id} AND 
                movie_id NOT IN ({movie_id})

                """.format(
                    user_id = user,
                    movie_id = self.target_movie.movie_id,
                )
                res1 = self.db.execute(query4).fetchall()
                if res1:
                    for row1 in res1:

                        self.tags_similarity[row[0]] = row[1]
                        #print("{}    {}".format(row1[0], row1[1])) 
    """
