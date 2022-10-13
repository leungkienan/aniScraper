from bs4 import BeautifulSoup
import requests
import re

# url = "https://anilist.co/search/anime"
# url = "https://myanimelist.net/"
search = "Chainsaw"


result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")
queryS = doc.find_all(text=re.compile(search), limit=100)
for anime in queryS:
    print(anime.strip())
    # if ice is None:
    #     break
    # print("no results found")

# print(doc)

# need the text field to be based on the input or saved titles.

# user enters in anime name
# returns list of anime close to entry
# user picks the anime to add
# this will save the anime to the db list
#