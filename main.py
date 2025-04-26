from Animegress_Interface import AnimegressInterface

anime = AnimegressInterface()
anime_name = "Naruto"
total_episodes = 220    
watched_episodes = 100

this_anime = anime.add_anime(anime_name, total_episodes, watched_episodes)
next_anime = anime.add_anime("Solo Leveling", 24, 0)
print("Anime shown successfully.")
print(this_anime)
print(next_anime)