import os
import string
from awards import films_awards

for data in films_awards:
    results = data.get('results', [])

    sorted_results = sorted(results, key=lambda x: x['award_name'])

    for film_data in sorted_results:
        movie_data = film_data.get('movie', {})
        film_title = movie_data.get('title')

        cleaned_title = film_title.replace(':', '')

        film_title_dir = os.path.join("Harry Potter", cleaned_title)
        os.makedirs(film_title_dir, exist_ok=True)

        for letter in string.ascii_uppercase:
            letter_dir = os.path.join(film_title_dir, letter)
            os.makedirs(letter_dir, exist_ok=True)

        award_name = film_data.get('award_name')
        award = film_data.get('award')

        first_letter = award_name[0].upper()

        letter_dir = os.path.join(film_title_dir, first_letter)

        award_file_path = os.path.join(letter_dir, f"{award_name}.txt")
        if not os.path.exists(award_file_path):
            with open(award_file_path, 'a', encoding='utf-8') as file:
                file.write(f"{award}\n")
        else:
            with open(award_file_path, 'r', encoding='utf-8') as file:
                content = file.read().splitlines()

            if award not in content:
                with open(award_file_path, 'a', encoding='utf-8') as file:
                    file.write(f"{award}\n")