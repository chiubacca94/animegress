import sqlite3
class Sqlite_Interface:
   
    def __init__(self):
        self.con = sqlite3.connect("animegress.db")
        self.cursor = self.con.cursor()

        if not self.check_table_exists():
            self.create_table()
   
#-----------------------------------------------------------------------
   #check if a table is there 
    def check_table_exists(self):
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='anime'")
        return self.cursor.fetchone() is not None

#-----------------------------------------------------------------------
    #create a table 
    def create_table(self):
        self.cursor.execute("""
                       CREATE TABLE anime(
                       anime_name TEXT,
                       total_episodes INTEGER,
                       watched_episodes INTEGER
                       )
                    """ 
                    )

#-----------------------------------------------------------------------        
        #add anime 
    def add_anime(self, anime_name, total_episodes, watched_episodes):
        self.cursor.execute("INSERT INTO anime (anime_name, total_episodes, watched_episodes) VALUES (?, ?, ?)",
                            (anime_name, total_episodes, watched_episodes))
        self.con.commit()
        return True

#-----------------------------------------------------------------------
    #does this anime exist? if so,  check it.  
    def anime_exists(self, anime_name):
        self.cursor.execute("SELECT 1 FROM anime WHERE anime_name = ?", (anime_name,))
        return self.cursor.fetchone() is not None
         
       
#-----------------------------------------------------------------------
    #update an anime on the table 
    def update_anime(self, anime_name, watched_episodes):

        if not self.anime_exists(anime_name):
            return False 

        self.cursor.execute(
            "UPDATE anime SET watched_episodes = ? WHERE anime_name = ?",
            (watched_episodes, anime_name)
        )
        self.con.commit()
        return True
    

#-----------------------------------------------------------------------
    #delete the anime 
    def delete_anime(self, anime_name):

        if not self.anime_exists(anime_name):
            return False

        self.cursor.execute(
            "DELETE FROM anime WHERE anime_name = ?",
            (anime_name,)
        )
        self.con.commit()
        return True
    
#-----------------------------------------------------------------------
    #get anime progress % 
    def anime_progress(self, anime_name):

        if not self.anime_exists(anime_name):
            return "anime not found"
           
        self.cursor.execute(
            "SELECT total_episodes, watched_episodes FROM anime WHERE anime_name = ?",
            (anime_name,)
        )
        self.con.commit()
        result = self.cursor.fetchone()
        total_episodes, watched_episodes = result 
        return {"total": total_episodes, "watched": watched_episodes}
    

#-----------------------------------------------------------------------
    #get all anime names 
    def getallanimes(self):
        self.cursor.execute(
            "Select anime_name from anime"
        )
        result = self.cursor.fetchall()
        list = [row[0] for row in result]

    #    anime_name = result
    #    return {"anime name": anime_name}
        return(list)
    

     