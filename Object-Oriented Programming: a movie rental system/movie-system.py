import os
import json

from user import User
def menu():
    username = input("Please Enter your name: ")
    if file_exists(username):
        with open(username,'r') as f:
            json_data = json.load(f)
        user =User.from_json(json_data)

    else :
        user = User(username)
    while 1:
        print("Menu")
        print("1# to add a movie")
        print("2# to see the list of movies")
        print("3# to set a movie as watched")
        print("4# to delete a movie")
        print("5# to see the list of watched movies")
        print("0# to quit")
        choice = int(input("Enter your choice : "))

        if choice == 1:
            name = input("Enter the movie name : ")
            genre = input("Enter the the genre of entered movie : ")
            user.add_movie(name,genre)
        elif choice == 2:
            for movie in user.movies:
                print("Name : {}, Genre : {}, Watched :{}\n".format(movie.name,movie.genre,movie.watched))
        elif choice == 3:
            movie_name = input("Enter the movie name to be set as watched : ")
            user.set_watched(movie_name)
        elif choice == 4:
            movie_name = input("Enter the movie name to be set as watched : ")
            user.delete_movie(movie_name)
        elif choice == 5:
            for movie in user.movies:
                if movie.watched== True:
                    print("Name : {}, Genre : {}, Watched :{}\n".format(movie.name,movie.genre,movie.watched))
        elif choice == 0:
            with open(username,'w') as f:
                json.dump(user.json(),f)
            break














def file_exists(filename):
    return os.path.isfile(filename)











menu()
