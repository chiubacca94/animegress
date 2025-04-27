import sqlite3
class Sqlite_Interface:
   
    def __init__(self):
        self.con = sqlite3.connect("animegress.db")
        self.cursor = self.con.cursor()

        if not self.check_table_exists():
            self.create_table()
   
    def check_table_exists(self):
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='anime'")
        return self.cursor.fetchone() is not None

    def create_table(self):
        self.cursor.execute("""
                       CREATE TABLE anime(
                       anime_name TEXT,
                       total_episodes INTEGER,
                       watched_episodes INTEGER
                       )
                    """ 
                    )
        
    def add_anime(self, anime_name, total_episodes, watched_episodes):
        self.cursor.execute("INSERT INTO anime (anime_name, total_episodes, watched_episodes) VALUES (?, ?, ?)",
                            (anime_name, total_episodes, watched_episodes))
        self.con.commit()
        return True

    def anime_exists(self, anime_name):
        self.cursor.execute("SELECT 1 FROM anime WHERE anime_name = ?", (anime_name,))
        return self.cursor.fetchone() is not None 
       
    def update_anime(self, anime_name, watched_episodes):

        if not self.anime_exists(anime_name):
            return False 

        self.cursor.execute(
            "UPDATE anime SET watched_episodes = ? WHERE anime_name = ?",
            (watched_episodes, anime_name)
        )
        self.con.commit()
        return True
    
    def delete_anime(self, anime_name):

        if not self.anime_exists(anime_name):
            return False

        self.cursor.execute(
            "DELETE FROM anime WHERE anime_name = ?",
            (anime_name,)
        )
        self.con.commit()
        return True