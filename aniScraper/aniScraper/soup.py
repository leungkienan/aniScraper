from bs4 import BeautifulSoup
import requests
import re

url = "https://anilist.co/search/anime"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")
stuff = doc.find_all(text=re.compile("Jujutsu"), limit=100)
for ice in stuff:
    print(ice.strip())
# print(doc)
