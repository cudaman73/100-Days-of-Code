from bs4 import BeautifulSoup
import requests
import numpy

# with open("website.html", encoding='utf8') as file:
#     website_data = BeautifulSoup(file, 'html.parser')
#
#
# print(website_data.p.a)

response = requests.get("https://news.ycombinator.com/")

soup = BeautifulSoup(response.text, 'html.parser')

# grab articles and sort the data we want into lists
articles = soup.find_all(name='a', class_='titlelink')
articles_text = [x.text for x in articles]
articles_link = [x.get('href') for x in articles]
article_score = [int(x.text.replace(" points", "")) for x in soup.find_all(name='span', class_='score')]

# highest score
max_score = numpy.argmax(article_score)

# print element from each array with highest score
print(articles_text[max_score])
print(articles_link[max_score])
print(article_score[max_score])

# score_list = soup.select('span.score')
#
# scores = [int(x.text.replace(" points", "")) for x in score_list]
#
# print(scores)
