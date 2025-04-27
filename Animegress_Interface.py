from Sqlite_Interface import Sqlite_Interface

class AnimegressInterface:

    def __init__(self):
        self.sqlite_interface = Sqlite_Interface()
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
        
        Doesanimeexist = self.sqlite_interface.anime_exists(anime_name)
        if Doesanimeexist == True:
            raise ValueError("Anime already exists")
        
        results = self.sqlite_interface.add_anime(anime_name, total_episodes, watched_episodes)
        if results == True:  
            return(anime_name + " added sucessfully")
        else:
            return(anime_name + " not added")
        
    def update_anime(self, anime_name, watched_episodes):
        if not self.sqlite_interface.anime_exists(anime_name):
                return False

        updated = self.sqlite_interface.update_anime(anime_name, watched_episodes)
        if updated == True:
            return(anime_name + " is now updated and you've now watched" + str(watched_episodes) + "episodes")
        else:
            return (anime_name + "not updated")

    def delete_anime(self, anime_name):
        Doesanimeexist = self.sqlite_interface.anime_exists(anime_name)
        if Doesanimeexist == False:
            raise ValueError("Anime doesnt exist")
        
        deleteanime = self.sqlite_interface.delete_anime(anime_name)
        if deleteanime:
            return(anime_name + " is now deleted")
        else:
            return(anime_name + "cant be deleted")
        

# when called, 