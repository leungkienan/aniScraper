from bs4 import BeautifulSoup
import requests

url = "https://myanimelist.net/anime/season"

result = requests.get(url)
# print(result.text)
doc = BeautifulSoup(result.text, "html.parser")
stuff = doc.find_all(text="$")
print(stuff)
