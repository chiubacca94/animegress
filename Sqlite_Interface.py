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

    def add_anime(self, anime_name, total_episodes, watched_episodes):
        self.cursor.execute("INSERT INTO anime (anime_name, total_episodes, watched_episodes) VALUES (?, ?, ?)",
                            (anime_name, total_episodes, watched_episodes))
        self.sqlite_interface.add_anime(anime_name, total_episodes, 0)

