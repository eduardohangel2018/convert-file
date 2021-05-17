# -*- coding: utf-8 -*-
import json
import os
import re
from datetime import datetime


# Formata a Data
def update_date(new_date: str) -> str:
    return datetime.strptime(new_date, "%d-%m-%Y").date().strftime("%d/%m/%Y")


# Formata o tamanho
def convert_size(new_size: str) -> str:
    value = int(new_size) / 1024 / 1024 / 1024
    if value != '':
        return f"{value:.2f} GB"
    return f"{int(value)}GB"


# Retorna a lista de filmes presente no arquivo
def load_movies(all_movies):
    all_movies = {}
    if os.path.exists('new_movies.json'):
        with open('new_movies.json', 'r') as file:
            all_movies = json.load(file)
    return all_movies


# Armazena os dados dos movies
def save_movies(movies):
    with open('new_movies.json', 'w') as file:
        json.dump(movies, file)


# Converte o valor size
# value = input("Entre com o valor:")
# value = int(value)
# convert_value = size(value)
# print(convert_value)
