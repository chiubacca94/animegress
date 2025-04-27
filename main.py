from Animegress_Interface import AnimegressInterface

anime = AnimegressInterface()


while True:

    print("What would you like to do?")
    print("1. Add a new anime")
    print("2. Update existing anime")

    choice = input("Pick 1 to add or 2 to update:")


    match choice:
            case "1":
                anime_name = input("Enter the anime name: ")
                total_episodes = int(input("Enter the total number of episodes: "))
                watched_episodes = int(input("Enter the number of episodes you have watched: "))

                this_anime = anime.add_anime(anime_name, total_episodes, watched_episodes)   
                print("Anime shown successfully.")
                print(this_anime)

            case "2":
               anime_name = input("Enter the anime name: ")
               watched_episodes = int(input("Enter the number of episodes you have watched: "))
               updated_anime = anime.update_anime(anime_name,watched_episodes)
               print("anime updated sucessfully")
               print(updated_anime)

            case default:
                print("use 1 or 2 punk ass bitch")


    continue_choice = input("Do you want to continue adding anime? (Y/N): ")
    if continue_choice != ("Y"):
        print("no more anime added")
        break