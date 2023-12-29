import os
import json


class Film:
    def __init__(self, title, description, director, writer, cast, running_time, country, language, imdb_rating,
                 year, budget, box_office, profitable, oscar_nominated, oscar_win, trailer_link):
        self.title = title
        self.description = description
        self.director = director
        self.writer = writer
        self.cast = cast
        self.running_time = running_time
        self.country = country
        self.language = language
        self.imdb_rating = imdb_rating
        self.year = year
        self.budget = budget
        self.box_office = box_office
        self.profitable = profitable
        self.oscar_nominated = oscar_nominated
        self.oscar_win = oscar_win
        self.trailer_link = trailer_link
        self.storage_address = None
        self.save_data()
        self.upload_file()

    def save_data(self):
        film_data = {
            "Title": self.title,
            "Description": self.description,
            "Director": self.director,
            "Writer": self.writer,
            "Cast": self.cast,
            "Running time": self.running_time,
            "Country": self.country,
            "Language": self.language,
            "IMDb Rating": self.imdb_rating,
            "Year": self.year,
            "Budget": self.budget,
            "Box office": self.box_office,
            "Profitable": self.profitable,
            "Oscar Nominated": self.oscar_nominated,
            "Oscar Win": self.oscar_win,
            "Trailer": self.trailer_link
        }
        film_json = json.dumps(film_data, indent=4)

        first_letter = self.title[0].upper()
        film_storage_directory = os.path.join("film_storage", first_letter)
        film_directory = os.path.join(film_storage_directory, self.title)

        if not os.path.exists(film_storage_directory):
            os.makedirs(film_storage_directory)

        if not os.path.exists(film_directory):
            os.makedirs(film_directory)

        with open(os.path.join(film_directory, "film.json"), "w") as file:
            file.write(film_json)

        self.storage_address = film_directory

    def upload_file(self):
        first_letter = self.title[0].upper()
        film_directory = os.path.join("film_storage", first_letter)
        if not os.path.exists(film_directory):
            os.makedirs(film_directory)
        film_path = os.path.join(film_directory, f"{self.title}.txt")
        with open(film_path, "w") as file:
            file.write("Is something supposed to be here?")

    def get_film_address(self):
        if self.storage_address:
            return os.path.join(self.storage_address, f"{self.title}.txt")
        else:
            return "Film data has not been saved yet."

bloodsport = Film(
    title="Bloodsport",
    description="Frank Dux has spent most his life being trained by Tanaka to participate in the Kumite, the ultimate martial arts tournament, where participants are seriously injured, even killed. Frank decides to go despite being told by his superiors in the army that he can't because they need him. Two army officers are sent to get him and the trail leads to Hong Kong.",
    director=["Newt Arnold"],
    writer="Sheldon Lettich",
    cast=["Jean-Claude Van Damme", "Donald Gibb", "Leah Ayres"],
    running_time=92,
    country="United States",
    language="English",
    imdb_rating=6.8,
    year=1988,
    budget="$1.1 million",
    box_office="$65 million",
    profitable=True,
    oscar_nominated=False,
    oscar_win=False,
    trailer_link="https://www.imdb.com/video/vi3722091801/"
)

print(bloodsport.get_film_address())
