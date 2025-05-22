from src.extract import most_used_langs_amzn, most_used_langs_netflix, most_used_langs_spotify
import pandas as pd

path = 'data/processed/'

def load_data(data, directory):
    data.to_csv(f'{path}/{directory}', index=True, index_label='index')


load_data(most_used_langs_amzn, 'amazon_langs.csv')
load_data(most_used_langs_netflix, 'netflix_langs.csv')
load_data(most_used_langs_spotify, 'spotify_langs.csv')
