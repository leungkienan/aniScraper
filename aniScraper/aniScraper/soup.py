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

# need the text field to be based on the input or saved titles.

# user enters in anime name
# returns list of anime close to entry
# user picks the anime to add
# this will save the anime to the db list
#