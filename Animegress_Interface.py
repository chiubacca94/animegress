from Sqlite_Interface import Sqlite_Interface

class AnimegressInterface:

    def __init__(self):
        self.sqlite_interface = Sqlite_Interface()
        pass
#-----------------------------------------------------------------------

    def echo_anime(self, anime_name, total_episodes, watched_episodes):
        if total_episodes < 0:
            raise ValueError("Total episodes cannot be negative.")
        if watched_episodes < 0:
            raise ValueError("Watched episodes cannot be negative.")
        if watched_episodes > total_episodes:
            raise ValueError("Watched episodes cannot exceed total episodes.")
    
        return f"Anime: {anime_name}, Total Episodes: {total_episodes}, Watched Episodes: {watched_episodes}"

#-----------------------------------------------------------------------

#add the anime to the DB
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
            return(anime_name + "is not added")


#-----------------------------------------------------------------------    
#updates the anime with how many episodes you've watched
    def update_anime(self, anime_name, watched_episodes):
        if not self.sqlite_interface.anime_exists(anime_name):
            return False

        updated = self.sqlite_interface.update_anime(anime_name, watched_episodes)
        if updated == True:
            return(anime_name + " is now updated and you've now watched" + str(watched_episodes) + "episodes")
        else:
            return (anime_name + "is not updated")


#-----------------------------------------------------------------------
#deletes the anime
    def delete_anime(self, anime_name):
        Doesanimeexist = self.sqlite_interface.anime_exists(anime_name)
        if Doesanimeexist == False:
            print("Anime doesnt exist")
        
        deleteanime = self.sqlite_interface.delete_anime(anime_name)
        if deleteanime:
            return(anime_name + " is now deleted")
        else:
            return(anime_name + "cant be deleted")


#-----------------------------------------------------------------------
#returns what % the anime is at right now
    def anime_progress(self, anime_name):
        progress = self.sqlite_interface.anime_progress(anime_name)
        percentage = (progress["watched"]/progress["total"]) 
        return (f'{percentage:.0%}')


#-----------------------------------------------------------------------
#returns if anime is completed or not
    def anime_completed(self, anime_name):
        completion = self.sqlite_interface.anime_progress(anime_name)
        
        if (completion["watched"]) == (completion["total"]):
            return ("This anime is fully completed")
        else:
            return ("this anime is not complete")

#-----------------------------------------------------------------------
# list animes in the table
    def anime_titles(self):
        anime_list = self.sqlite_interface.getallanimes()

        if not anime_list:
            print("You are not watching any anime yet.")
            return
       
        print("You are watching the following: ", end="")

        for i in range(len(anime_list)):
            if i == 0:
                print (anime_list[i] ,end="")
            elif i == (len(anime_list) - 1 ):
                print(f", and {anime_list[i]}", end="")
            else:
                print(f", {anime_list[i]}", end="")


#-----------------------------------------------------------------------
    def anime_real(self, anime_name):
        Doesanimeexist = self.sqlite_interface.anime_exists(anime_name)
        if not Doesanimeexist:
                print("Anime doesn't exist.")
                return False
        return True

