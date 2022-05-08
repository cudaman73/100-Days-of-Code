import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')

names = [x.text for x in soup.find_all(name='h3', class_='title')]
names.reverse()

movie_list = "\n".join(names)

with open("movies.txt", "w") as file:
    file.write(movie_list)


