from Animegress_Interface import AnimegressInterface

anime = AnimegressInterface()


while True:

    print("\nWhat would you like to do?")
    print("1. Add a new anime")
    print("2. Update existing anime")
    print("3. Delete an anime")

    choice = input("Pick 1 to add or 2 to update or 3 to delete:").strip()
  

    match choice:
            case "1":
                anime_name = input("Enter the anime name: ").strip

                try:    
                    total_episodes = int(input("Enter the total number of episodes: "))
                    watched_episodes = int(input("Enter the number of episodes you have watched: "))
                except ValueError:
                    print("total episodes must be numbers")
                    continue
                
                if total_episodes < 0 or watched_episodes < 0:
                    print("cant be less than 0")

                if watched_episodes > total_episodes:
                    print("cant be more than total episodes watched")

                this_anime = anime.add_anime(anime_name, total_episodes, watched_episodes) 

                print("Anime shown successfully.")
                print(this_anime)

            case "2":
               anime_name = input("Enter the anime name: ")
               watched_episodes = int(input("Enter the number of episodes you have watched: "))
               updated_anime = anime.update_anime(anime_name,watched_episodes)
               print("anime updated sucessfully")
               print(updated_anime)

            case "3":
                anime_name = input("Enter the anime name: ")
                deleteanime = anime.delete_anime(anime_name)
                print("anime deleted")
                print(deleteanime)

            case default:
                print("use 1 or 2 or 3 punk ass bitch")


    continue_choice = input("Do you want to continue adding anime? (Y/N): ")
    if continue_choice != ("y"):
        print("no more anime added")
        break

