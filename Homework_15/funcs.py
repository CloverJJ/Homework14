import csv
import ast

def load_data(file_name):
    with open(file_name, newline='', encoding='utf-8') as csvfile:
        return list(csv.DictReader(csvfile))

def search_by_title(data, title):
    return [film for film in data if title.lower() in film['title'].lower()]

def get_unique_genres_with_counts(data):
    genres_count = {}
    for film in data:
        genres_list = ast.literal_eval(film['gen'])
        for genre in genres_list:
            genres_count[genre['genre']] = genres_count.get(genre['genre'], 0) + 1
    return genres_count

def search_by_genre(data, genre):
    genre = genre.lower()
    return [film for film in data if any(genre == g['genre'].lower() for g in ast.literal_eval(film['gen']))]

def search_by_year(data, year):
    return [film for film in data if film['year'] == year]

def display_film_info(film):
    print("Повна інформація про фільм:")
    exclude = ['gen', 'more_like_this', 'keywords', 'type']
    for key, value in film.items():
        if key not in exclude:
            print(f"{key}: {value}")
    print()

def print_border():
    print("--------------------")

def save_data(file_name, films_data, fieldnames):
    with open(file_name, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        if file.tell() == 0:
            writer.writeheader()

        for film in films_data:
            writer.writerow(film)

def add_new_film(fieldnames):
    new_film = {}
    for field in fieldnames:
        new_value = input(f"Введіть {field}: ")
        new_film[field] = new_value
    return new_film
