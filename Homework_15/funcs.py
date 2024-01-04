
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

def display_film_info(film):
    print("Інформація про фільм:")
    exclude = ['gen', 'more_like_this', 'keywords', 'type']
    for key, value in film.items():
        if key not in exclude:
            print(f"{key}: {value}")
    print()

def print_border():
    print("--------------------")
