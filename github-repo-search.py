
import requests
import json
from bs4 import BeautifulSoup

query="python"
res = requests.get(f'https://github.com/search?o=desc&q={query}&s=updated&type=Repositories')
soup = BeautifulSoup(res.text, 'html.parser')

start = soup.find_all('ul',class_='repo-list')
github=[]

for item in start:
    repo = item.find_all('div',class_='f4 text-normal')

for item2 in repo:
    repo2 = item2.find_all('a')[0]
    title=repo2.text
    link="https://github.com" + repo2['href']
    temp = {
    'title': title,
    'link': link 
    }
    github.append(temp)

print(github)


