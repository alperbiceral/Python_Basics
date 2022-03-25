import requests
from bs4 import BeautifulSoup

res = requests.get("https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc")
soup = BeautifulSoup(res.text, "html5lib")
list = soup.find("div", {"class":"lister-list"}).find_all("div", {"class":"lister-item mode-advanced"})

names = []
newNames = []
for film in list:
	names.append(film.find("div", {"class":"lister-item-content"}).find("h3").text.strip())

for i in range(len(names)):
	newNames.append(names[i].split('\n'))
	print(newNames[i][2].strip())
