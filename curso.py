import requests
from bs4 import BeautifulSoup
from inflection import titleize

def titles_generator(links):
    titles = []

    def post_formatter(url):
        if 'posts' in url:
            url = url.split('/')[-1]
            url = url.replace('-', ' ')
            url = titleize(url)
            titles.append(url)

   
    for link in links:
        post_formatter(link['href'])

        return titles

r = requests.get('http://www.dailysmarty.com/topics/python')
soup = BeautifulSoup(r.text, 'hmtl.parser')
links = soup.find_all('a')

titles = titles_generator(links)

for title in titles:
    print(title)