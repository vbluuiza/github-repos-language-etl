import requests
from dotenv import load_dotenv
import os

load_dotenv()

headers = {'X-GitHub-Api-Version': '2022-11-28',
           'Authorization': 'Bearer ' + os.getenv('ACCESS_TOKEN')
           }

api_url_base = 'https://api.github.com'
owner = 'amzn'
url = f'{api_url_base}/users/{owner}/repos'

response = requests.get(url, headers=headers)

repos_list = []
page = 1

while True:
    url_page = f'{url}?page={page}&per_page=100'
    response = requests.get(url_page, headers=headers)

    if response.status_code != 200:
        print(f"❌ Error on page {page}: {response.status_code}")
        break

    data = response.json()
    if not data:
        break

    repos_list.extend(data)
    print(f"✅ Page {page} loaded: {len(data)} repos")
    page += 1
        
print(f"\nTotal repositories collected: {len(repos_list)}")
