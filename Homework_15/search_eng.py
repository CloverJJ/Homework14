from funcs import (
    load_data,
    search_by_title,
    get_unique_genres_with_counts,
    search_by_genre,
    display_film_info,
    print_border
)

def main():
    file_name = 'films.csv'
    films_data = load_data(file_name)

    print_border()
    print("Оберіть режим пошуку:")
    print("1. Пошук за назвою")
    print("2. Пошук за жанром")
    print_border()

    mode_choice = input("Введіть номер режиму: ")

    if mode_choice == '1':
        title_query = input("Введіть назву фільму: ")
        title_results = search_by_title(films_data, title_query)
        if title_results:
            print_border()
            print("Результати пошуку за назвою:")
            for idx, film in enumerate(title_results, start=1):
                print(f"{idx}. {film['title']} ({film['year']})")
            print_border()

            choice = input("Оберіть номер фільму або 'exit' для виходу: ")
            if choice.isdigit():
                choice = int(choice)
                if 1 <= choice <= len(title_results):
                    display_film_info(title_results[choice - 1])
                else:
                    print("Номер фільму введено некоректно, будь ласка, вкажіть коректний номер фільму.")
            elif choice.lower() == 'exit':
                return
            else:
                print("Введено некоректні дані.")
        else:
            print("Фільм не знайдено.")

    elif mode_choice == '2':
        genres_with_counts = get_unique_genres_with_counts(films_data)
        print_border()
        print("Доступні жанри:")
        for idx, (genre, count) in enumerate(genres_with_counts.items(), start=1):
            print(f"{idx}. {genre} ({count})")
        print_border()

        genre_choice = input("Оберіть номер жанру: ")
        if genre_choice.isdigit():
            genre_choice = int(genre_choice)
            if 1 <= genre_choice <= len(genres_with_counts):
                selected_genre = list(genres_with_counts.keys())[genre_choice - 1]
                genre_results = search_by_genre(films_data, selected_genre)
                if genre_results:
                    print_border()
                    print(f"Знайдено фільми у жанрі {selected_genre}:")
                    for idx, film in enumerate(genre_results, start=1):
                        print(f"{idx}. {film['title']} ({film['year']})")
                    print_border()
                    film_choice = input("Оберіть номер фільму або 'exit' для виходу: ")
                    if film_choice.isdigit():
                        film_choice = int(film_choice)
                        if 1 <= film_choice <= len(genre_results):
                            display_film_info(genre_results[film_choice - 1])
                        else:
                            print("Номер фільму введено некоректно, будь ласка, вкажіть коректний номер фільму.")
                    elif film_choice.lower() == 'exit':
                        return
                    else:
                        print("Введено некоректні дані.")
                else:
                    print(f"Фільмів у жанрі {selected_genre} не знайдено.")
            else:
                print("Введено некоректний номер жанру.")
        else:
            print("Введено некоректний номер жанру.")

    else:
        print("Введено некоректний номер режиму.")

if __name__ == "__main__":
    main()
