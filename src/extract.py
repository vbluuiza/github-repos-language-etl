from src.scripts.repos_data import RepositoriesData



amazon_repo = RepositoriesData('amzn')
most_used_langs_amzn = amazon_repo.create_df_lang()
# print(most_used_langs_amzn)

netflix_repo = RepositoriesData('netflix')
most_used_langs_netflix = netflix_repo.create_df_lang()
# print(most_used_langs_netflix)

spotify_repo = RepositoriesData('spotify')
most_used_langs_spotify = spotify_repo.create_df_lang()
# print(most_used_langs_spotify)
