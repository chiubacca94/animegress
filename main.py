from Animegress_Interface import AnimegressInterface

anime = AnimegressInterface()


while True:

    print("\nWhat would you like to do?")
    print("1. Add a new anime")
    print("2. Update existing anime")
    print("3. Delete an anime")
    print("4. Get anime perctange")
    print("5. print all animes in table")

    choice = input("Pick 1-5 to do something: ").strip()
  

    match choice:
            case "1": #add a new anime
                anime_name = input("Enter the anime name: ").strip()

                try:    
                    total_episodes = int(input("Enter the total number of episodes: "))
                    watched_episodes = int(input("Enter the number of episodes you have watched: "))
                except ValueError:
                    print("total episodes must be numbers")
                    continue
                
                if total_episodes < 0 or watched_episodes < 0:
                    print("cant be less than 0")
                    continue

                if watched_episodes > total_episodes:
                    print("cant be more than total episodes watched")
                    continue

                this_anime = anime.add_anime(anime_name, total_episodes, watched_episodes) 

                print("Anime shown successfully.")
                print(this_anime)

            case "2":  #update an anime 
               anime_name = input("Enter the anime name: ").strip()
               
               try:    
                    watched_episodes = int(input("Enter the number of episodes you have watched: "))
               except ValueError:
                    print("total episodes must be numbers")
                    continue
               
               if watched_episodes < 0:
                    print("cant be less than 0")
                    continue
               
               updated_anime = anime.update_anime(anime_name,watched_episodes)
               print("anime updated sucessfully")
               print(updated_anime)

            case "3": #delete an anime
                anime_name = input("Enter the anime name: ").strip()
                deleteanime = anime.delete_anime(anime_name)
                print("anime deleted")
                print(deleteanime)

            case "4": #whats the progress on all anime?
                anime_name = input("Enter the anime name: ").strip()
                progressanime = anime.anime_progress(anime_name)
                completedanime = anime.anime_completed(anime_name)
                print (progressanime)
                print (completedanime)

            case "5":  #print anime name list
                anime.anime_titles()
                print("\n")

            case default:
                print("use numbers punk ass bitch")


    continue_choice = input("Do you want to continue adding anime? (Y/N): ").strip().lower()
    if continue_choice != ("y"):
        print("no more anime added")
        break

