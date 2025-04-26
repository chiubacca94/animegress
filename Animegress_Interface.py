from Sqlite_Interface import Sqlite_Interface

class AnimegressInterface:

    # sqlite_interface = Sqlite_Interface()

    def __init__(self):
        pass

    def echo_anime(self, anime_name, total_episodes, watched_episodes):
        if total_episodes < 0:
            raise ValueError("Total episodes cannot be negative.")
        if watched_episodes < 0:
            raise ValueError("Watched episodes cannot be negative.")
        if watched_episodes > total_episodes:
            raise ValueError("Watched episodes cannot exceed total episodes.")
    
        return f"Anime: {anime_name}, Total Episodes: {total_episodes}, Watched Episodes: {watched_episodes}"

    def add_anime(self, anime_name, total_episodes, watched_episodes):
        if total_episodes < 0:
            raise ValueError("Total episodes cannot be negative.")
        
        self.sqlite_interface.add_anime(anime_name, total_episodes, 0)

