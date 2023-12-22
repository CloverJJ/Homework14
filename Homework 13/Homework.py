import os
import json
import csv
from data import ganres, films_data

genres_dict = json.loads(ganres)

main_folder = 'Ganres'
os.makedirs(main_folder, exist_ok=True)

for genre_info in genres_dict['results']:
    genre_name = genre_info['genre']
    genre_folder = os.path.join(main_folder, genre_name)
    os.makedirs(genre_folder, exist_ok=True)

for film in films_data:
    film_title = film['title']
    film_year = film['year']
    film_rating = film['rating']
    film_type = film['type']
    film_genres = ';'.join([genre['genre'] for genre in film['gen']])
    imdb_id = film['imdb_id']

    for genre_info in film['gen']:
        genre_name = genre_info['genre']
        file_path = os.path.join(main_folder, genre_name, f"{genre_name}_films.csv")

        if not os.path.exists(file_path) or imdb_id not in open(file_path).read():
            with open(file_path, 'a', newline='', encoding='utf-8') as csvfile:
                fieldnames = ['IMDb_ID', 'title', 'year', 'rating', 'type', 'genres']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                if os.stat(file_path).st_size == 0:
                    writer.writeheader()

                writer.writerow({
                    'IMDb_ID': imdb_id,
                    'title': film_title,
                    'year': film_year,
                    'rating': film_rating,
                    'type': film_type,
                    'genres': film_genres
                })
