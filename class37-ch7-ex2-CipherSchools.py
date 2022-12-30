#Word_counter using dictionary

user = {}
name = input("Enter your name:")
age = input("Enter your age:")
fav_movies = input("Enter your fav movies:").split(',')
fav_songs = input("Enter your fav songs:" ).split(',')

user["name"] = name
user["age"] = age
user["fav_movies"] = fav_movies
user["fav_songs"] = fav_songs

for key,value in user.items():
    print(f"{key}:{value}")