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
    print("\n")
  

    match choice:
            case "1": #add a new anime
                anime_name = input("Enter the anime name: ").strip()

                try:    
                    total_episodes = int(input("Enter the total number of episodes: "))
                    watched_episodes = int(input("Enter the number of episodes you have watched: "))
                except ValueError:
                    print("Total episodes must be numbers.")
                    continue
                
                if total_episodes < 0 or watched_episodes < 0:
                    print("Total episodes can't be less than 0.")
                    continue

                if watched_episodes > total_episodes:
                    print("Watched episodes can't be more than total episodes.")
                    continue

                this_anime = anime.add_anime(anime_name, total_episodes, watched_episodes) 

                print("Anime shown successfully.")
                print(this_anime)
                print("\n")

#-----------------------------------------------------------------------

            case "2":  #update an anime 
               anime_name = input("Enter the anime name: ").strip()
               
               if anime.anime_real(anime_name) == False: #check if the anime exists
                    print("Anime not found in database.")
                    continue
               
               try:    
                    watched_episodes = int(input("Enter the number of episodes you have watched: "))
               except ValueError:
                    print("Total episodes must be numbers.")
                    continue
               
               if watched_episodes < 0:
                    print("Watched episodes can't be less than 0.")
                    continue
               
               updated_anime = anime.update_anime(anime_name,watched_episodes)
               print("Anime has updated sucessfully.")
               print("\n")
               
#-----------------------------------------------------------------------

            case "3": #delete an anime
                anime_name = input("Enter the anime name: ").strip()

                if anime.anime_real(anime_name) == False: #check if the anime exists
                    print("Anime not found in database.")
                    continue


                deleteanime = anime.delete_anime(anime_name)
                print("Anime deleted successfully.")
                print("\n")


#-----------------------------------------------------------------------
            case "4": #whats the progress on all anime?
                anime_name = input("Enter the anime name: ").strip()

                if anime.anime_real(anime_name) == False:  #check if the anime exists
                    print("Anime not found in database.")
                    continue

                progressanime = anime.anime_progress(anime_name)
                completedanime = anime.anime_completed(anime_name)
                print (progressanime)
                print (completedanime)
                print("\n")

#-----------------------------------------------------------------------

            case "5":  #print anime name list
                anime.anime_titles()
                print("\n")


#-----------------------------------------------------------------------

            case default:
                print("use numbers punk ass bitch")
                print("\n")

    continue_choice = input("Do you want to continue adding anime? (Y/N): ").strip().lower()
    if continue_choice != ("y"):
        print("No more anime will be added.  Thank you for your time.")
        print("\n")
        break

