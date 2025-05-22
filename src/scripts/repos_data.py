import requests
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

class RepositoriesData:
    
    def __init__(self, owner):
        self.owner = owner
        self.api_url_base = 'https://api.github.com'
        self.access_token = os.getenv('ACCESS_TOKEN')
        self.headers = {'X-GitHub-Api-Version': '2022-11-28',
           'Authorization': f'token {self.access_token}'
           }


    def repos_list(self):
        repos_list = []
        page = 1
        while True:
            
            url_page = f'{self.api_url_base}/users/{self.owner}/repos?page={page}&per_page=100'
            response = requests.get(url_page, headers=self.headers)

            if response.status_code != 200:
                # print(f"❌ Error on page {page}: {response.status_code}")
                break

            data = response.json()
            if not data:
                break

            repos_list.extend(data)
            # print(f"✔️ Page {page} loaded: {len(data)} repos")
            page += 1
                
        # print(f"\nTotal repositories collected: {len(repos_list)}")
        return repos_list


    def collect_repos_name(self, repos_list):
        repos_names = [repo['name'] for repo in repos_list if 'name' in repo]
        return repos_names
    
    def collect_repos_language(self, repos_list):
        repos_languages = [repo['language'] for repo in repos_list if 'language' in repo]
        return repos_languages

        
    def create_df_lang(self):
        repos = self.repos_list()
        names = self.collect_repos_name(repos)
        langs = self.collect_repos_language(repos)

        data = pd.DataFrame()
        data['repository_name'] = names
        data['languages'] = langs

        return data
    