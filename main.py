# -*- coding: utf-8 -*-
from functions import load_movies, save_movies, update_date, convert_size

print("------------------")
print("------Movies------")
print("------------------")


# load_movies()


def convert_value():
    with open('planilha.txt', 'r', encoding='utf-8') as file:
        for lines in file:
            file.readlines()

            for line in lines:
                value = lines.split()
                names = value[0]
                dates = value[1]
                paths = value[2]
                sizes = value[4]

                while True:
                    name = names
                    date = dates
                    path = paths
                    size = sizes

                    movies = {
                        "name": name.split(),
                        "date": update_date(date),
                        "path": path.split(),
                        "size": convert_size(size)
                    }
                    save_movies(movies)
                    exit()


if __name__ == "__main__":
    convert_value()